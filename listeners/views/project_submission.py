from helpers.services import service_create_project


def project_submission(view, ack, body, client, logger, say):
    try:
        ack()
        data = view["state"]["values"]
        payload = {}

        payload["name"] = data["project_name"]["project_name"]["value"].replace(" ", "-")
        payload["workspace"] = body["team"]["id"]
        payload["admin"] = body["user"]["id"]
        payload["description"] = data["project_description"]["project_description"]["value"]
        payload["dev_team"] = data["project_developers"]["project_developers"]["selected_users"]
        payload["qa_team"] = data["project_qa"]["project_qa"]["selected_users"]
        payload["project_manager"] = data["project_manager"]["project_manager"]["selected_user"]

        response = service_create_project(payload, payload["admin"])

        if('success' in response):
            channel = client.conversations_create(name=payload["name"], is_private=True)
            print(channel)
            if not channel["ok"]:
                say(channel=body["user"]["id"], text="Permission Needed to Create Channel")
            else:
                channel = channel["channel"]

                users = [payload["project_manager"], payload["admin"]]
                users.extend(payload["dev_team"])
                users.extend(payload["qa_team"])
                # print(users)
                client.conversations_invite(channel=channel["id"], users=users)

                say(channel=channel["id"], text=message(payload))

    except Exception as e:
        logger.error(e)

def message(form):
    new_line = '\n'
    return f"""Welcome to *{form['name']}* project!{new_line*2}\
*Project Manager:*{new_line}\
<@{form['project_manager']}>{new_line*2}\
*Dev team:*{new_line}\
{new_line.join(map(lambda x: f'<@{x}>', form['dev_team']))}{new_line*2}\
*QA team:*{new_line}\
{new_line.join(map(lambda x: f'<@{x}>', form['qa_team']))}{new_line}"""
