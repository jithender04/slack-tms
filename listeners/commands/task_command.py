import json
from user_interface import static_task_model, assignee_block

def create_task_model(ack, client, body):
    ack()
    model = static_task_model()
    model["private_metadata"] = json.dumps({"channel_id": body["channel_id"]})
    model["blocks"].append(assignee_block())
    client.views_open(trigger_id=body["trigger_id"], view=model)
