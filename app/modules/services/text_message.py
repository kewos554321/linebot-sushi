from linebot.v3.messaging import TextMessage
from .abstract_message import AbstractMessageService

class TextMessageService(AbstractMessageService):

    def __init__(self):
        super().__init__()

    def reply_text_message_with_resource(self, reply_token, filename):
        data = self.common_util.handle_json_file("text_messages", filename)
        print("\n=>\ntext-data: ", data)
        data_combined_text = ''.join(data["texts"])
        messages = []
        messages.append(TextMessage(text=data_combined_text))
        super().send_reply_message(reply_token, messages)

    def show_test_text_message(self, reply_token):
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