from linebot.v3.messaging import FlexMessage, FlexContainer
from .abstract_message import AbstractMessageService

class FlexMessageService(AbstractMessageService):

    def __init__(self):
        super().__init__()

    def reply_flex_message_with_resource(self, reply_token, filename):
        data = self.common_util.handle_json_file("flex_messages", filename)
        print("\n=>\nflex-data: ", data)
        data_contents = self.create_content(data)
        messages = []
        messages.append(
            FlexMessage(
                altText=data["altText"], 
                contents=data_contents
            )
        )
        super().send_reply_message(reply_token, messages)

    def create_content(self, data):
        json_string = self.common_util.json2string(data["contents"])
        print("\n=>\njson:", json_string)
        flex_container = FlexContainer.from_json(json_string)
        return flex_container
    
    def show_bubble_flex_message_test(self, reply_token):
        filename = "test_bubble_flex_message.json"
        self.reply_flex_message_with_resource(reply_token, filename)

    def show_carousel_flex_message_test(self, reply_token):
        filename = "test_carousel_flex_message.json"
        self.reply_flex_message_with_resource(reply_token, filename)

    def show_sushi_flex_message(self, reply_token):
        filename = "sushi_flex.json"
        self.reply_flex_message_with_resource(reply_token, filename)