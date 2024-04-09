from .task_actions import *
from .login_actions import *

def register(app):
    app.action("create-task")(create_task_model)
    app.action("assignee-select")(handle_some_action)
    app.action("date-select")(handle_some_action)
    app.action("status-select-action")(handle_some_action)
    app.action("update_task")(update_task_model)
    app.action("delete_task")(delete_task_model)
    app.action("login")(show_login_modal)
