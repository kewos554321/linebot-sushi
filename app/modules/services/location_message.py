from linebot.models import LocationMessage
from app import app
from linebot import LineBotApi
from ..utils import common as cmn

def create_location_message(reply_token, filename):
    line_bot_api = LineBotApi(app.config['LINE_CHANNEL_ACCESS_TOKEN'])
    data = cmn.handle_json_file("location_messages", filename)
    print("\n=>\nlocation-data: ", data)
    location_msg = LocationMessage(
        title=data["title"],
        address=data["address"],
        latitude=data["latitude"],
        longitude=data["longitude"]
    )

    line_bot_api.reply_message(reply_token, location_msg)

def show_location_message(reply_token):
    filename = "sushi_location.json"
    create_location_message(reply_token, filename)