def assignee_block(assignee=None):
    block = {
        "type": "input",
        "block_id": "create_task_assignee",
        "element": {
            "type": "users_select",
            "placeholder": {"type": "plain_text", "text": "Select users", "emoji": True},
            "action_id": "assignee-select"
        },
        "label": {"type": "plain_text", "text": "Assignee", "emoji": True}
    }
    
    if assignee:
        block["element"]["initial_user"] = assignee
    
    return block

def task_model(title, description, status, assignee, due_date, payload):

    status_option = {"text": {"type": "plain_text", "text": status, "emoji": True}, "value": status}
    return {
        "type": "modal",
        "callback_id": "submit_task_model",
        "title": {"type": "plain_text", "text": "Edit task", "emoji": True},
        "submit": {"type": "plain_text", "text": "Update", "emoji": True},
        "close": {"type": "plain_text", "text": "Cancel", "emoji": True},
        "private_metadata": payload,
        "blocks": [
            {
                "type": "input",
                "block_id": "create_task_title",
                "element": {"type": "plain_text_input", "action_id": "text", "initial_value": title},
                "label": {"type": "plain_text", "text": "Title", "emoji": True},
            },
            {
                "type": "input",
                "block_id": "create_task_description",
                "element": {"type": "plain_text_input", "action_id": "text", "initial_value": description},
                "label": {"type": "plain_text", "text": "Description", "emoji": True},
            },
            {
                "type": "actions",
                "block_id": "create_task_actions",
                "elements": [
                    {
                        "type": "datepicker",
                        "placeholder": {"type": "plain_text", "text": "Select a date", "emoji": True},
                        "action_id": "date-select",
                        "initial_date": due_date,
                    },
                    # {
                    #     "type": "users_select",
                    #     "placeholder": {"type": "plain_text", "text": "Select a user", "emoji": True},
                    #     "action_id": "assignee-select",
                    #     "initial_user": assignee
                    # },
                    {
                        "type": "static_select",
                        "placeholder": {"type": "plain_text", "text": "Ready?", "emoji": True},
                        "initial_option": status_option,
                        "options": [
                            {"text": {"type": "plain_text", "text": "Ready", "emoji": True}, "value": "Ready"},
                            {"text": {"type": "plain_text", "text": "In Progress", "emoji": True}, "value": "In Progress"},
                            {"text": {"type": "plain_text", "text": "Ready For QA", "emoji": True}, "value": "Ready For QA"},
                            {"text": {"type": "plain_text", "text": "Done", "emoji": True}, "value": "Done"},
                        ],
                        "action_id": "status-select-action",
                    }
                ],
            },
            # {
            #     "type": "input",
            #     "block_id": "create_task_due_date",
            #     "element": {
            #         "type": "datepicker",
            #         "initial_date": due_date,
            #         "placeholder": {
            #             "type": "plain_text",
            #             "text": "Select a date",
            #             "emoji": True
            #         },
            #         "action_id": "date-select"
            #     },
            #     "label": {
            #         "type": "plain_text",
            #         "text": "Due date",
            #         "emoji": True
            #     }
            # }
        ],
    }

def static_task_model():
    return {
        "type": "modal",
        "callback_id": "submit_task_model",
        "title": {"type": "plain_text", "text": "Create a task", "emoji": True},
        "submit": {"type": "plain_text", "text": "Submit", "emoji": True},
        "close": {"type": "plain_text", "text": "Cancel", "emoji": True},
        "blocks": [
            {
                "type": "input",
                "block_id": "create_task_title",
                "element": {"type": "plain_text_input", "action_id": "text", "placeholder": {"type": "plain_text", "text": " "}},
                "label": {"type": "plain_text", "text": "Title", "emoji": True},
            },
            {
                "type": "input",
                "block_id": "create_task_description",
                "element": {"type": "plain_text_input", "action_id": "text", "placeholder": {"type": "plain_text", "text": " "}},
                "label": {"type": "plain_text", "text": "Description", "emoji": True},
            },
            {
                "type": "actions",
                "block_id": "create_task_actions",
                "elements": [
                    {
                        "type": "datepicker",
                        "placeholder": {"type": "plain_text", "text": "Select a date", "emoji": True},
                        "action_id": "date-select",
                    },
                    {
                        "type": "static_select",
                        "placeholder": {"type": "plain_text", "text": "Ready?", "emoji": True},
                        "options": [
                            {"text": {"type": "plain_text", "text": "Ready", "emoji": True}, "value": "Ready"},
                            {"text": {"type": "plain_text", "text": "In Progress", "emoji": True}, "value": "In Progress"},
                            {"text": {"type": "plain_text", "text": "Ready For QA", "emoji": True}, "value": "Ready For QA"},
                            {"text": {"type": "plain_text", "text": "Done", "emoji": True}, "value": "Done"},
                        ],
                        "action_id": "status-select-action",
                    }
                ],
            },
            # {
            #             "type": "users_select",
            #             "placeholder": {"type": "plain_text", "text": "Select a user", "emoji": True},
            #             "action_id": "assignee-select"
            #         },
            # {
            #     "type": "input",
            #     "block_id": "create_task_due_date",
            #     "element": {
            #         "type": "datepicker",
            #         "placeholder": {
            #             "type": "plain_text",
            #             "text": "Select a date",
            #             "emoji": True
            #         },
            #         "action_id": "date-select"
            #     },
            #     "label": {
            #         "type": "plain_text",
            #         "text": "Due date",
            #         "emoji": True
            #     }
            # }
        ],
    }

def homePage(userID):
    view = (
        {
            "type": "home",
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "*Welcome home, <@" + userID + "> :house:*",
                    },
                },
                {
                    "type": "actions",
                    "elements": [
                        {
                            "type": "button",
                            "text": {"type": "plain_text", "text": "Create a Task", "emoji": True},
                            "style": "primary",
                            "action_id": "create-task",
                        },
                        {
                            "type": "button",
                            "text": {"type": "plain_text", "text": "Create a Project", "emoji": True},
                            "style": "primary",
                            "action_id": "create_project",
                        },
                        {
                            "type": "button",
                            "text": {"type": "plain_text", "text": "Invite members", "emoji": True},
                            "style": "primary",
                            "action_id": "invite_project",
                        }
                    ],
                },
                {
                    "type": "context",
                    "elements": [
                        {
                            "type": "image",
                            "image_url": "https://api.slack.com/img/blocks/bkb_template_images/placeholder.png",
                            "alt_text": "placeholder",
                        }
                    ],
                },
                {"type": "section", "text": {"type": "mrkdwn", "text": "*Assigned tasks*"}},
                {"type": "divider"},
            ],
        }
    )
    return view

def dynamic_block(data):
    return {
        "type": "section",
        "text": {"type": "mrkdwn", "text": f"*Title* : {data["title"]}\n*Description*:  {data["description"]}\n*Status* : {data["status"]}\n*Due* : {data["dueDate"]}"},
    }

def update_button(task_id, showDeleteButton):
    block = {
        "type": "actions",
        "block_id": f"update_task_button_{task_id}",
        "elements": [
            {
                "type": "button",
                "text": {"type": "plain_text", "text": "Edit", "emoji": True},
                "value": task_id,
                "action_id": "update_task",
            }
        ],
    }
    if showDeleteButton:
        block["elements"].append(
            {
                "type": "button",
                "text": {"type": "plain_text", "text": "Delete", "emoji": True},
                "style": "danger",
                "value": task_id,
                "action_id": "delete_task",
            }
        )
    return block

def update_home_tab(client, user_id, logger):
    from helpers.services import service_get_tasks
    from datetime import datetime
    try:
        tasks = service_get_tasks(user_id)
        view = homePage(user_id)
        for key in tasks:
            key["dueDate"] = datetime.strptime(key["dueDate"], "%a, %d %b %Y %H:%M:%S %Z").strftime("%d %b %Y")
            view["blocks"].append(dynamic_block(key))
            view["blocks"].append(update_button(key["_id"], key["assignee"] == key["userId"]))
            view["blocks"].append({"type": "divider"})
        client.views_publish(user_id=user_id, view=view)
    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")

def dynamic_message_block(message):
    return [{
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": message,
        }
    }]

def message_attachment(response):
    from datetime import datetime
    response["dueDate"] = datetime.strptime(response["dueDate"], "%Y-%m-%d %H:%M:%S").strftime("%d %b %Y")
    return [
        {
            "blocks": [
                {"type": "section", "text": {"type": "mrkdwn", "text": "*Task Details*"}},
                {"type": "section", "text": {"type": "mrkdwn", "text": f"*Title*: {response["title"]}"}},
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": f"*Description*:{response["description"]}"},
                },
                {
                    "type": "section",
                    "fields": [
                        {"type": "mrkdwn", "text": f"*Assignee*: <@{response["assignee"]}>"},
                        {"type": "mrkdwn", "text": f"*Status*: {response["status"]}"},
                    ],
                },
                {"type": "section", "text": {"type": "mrkdwn", "text": f"*Due Date*:{response["dueDate"]}"}},
            ],
            "color": "#36a64f",
        }
    ]

def login_page(user_id):
    return {
        "type": "home",
        "blocks": [
            {"type": "section", "text": {"type": "plain_text", "text": "Please Login to continue"}}, 
            {
                "type": "actions",
                "elements": [
                    {"type": "button", "text": {"type": "plain_text", "text": "Login"}, "value": user_id, "action_id": "login","style": "primary"}
                ],
            }
        ]
    }

def login_modal(user_id):
    return {
        "type": "modal",
        "title": {"type": "plain_text", "text": "Login", "emoji": True},
        "submit": {"type": "plain_text", "text": "Login", "emoji": True},
        "close": {"type": "plain_text", "text": "Cancel", "emoji": True},
        "callback_id": "submit_login_model",
        "blocks": [
            {"type": "context", "elements": [{"type": "plain_text", "text": f"Username: {user_id}", "emoji": True}]},
            {
                "type": "input",
                "block_id": "login_password",
                "element": {"type": "plain_text_input", "action_id": "login_password"},
                "label": {"type": "plain_text", "text": "Password", "emoji": True},
            },
        ],
    }

def project_modal():
    return {
        "type": "modal",
        "callback_id": "create_project",
        "title": {
            "type": "plain_text",
            "text": "Enter Project details",
            "emoji": True,
        },
        "submit": {"type": "plain_text", "text": "Create", "emoji": True},
        "close": {"type": "plain_text", "text": "Cancel", "emoji": True},
        "blocks": [
            {
                "block_id": "project_name",
                "type": "input",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "project_name",
                    "placeholder": {"type": "plain_text", "text": " "},
                },
                "label": {
                    "type": "plain_text",
                    "text": "Project Name",
                    "emoji": True,
                },
            },
            {
                "block_id": "project_description",
                "type": "input",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "project_description",
                    "placeholder": {"type": "plain_text", "text": " "},
                },
                "label": {
                    "type": "plain_text",
                    "text": "Description",
                    "emoji": True,
                },
            },
            {
                "block_id": "project_developers",
                "type": "input",
                "element": {
                    "action_id": "project_developers",
                    "type": "multi_users_select",
                    "placeholder": {"type": "plain_text", "text": " "},
                },
                "label": {
                    "type": "plain_text",
                    "text": "Select Developers",
                    "emoji": True,
                },
            },
            {
                "block_id": "project_qa",
                "type": "input",
                "element": {
                    "action_id": "project_qa",
                    "type": "multi_users_select",
                    "placeholder": {"type": "plain_text", "text": " "},
                },
                "label": {
                    "type": "plain_text",
                    "text": "Select QA's",
                    "emoji": True,
                },
            },
            {
                "block_id": "project_manager",
                "type": "input",
                "element": {
                    "action_id": "project_manager",
                    "type": "multi_users_select",
                    "placeholder": {"type": "plain_text", "text": " "},
                },
                "label": {
                    "type": "plain_text",
                    "text": "Select Project Manager",
                    "emoji": True,
                },
            }
        ],
    }

def invite_modal(payload):
    return {
        "type": "modal",
        "title": {"type": "plain_text", "text": "Invite to project", "emoji": True},
        "submit": {"type": "plain_text", "text": "Invite", "emoji": True},
        "close": {"type": "plain_text", "text": "Cancel", "emoji": True},
        "callback_id": "submit_invite_members_model",
        "private_metadata": payload,
        "blocks": [
            {
                "block_id": "project_developers",
                "type": "input",
                "optional": True,
                "element": {
                    "action_id": "project_developers",
                    "type": "multi_users_select",
                    "placeholder": {"type": "plain_text", "text": " "}
                },
                "label": {
                    "type": "plain_text",
                    "text": "Select Developers",
                    "emoji": True,
                },
            },
            {
                "block_id": "project_qa",
                "type": "input",
                "optional": True,
                "element": {
                    "action_id": "project_qa",
                    "type": "multi_users_select",
                    "placeholder": {"type": "plain_text", "text": " "}
                },
                "label": {
                    "type": "plain_text",
                    "text": "Select QA's",
                    "emoji": True,
                },
            },
            {
                "block_id": "project_manager",
                "type": "input",
                "optional": True,
                "element": {
                    "action_id": "project_manager",
                    "type": "multi_users_select",
                    "placeholder": {"type": "plain_text", "text": " "}
                },
                "label": {
                    "type": "plain_text",
                    "text": "Select Project Manager",
                    "emoji": True,
                },
            }
        ],
    }
