# from linebot.v3.messaging import Configuration, ApiClient, MessagingApi, ReplyMessageRequest, TextMessage
from linebot.v3.webhooks import MessageEvent, TextMessageContent
from app import handler
from .services import text_message as stm
from .services import template_message as stpm
from .services import location_message as slm
from .utils import common as cmn

@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    print("\nevent=", event)
    src_user_id, src_group_id, msg_text, reply_token = get_event_attr(event)
    source_id = src_user_id if src_group_id is None else src_group_id
    if msg_text == "h": 
        filename = "help.json"
        stm.send_reply_message_with_resource(reply_token, filename)
    elif msg_text == "t":
        stpm.do_template_test(source_id)
    elif msg_text == "cr":
        stpm.show_carousel_test(source_id)
    elif msg_text == "cf":
        stpm.show_confirm_test(source_id)
    elif msg_text == "ic":
        stpm.show_imagecarousel_test(source_id)
    elif msg_text == "menu":
        stpm.show_shushi_menu(source_id)
    elif msg_text == "我想要訂位預約":
        stpm.show_shushi_reservation_step1(source_id)
    elif msg_text == "我想看今日特餐":
        filename = "test.json"
        stm.send_reply_message_with_resource(reply_token, filename) 
    elif msg_text == "我想看菜單":
        filename = "test.json"
        stm.send_reply_message_with_resource(reply_token, filename) 
    elif msg_text == "我想知道店鋪位置":
        slm.show_location_message(reply_token)
    else:
        stm.send_reply_message(reply_token, "unkown...")


def get_event_attr(event):
    src_user_id = getattr(event.source, 'user_id', None)
    src_group_id = getattr(event.source, 'group_id', None)
    src_type = getattr(event.source, 'type', None)
    raw_msg_text = getattr(event.message, 'text', None)
    msg_text = stm.preprocess_message(src_type, raw_msg_text)

    reply_token = getattr(event, 'reply_token', None)
    return src_user_id, src_group_id, msg_text, reply_token
