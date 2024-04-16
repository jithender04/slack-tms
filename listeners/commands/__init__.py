from slack_bolt import App
from .task_command import create_task_model


def register(app: App):
    app.command("/create-task")(create_task_model)
