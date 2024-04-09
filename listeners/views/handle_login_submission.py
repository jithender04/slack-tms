from helpers.services import service_login
from helpers.db import insert_document
from user_interface import update_home_tab

def handle_login_submission(ack, body, client, logger):
    try:
        ack()
        payload = body["view"]["state"]["values"]
        print(payload) 
        response = service_login(body["user"]["id"], payload["login_password"]["login_password"]["value"])
        insert_document({
            "user_id": body["user"]["id"],
            "token": response["token"]
        })
        update_home_tab(client, body["user"]["id"], logger)

    except Exception as e:
        print(f"An error occurred on login submission: {e}")
