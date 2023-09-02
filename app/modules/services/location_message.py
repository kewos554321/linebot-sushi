from linebot.models import LocationMessage
from app import app
from linebot import LineBotApi
from ..utils import common as cmn

def create_location_message(reply_token, filename):
    line_bot_api = LineBotApi(app.config['LINE_CHANNEL_ACCESS_TOKEN'])
    data = cmn.handle_json_file("template_messages", filename)
    print("\n=>\nlocation-data: ", data)
    location_msg = LocationMessage(
        title='My Office',
        address='123 Main St, Anytown, Country',
        latitude=35.6895,
        longitude=139.6917
    )

    line_bot_api.reply_message(reply_token, location_msg)

