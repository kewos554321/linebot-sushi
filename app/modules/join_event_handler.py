# from linebot.v3.messaging import Configuration, ApiClient, MessagingApi, ReplyMessageRequest, TextMessage
from linebot.v3.webhooks import JoinEvent, PostbackEvent, MessageEvent, TextMessageContent
from app import handler
from .services import text_message as stm
from .services import template_message as stpm
from .services import location_message as slm
from .utils import common as cmn

@handler.add(JoinEvent)
def handle_join(event):
    # Event source can be user, group, or room
    print("\n=>\nevent=", event)
    src_user_id, src_group_id, reply_token = cmn.get_event_attr(event)
    source_id = src_user_id if src_group_id is None else src_group_id

    stpm.show_shushi_menu(source_id)
    stm.send_reply_message(reply_token, "unkown...")