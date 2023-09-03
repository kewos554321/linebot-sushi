from linebot.v3.messaging import TextMessage, QuickReply, QuickReplyItem
from linebot.v3.messaging import MessageAction, PostbackAction, URIAction, AltUri, DatetimePickerAction, CameraAction, CameraRollAction, LocationAction
from .abstract_message import AbstractMessageService

class CommonFeaturesService(AbstractMessageService):

    def __init__(self):
        super().__init__()

    def reply_text_message_with_resource(self, reply_token, filename):
        data = self.common_util.handle_json_file("text_messages", filename)
        print("\n=>\ntext-data: ", data)
        messages = []
        messages.append(TextMessage(
                        text='Quick reply',
                        quick_reply=QuickReply(
                            items=[
                                QuickReplyItem(
                                    action=PostbackAction(label="label1", data="data1")
                                ),
                                QuickReplyItem(
                                    action=MessageAction(label="label2", text="text2")
                                ),
                                QuickReplyItem(
                                    action=DatetimePickerAction(label="label3",
                                                                data="data3",
                                                                mode="date")
                                ),
                                QuickReplyItem(
                                    action=CameraAction(label="label4")
                                ),
                                QuickReplyItem(
                                    action=CameraRollAction(label="label5")
                                ),
                                QuickReplyItem(
                                    action=LocationAction(label="label6")
                                ),
                            ]
                        )))
        super().send_reply_message(reply_token, messages)

    def show_test_common_message(self, reply_token):
        filename = "test_text_message.json"
        self.reply_text_message_with_resource(reply_token, filename)

    def reply_text_message(self, reply_token, text):
        messages = []
        messages.append(TextMessage(text=text))
        super().send_reply_message(reply_token, messages)
    
    def show_unkown(self, reply_token):
        self.reply_text_message(reply_token, "unkown...")

    def preprocess_message(self, src_type, msg_text):
        if src_type == "group" and msg_text.startswith("/"):
            return msg_text[len("/ "):]
        return msg_text