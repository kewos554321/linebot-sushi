from linebot.v3.messaging import TemplateMessage, ImageCarouselTemplate, ImageCarouselColumn, CarouselTemplate, CarouselColumn,ButtonsTemplate, ConfirmTemplate, MessageAction, PostbackAction, URIAction, AltUri, DatetimePickerAction
from .abstract_message import AbstractMessageService
from .action import ActionService

class TemplateMessageService(AbstractMessageService):

    def __init__(self):
        super().__init__()
        self.action_service = ActionService()

    def reply_template_message_with_resource(self, reply_token, filename):
        data = self.common_util.handle_json_file("template_messages", filename)
        print("\n=>\ntemplate-data: ", data)
        messages = []
        messages.append(self.create_template_message(data))
        super().send_reply_message(reply_token, messages)
    
    def create_template_message(self, data):
        if (data["template"]["type"] == "confirm"):
            return self.create_confirm_template_message(data)
        if (data["template"]["type"] == "buttons"):
            return self.create_buttons_template_message(data)
        if (data["template"]["type"] == "carousel"):
            return self.create_carousel_template_message(data)
        if (data["template"]["type"] == "image_carousel"):
            return self.create_imagecarousel_template_message(data)
    
    def create_confirm_template_message(self, data):
        data_actions = []
        for action in data["template"]["actions"]:
            data_actions.append(self.action_service.create_action(action))
        confirm_template = ConfirmTemplate(text=data["template"]["text"], actions=data_actions)   
        template_message = TemplateMessage(alt_text=data["altText"], template=confirm_template)
        return template_message
    
    def create_buttons_template_message(self, data):
        data_default_action = self.action_service.create_action(data["template"]["defaultAction"])
        data_actions = []
        for action in data["template"]["actions"]:
            data_actions.append(self.action_service.create_action(action))
        buttons_template = ButtonsTemplate(
            thumbnail_image_url=data["template"]["thumbnailImageUrl"],
            image_aspect_ratio=data["template"]["imageAspectRatio"],
            image_size=data["template"]["imageSize"],
            image_background_color=data["template"]["imageBackgroundColor"],
            title=data["template"]["title"],
            text=data["template"]["text"],
            default_action=data_default_action,
            actions=data_actions
        )
        template_message = TemplateMessage(alt_text=data["altText"], template=buttons_template)
        return template_message
    
    def create_carousel_template_message(self, data):
        data_columns = []
        for column in data["template"]["columns"]:
            data_columns.append(self.create_carousel_column(column))
        carousel_template = CarouselTemplate(
            image_aspect_ratio=data["template"]["imageAspectRatio"],
            image_size=data["template"]["imageSize"],
            columns=data_columns
        )  
        template_message = TemplateMessage(alt_text=data["altText"], template=carousel_template)
        return template_message
    
    def create_carousel_column(self,data):
        data_default_action = self.action_service.create_action(data["defaultAction"])
        data_actions = []
        for action in data["actions"]:
            data_actions.append(self.action_service.create_action(action))
        carousel_column = CarouselColumn(
            thumbnail_image_url=data["thumbnailImageUrl"],
            image_background_color=data["imageBackgroundColor"],
            title=data["title"],
            text=data["text"],
            default_action=data_default_action,
            actions=data_actions
        )
        return carousel_column
    
    def create_imagecarousel_template_message(self, data):
        data_columns = []
        for column in data["template"]["columns"]:
            data_columns.append(self.create_imagecarousel_column(column))
        imagecarousel_template = ImageCarouselTemplate(columns=data_columns)   
        template_message = TemplateMessage(alt_text=data["altText"], template=imagecarousel_template)
        return template_message
    
    def create_imagecarousel_column(self, data):
        data_action = self.action_service.create_action(data["action"])
        imagecarousel_column = ImageCarouselColumn(image_url=data["imageUrl"], action=data_action)
        return imagecarousel_column

    def show_test_confirm_template_message(self, reply_token):
        filename = "test_confirm_template.json"
        self.reply_template_message_with_resource(reply_token, filename)

    def show_test_buttons_template_message(self, reply_token):
        filename = "test_buttons_template.json"
        self.reply_template_message_with_resource(reply_token, filename)

    def show_test_carousel_template_message(self, reply_token):
        filename = "test_carousel_template.json"
        self.reply_template_message_with_resource(reply_token, filename)

    def show_test_imagecarousel_template_message(self, reply_token):
        filename = "test_imagecarousel_template.json"
        self.reply_template_message_with_resource(reply_token, filename)

    def show_sushi_template_message(self, reply_token):
        filename = "sushi_template.json"
        self.reply_template_message_with_resource(reply_token, filename)

    def show_shushi_menu(self, reply_token):
        filename = "sushi_menu.json"
        self.reply_template_message_with_resource(reply_token, filename)

    def show_shushi_reservation_step1(self, reply_token):
        filename = "sushi_reservation_step1.json"
        self.reply_template_message_with_resource(reply_token, filename) 

