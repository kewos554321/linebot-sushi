# from linebot.v3.messaging import Configuration, ApiClient, MessagingApi, ReplyMessageRequest, TextMessage
from linebot.v3.webhooks import PostbackEvent, MessageEvent, TextMessageContent
from app import handler
from .services import text_message as stm
from .services import template_message as stpm
from .services import location_message as slm
from .utils import common as cmn

@handler.add(PostbackEvent)
def handle_postback(event):
    # 這裡處理 PostbackEvent
    print("\n=>\nevent: ", event)

    data = event.postback.data
    if "action=select_datetime" in data:
        selected_datetime = event.postback.params['datetime']
        reply_message = f"你選擇的時間是：{selected_datetime}"
        # line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_message))
    # 例如，取得 postback 的 data:
    # data = event.postback.data

    # # 若你有使用 DatetimePickerAction，你也可以取得用戶所選的日期或時間
    # if 'date' in event.postback.params:
    #     selected_date = event.postback.params['date']
    # elif 'time' in event.postback.params:
    #     selected_time = event.postback.params['time']
    # elif 'datetime' in event.postback.params:
    #     selected_datetime = event.postback.params['datetime']