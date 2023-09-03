from linebot.v3.webhooks import MessageEvent, TextMessageContent, StickerMessageContent
from app import handler
from .services.text_message import TextMessageService
from .services.template_message import TemplateMessageService
from .services.location_message import LocationMessageService
from .services.image_message import ImageMessageService
from .services.sticker_message import StickerMessageService
from .services.flex_message import FlexMessageService
from .services.common_features import CommonFeaturesService
from .utils import common as cmn

@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    sms, lms, tms, tpms, ims, fms, cfs = create_all_service()
    print("\nevent=", event)
    src_user_id, src_group_id, msg_text, reply_token = get_event_attr(event, tms)
    source_id = src_user_id if src_group_id is None else src_group_id
    if msg_text == "h": 
        filename = "help.json"
        sms.show_test_sticker_message(reply_token)
        # stm.send_reply_message_with_resource(reply_token, filename)
    elif msg_text == "sm":
        sms.show_test_sticker_message(reply_token)
    elif msg_text == "t":
        tpms.show_test_confirm_template_message(reply_token)
    elif msg_text == "r":
        tpms.show_test_buttons_template_message(reply_token)
    elif msg_text == "e":
        tpms.show_test_carousel_template_message(reply_token)
    elif msg_text == "w":
        tpms.show_test_imagecarousel_template_message(reply_token)
    elif msg_text == "q":
        ims.show_sushi_image_message(reply_token)
    elif msg_text == "y":
        fms.show_carousel_flex_message_test(reply_token)
    elif msg_text == "u":
        cfs.show_test_common_message(reply_token)
    elif msg_text == "menu":
        tpms.show_shushi_menu(reply_token)
    elif msg_text == "我想要訂位預約":
        tpms.show_shushi_reservation_step1(reply_token)
    elif msg_text == "我想看今日特餐":
        tms.show_test_text_message(reply_token) 
    elif msg_text == "我想看菜單":
        tms.show_test_text_message(reply_token) 
    elif msg_text == "我想知道店鋪位置":
        lms.show_test_location_message(reply_token)
    else:
        tms.show_unkown(reply_token)

def create_all_service():
    lms = LocationMessageService()
    sms = StickerMessageService()
    tms = TextMessageService()
    tpms = TemplateMessageService()
    ims = ImageMessageService()
    fms = FlexMessageService()
    cfs = CommonFeaturesService()
    return sms, lms, tms, tpms, ims, fms, cfs

def get_event_attr(event, tms):
    src_user_id = getattr(event.source, 'user_id', None)
    src_group_id = getattr(event.source, 'group_id', None)
    src_type = getattr(event.source, 'type', None)
    raw_msg_text = getattr(event.message, 'text', None)
    msg_text = tms.preprocess_message(src_type, raw_msg_text)

    reply_token = getattr(event, 'reply_token', None)
    return src_user_id, src_group_id, msg_text, reply_token
