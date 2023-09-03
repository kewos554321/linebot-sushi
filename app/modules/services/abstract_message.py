from abc import ABC, abstractclassmethod
from linebot.v3.messaging import ApiClient, MessagingApi, ReplyMessageRequest, TextMessage
from app import configuration
from ..utils.common import CommonUtil
class AbstractMessageService(ABC):

    def __init__(self):
        super().__init__()
        self.common_util = CommonUtil()


    def do():
        pass

    def send_reply_message(self, reply_token, messages):
        with ApiClient(configuration) as api_client:
            line_bot_api = MessagingApi(api_client)
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=reply_token,
                    messages=messages
                )
            )    