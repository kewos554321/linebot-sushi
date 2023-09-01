from linebot.v3.messaging import Configuration, ApiClient, MessagingApi, ReplyMessageRequest, TextMessage
from linebot.v3.webhooks import MessageEvent, TextMessageContent
from config import LINE_CHANNEL_ACCESS_TOKEN
from app import handler
configuration = Configuration(access_token=LINE_CHANNEL_ACCESS_TOKEN)

@handler.add(MessageEvent, message=TextMessageContent)
def handle_messages(event):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=event.message.text)]
            )
        )
