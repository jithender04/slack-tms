import re
from helpers.services import service_update_project

def remove_user(ack, payload, say, client):
    ack()
    # print(payload["text"])
    match = re.search(r"<@(.*?)\|", payload["text"])
    # print(match)
    if match:
        extracted_id = match.group(1)
        client.conversations_kick(channel=payload["channel_id"],user=extracted_id)
        say(channel=payload["channel_id"], text=f"<@{extracted_id}> has been removed from {payload["channel_name"]} by <@{payload['user_id']}>")
            
