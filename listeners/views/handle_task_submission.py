import json
from user_interface import update_home_tab, message_attachment, dynamic_message_block
from helpers.services import service_create_task, service_update_task

def handle_submission(ack, body, client, say, logger):
    try:
        isTaskUpdated = False
        payload = body["view"]["state"]["values"]
        data = json.loads(body["view"]["private_metadata"] or '{}')
        ack()

        if "task_id" in data:
            response = service_update_task(data["task_id"], payload, body["user"]["id"])
            isTaskUpdated = True
        else:
            response = service_create_task(payload, body["user"]["id"], data)

        update_home_tab(client, body["user"]["id"], logger)
        attachments = message_attachment(response)
        if isTaskUpdated:
            say(
                blocks=dynamic_message_block("*Task has been updated successfully*"),
                attachments=attachments,
                channel=body["user"]["id"],
                text="Task has been updated successfully"
            )
        else:
            if "channel_id" in data:
                say(
                    blocks=dynamic_message_block(f"<@{body["user"]["id"]}> *has assigned a task for <@{response["assignee"]}>*"),
                    attachments=attachments,
                    channel=data["channel_id"],
                    text="Task has been created successfully",
                )
            else:
                say(
                    blocks=dynamic_message_block("*Task has been created successfully*"),
                    attachments=attachments,
                    channel=body["user"]["id"],
                    text="Task has been created successfully"
                )

        # if not body["user"]["id"] == assignee_user_id:
        #     say(
        #         blocks=dynamic_message_block(f'*Task has been assigned to you by <@{body["user"]["id"]}>*'),
        #         attachments=attachments,
        #         channel=assignee_user_id,
        #         text=f'Task has been assigned to you by <@{body["user"]["id"]}>'
        #     )

    except Exception as e:
        print(f"An error occurred: {e}")
