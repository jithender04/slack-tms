from logging import Logger
from user_interface import update_home_tab, login_page
from helpers.db import fetch_document
from helpers.services import service_update_project

def is_logged_in(user):
    result = fetch_document(user)
    return True if result is not None else False

def app_home_opened_callback(client, event, logger: Logger):
    if event["tab"] != "home":
        return  
    elif is_logged_in(event["user"]):
        update_home_tab(client, event["user"], logger)
    else:
        client.views_publish(user_id=event["user"], view=login_page(event["user"]))

def member_left_channel_callback(event,say):
    # print(event)
    service_update_project(
        event["channel"],{
            "removeUser": True,
        },
        event["user"],
    )
    say(channel=event["channel"], text=f"<@{event["user"]}> left project")
