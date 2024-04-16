from .handle_task_submission import handle_submission
from .handle_login_submission import handle_login_submission
from .project_submission import project_submission

def register(app):
    app.view("submit_task_model")(handle_submission)
    app.view("submit_login_model")(handle_login_submission)
    app.view("create_project")(project_submission)
