from user_interface import login_modal

def show_login_modal(ack, client, body):
    ack()
    client.views_open(trigger_id=body["trigger_id"], view=login_modal(body["user"]["id"]))
