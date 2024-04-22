from helpers.services import service_create_project, service_update_project, service_create_account

def project_submission(view, ack, body, client, logger, say):
    try:
        ack()
        data = view["state"]["values"]
        payload = {}
        payload["name"] = data["project_name"]["project_name"]["value"].replace(" ", "-")
        payload["workspace"] = body["team"]["id"]
        # payload["admin"] = body["user"]["id"]
        payload["description"] = data["project_description"]["project_description"]["value"]
        # payload["dev_team"] = data["project_developers"]["project_developers"]["selected_users"]
        # payload["qa_team"] = data["project_qa"]["project_qa"]["selected_users"]
        # payload["project_manager"] = data["project_manager"]["project_manager"]["selected_users"]
        users = [body["user"]["id"]]
        users.extend(data["project_developers"]["project_developers"]["selected_users"])
        users.extend(data["project_qa"]["project_qa"]["selected_users"])
        users.extend(data["project_manager"]["project_manager"]["selected_users"])
        users = list(set(users))
        payload['users'] = users     
        channel = client.conversations_create(name=payload["name"], is_private=True)
        if not channel["ok"]:
            say(channel=body["user"]["id"], text="Permission Needed to Create Channel")
        else:
            channel = channel["channel"]
            payload["channel_id"] = channel["id"]
            response = service_create_project(payload, payload["admin"])
            if('success' in response):
                client.conversations_invite(channel=channel["id"], users=users)
                say(channel=channel["id"], text=message(payload))

    except Exception as e:
        logger.error(e)

def invite_members_submission(ack, view, body, logger, say, client):
    import json
    try:
        ack()
        data = view["state"]["values"]
        payload = {}
        payload["dev_team"] = data["project_developers"]["project_developers"]["selected_users"]
        payload["qa_team"] = data["project_qa"]["project_qa"]["selected_users"]
        payload["project_manager"] = data["project_manager"]["project_manager"]["selected_users"]

        metadata = json.loads(view["private_metadata"] or "{}")
        if "channel_id" in metadata:
            payload["project_manager"] = create_account(payload["project_manager"])
            payload["dev_team"] = create_account(payload["dev_team"])
            payload["qa_team"] = create_account(payload["qa_team"])
            users = []
            users.extend(payload["project_manager"])
            users.extend(payload["dev_team"])
            users.extend(payload["qa_team"])
            response = service_create_account(users)
            existing_users = set(response['existing_users'])
            channel = client.conversations_info(channel=metadata["channel_id"])
            if channel['ok']: 
                channel = channel['channel']
                for user in payload["project_manager"]:
                    say(
                        channel=user["username"],
                        blocks=project_assigned_message(
                            channel,
                            user["username"],
                            user["password"],
                            "project_manager",
                            user["username"] in existing_users,
                        ),
                        text="A project has been assigned to you.",
                    )
                for user in payload["dev_team"]:
                    say(
                        channel=user["username"],
                        blocks=project_assigned_message(
                            channel,
                            user["username"],
                            user["password"],
                            "dev_team",
                            user["username"] in existing_users,
                        ),
                        text="A project has been assigned to you.",
                    )
                for user in payload["qa_team"]:
                    say(
                        channel=user["username"],
                        blocks=project_assigned_message(
                            channel,
                            user["username"],
                            user["password"],
                            "qa_team",
                            user["username"] in existing_users,
                        ),
                        text="A project has been assigned to you.",
                    )

    except Exception as e:
        logger.error(f'{e} in invite_members_submission function')

def create_account(users):
    user_dicts = []
    for user_id in users:
        user_dict = {"username": user_id, "password": '1234'}
        user_dicts.append(user_dict)
    return user_dicts

def message(form):
    new_line = '\n'
    return f"""Welcome to *{form['name']}* project!{new_line*2}\
*Project Manager:*{new_line}\
<@{form['project_manager']}>{new_line*2}\
*Dev team:*{new_line}\
{new_line.join(map(lambda x: f'<@{x}>', form['dev_team']))}{new_line*2}\
*QA team:*{new_line}\
{new_line.join(map(lambda x: f'<@{x}>', form['qa_team']))}{new_line}"""

def project_assigned_message(channel, username, pwd, role, isExistingUser):
    message = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"You have been invited to *{channel['name']}* as part of {role}\n",
            },
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Join", "emoji": True},
                "style": "primary",
                "value": f"{channel['id']}:{role}:{channel['name']}",
                "action_id": "join_project_button",
            },
        }
    ]

    if not isExistingUser:
        message.append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"Please login with below credentials in app home page to start",
                },
                "fields": [
                    {"type": "mrkdwn", "text": f"Username:\n {username}"},
                    {"type": "mrkdwn", "text": f"Password:\n {pwd}"},
                ],
            }
        )

    return message
