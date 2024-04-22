from slack_bolt import App
from .events import app_home_opened_callback, member_left_channel_callback


def register(app: App):
    app.event("app_home_opened")(app_home_opened_callback)
    app.event("member_left_channel")(member_left_channel_callback)
