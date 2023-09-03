from linebot.v3.messaging import ImageMessage
from .abstract_message import AbstractMessageService

class ImageMessageService(AbstractMessageService):

    def __init__(self):
        super().__init__()

    def reply_image_message_with_resource(self, reply_token, filename):
        data = self.common_util.handle_json_file("image_messages", filename)
        print("\n=>\nimage-data: ", data)
        messages = []
        messages.append(
            ImageMessage(
                original_content_url=data["originalImageUrl"], 
                preview_image_url=data["previewImageUrl"]
            )
        )
        super().send_reply_message(reply_token, messages)

    def show_test_image_message(self, reply_token):
        filename = "test_image_message.json"
        self.reply_image_message_with_resource(reply_token, filename)

    def show_sushi_image_message(self, reply_token):
        filename = "sushi_image.json"
        self.reply_image_message_with_resource(reply_token, filename)