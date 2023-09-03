from linebot.v3.messaging import StickerMessage
from .abstract_message import AbstractMessageService

class StickerMessageService(AbstractMessageService):

    def __init__(self):
        super().__init__()

    def reply_sticker_message_with_resource(self, reply_token, filename):
        data = self.common_util.handle_json_file("sticker_messages", filename)
        print("\n=>\nsticker-data: ", data)
        messages = []
        messages.append(
            StickerMessage(
                package_id=data["packageId"],
                sticker_id=data["stickerId"]
            )
        )
        super().send_reply_message(reply_token, messages)

    def show_test_sticker_message(self, reply_token):
        filename = "test_sticker_message.json"
        self.reply_sticker_message_with_resource(reply_token, filename)