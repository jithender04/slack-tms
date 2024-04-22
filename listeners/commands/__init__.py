from slack_bolt import App
from .task_command import create_task_model
from .project_commands import remove_user


def register(app: App):
    app.command("/create-task")(create_task_model)
    app.command("/rm-user")(remove_user)
