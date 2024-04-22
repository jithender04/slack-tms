import json
from user_interface import project_modal, invite_modal
from helpers.services import service_update_project, headers

def create_project_modal(ack, body, logger, client):
    try:
        ack()
        client.views_open(trigger_id=body["trigger_id"], view=project_modal())

    except Exception as e:
        logger.error(e)

def invite_project_modal(ack, body, logger, client):
    try:
        ack()
        payload = json.dumps({"channel_id": "C06UGEC5J9H"})
        client.views_open(trigger_id=body["trigger_id"], view=invite_modal(payload))

    except Exception as e:
        logger.error(e)


def join_project_modal(ack, body, logger, client, action, say):
    try:
        ack()
        value = action['value'].split(":")
        payload = {"role": value[1], "channel_id": value[0], 'channel_name': value[2], 'addUser': True}
        if headers(body['user']['id']) is None:
            say(text = 'Please Login to join project', channel=body['user']['id'])
        else:
            response = service_update_project(value[0], payload, body['user']['id'])
            if('success' in response):
                client.conversations_invite(channel=value[0], users=[body["user"]["id"]])
                client.chat_update(channel=body["channel"]["id"],ts=body["message"]["ts"], text=f"*Message Update*: You have now joined in {value[2]} project")
                say(channel=value[0], text=f"\n<@{body["user"]["id"]}> joined as part of the {payload['role']}")
    except Exception as e:
        logger.error(f'{e} in function join_project_modal')

