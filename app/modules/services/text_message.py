from linebot.v3.messaging import Configuration, ApiClient, MessagingApi, ReplyMessageRequest, TextMessage
from app import configuration
from ..utils import common as cmn
def preprocess_message(src_type, msg_text):
    if src_type == "group" and msg_text.startswith("/"):
        return msg_text[len("/ "):]
    return msg_text

def send_reply_message(reply_token, message_text):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=reply_token,
                messages=[TextMessage(text=message_text)]
            )
        )

def send_reply_message_with_resource(reply_token, filename):

    reply_data = cmn.handle_json_file("reply_message_texts", filename)

    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=reply_token,
                messages=[TextMessage(text=reply_data["text"])]
            )
        )