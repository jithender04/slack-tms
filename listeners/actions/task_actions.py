import json
from user_interface import task_model, static_task_model, update_home_tab
from helpers.services import service_get_task, service_delete_task


def create_task_model(ack, client, body):
    ack()
    client.views_open(trigger_id=body["trigger_id"], view=static_task_model())

def handle_some_action(ack):
    ack()

def update_task_model(ack, body, client, action):
    ack()
    task = service_get_task(action["value"], body["user"]["id"])
    task["dueDate"] = task["dueDate"].split(" ")[0]
    payload = json.dumps({"task_id": action["value"]})
    update_task_model_view = task_model(
        task["title"], task["description"], task["status"], task["assignee"], task["dueDate"], payload
    )
    client.views_open(trigger_id=body["trigger_id"], view=update_task_model_view)

def delete_task_model(ack, body, client, action, logger, say):
    ack()
    service_delete_task(action["value"], body["user"]["id"])
    update_home_tab(client, body["user"]["id"], logger)
    say("task has been deleted successfully", channel=body["user"]["id"])
