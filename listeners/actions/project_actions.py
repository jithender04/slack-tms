from user_interface import project_modal
def create_project_modal(ack, body, logger, client):
    try:
        ack()
        client.views_open(trigger_id=body["trigger_id"], view=project_modal())

    except Exception as e:
        logger.error(e)
