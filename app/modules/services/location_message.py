from linebot.v3.messaging import LocationMessage
from .abstract_message import AbstractMessageService
    
class LocationMessageService(AbstractMessageService):

    def __init__(self):
        super().__init__()

    def reply_location_message_with_resource(self, reply_token, filename):
        data = self.common_util.handle_json_file("location_messages", filename)
        print("\n=>\nlocation-data: ", data)
        messages = []
        messages.append(
            LocationMessage(
                title=data["title"],
                address=data["address"],
                latitude=data["latitude"],
                longitude=data["longitude"]
            )
        )
        super().send_reply_message(reply_token, messages)

    def show_test_location_message(self, reply_token):
        filename = "test_location_message.json"
        self.reply_location_message_with_resource(reply_token, filename)

    def show_sushi_location_message(self, reply_token):
        filename = "sushi_location.json"
        self.reply_location_message_with_resource(reply_token, filename)