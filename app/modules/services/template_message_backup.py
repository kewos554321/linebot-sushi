from app import app
from linebot import LineBotApi
from linebot.models import (
    TemplateSendMessage, ButtonsTemplate, CarouselTemplate, CarouselColumn, ConfirmTemplate, ImageCarouselTemplate, ImageCarouselColumn, MessageAction, PostbackAction, URIAction, DatetimePickerAction
)
from ..utils import common as cmn

def create_message_action(action):
    return MessageAction(label=action["label"], text=action["text"])

def create_postback_action(action):
    return PostbackAction(label=action["label"], data=action["data"], display_text=action["display_text"])

def create_uri_action(action):
    return URIAction(label=action["label"], uri=action["uri"], altUri=action["altUri"])

def create_datetimepicker_action(action):
    initial_datetime, min_datetime, max_datetime = get_datetime()
    return DatetimePickerAction(label=action["label"], mode=action["mode"], initial=initial_datetime, max=max_datetime, min=min_datetime, data=action["data"])

import datetime
def get_datetime():
    now = datetime.datetime.now()
    initial_datetime = now.strftime('%Y-%m-%dT%H:%M')
    min_datetime = initial_datetime
    one_month_later = now + datetime.timedelta(days=30)
    max_datetime = one_month_later.strftime('%Y-%m-%dT%H:%M')
    return initial_datetime, min_datetime, max_datetime

def create_action(action):
    print("\naction", action)
    if action["type"] == "message":
        return create_message_action(action)
    if action["type"] == "postback":
        return create_postback_action(action)
    if action["type"] == "uri":
        return create_uri_action(action)
    if action["type"] == "datetimepicker": 
        return create_datetimepicker_action(action)
    
def create_buttons_template_message(data):
    data_default_action = create_action(data["template"]["defaultAction"])
    data_actions = []
    for action in data["template"]["actions"]:
        data_actions.append(create_action(action))
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
    template_message = TemplateSendMessage(alt_text=data["altText"], template=buttons_template)
    return template_message

def create_buttons_template(source_id, filename):
    line_bot_api = LineBotApi(app.config['LINE_CHANNEL_ACCESS_TOKEN'])
    data = cmn.handle_json_file("template_messages", filename)
    print("\n=>\nbuttons-data: ", data)
    buttons_template_message = create_buttons_template_message(data)
    line_bot_api.push_message(source_id, buttons_template_message)

def create_carousel_template_message(data):
    data_columns = []
    for column in data["template"]["columns"]:
        data_columns.append(create_carousel_column(column))
    carousel_template = CarouselTemplate(
        image_aspect_ratio=data["template"]["imageAspectRatio"],
        image_size=data["template"]["imageSize"],
        columns=data_columns
    )   
    template_message = TemplateSendMessage(alt_text=data["altText"], template=carousel_template)
    return template_message

def create_carousel_column(data):
    data_default_action = create_action(data["defaultAction"])
    data_actions = []
    for action in data["actions"]:
        data_actions.append(create_action(action))
    carousel_column = CarouselColumn(
        thumbnail_image_url=data["thumbnailImageUrl"],
        image_background_color=data["imageBackgroundColor"],
        title=data["title"],
        text=data["text"],
        default_action=data_default_action,
        actions=data_actions
    )
    return carousel_column

def create_carousel_template(source_id, filename):
    line_bot_api = LineBotApi(app.config['LINE_CHANNEL_ACCESS_TOKEN'])
    data = cmn.handle_json_file("template_messages", filename)
    print("\n=>\ncarousel-data: ", data)
    carousel_template_message = create_carousel_template_message(data)
    line_bot_api.push_message(source_id, carousel_template_message)

def create_confirm_template_message(data):
    data_actions = []
    for action in data["template"]["actions"]:
        data_actions.append(create_action(action))
    confirm_template = ConfirmTemplate(text=data["template"]["text"], actions=data_actions)   
    template_message = TemplateSendMessage(alt_text=data["altText"], template=confirm_template)
    return template_message

def create_confirm_template(source_id, filename):
    line_bot_api = LineBotApi(app.config['LINE_CHANNEL_ACCESS_TOKEN'])
    data = cmn.handle_json_file("template_messages", filename)
    print("\n=>\nconfirm-data: ", data)
    confirm_template_message = create_confirm_template_message(data)
    line_bot_api.push_message(source_id, confirm_template_message)

def create_imagecarousel_template_message(data):
    data_columns = []
    for column in data["template"]["columns"]:
        data_columns.append(create_imagecarousel_column(column))
    imagecarousel_template = ImageCarouselTemplate(columns=data_columns)   
    template_message = TemplateSendMessage(alt_text=data["altText"], template=imagecarousel_template)
    return template_message

def create_imagecarousel_column(data):
    data_action = create_action(data["action"])
    imagecarousel_column = ImageCarouselColumn(image_url=data["imageUrl"], action=data_action)
    return imagecarousel_column

def create_imagecarousel_template(source_id, filename):
    line_bot_api = LineBotApi(app.config['LINE_CHANNEL_ACCESS_TOKEN'])
    data = cmn.handle_json_file("template_messages", filename)
    print("\n=>\nimagecarousel-data: ", data)
    imagecarousel_template_message = create_imagecarousel_template_message(data)
    line_bot_api.push_message(source_id, imagecarousel_template_message)


def show_shushi_menu(source_id):
    filename = "sushi_menu.json"
    create_buttons_template(source_id, filename)

def show_shushi_reservation_step1(source_id):
    filename = "sushi_reservation_step1.json"
    create_buttons_template(source_id, filename) 

def show_carousel_test(source_id):
    filename = "test_carousel_template.json"
    create_carousel_template(source_id, filename)

def show_confirm_test(source_id):
    filename = "test_confirm_template.json"
    create_confirm_template(source_id, filename)

def show_imagecarousel_test(source_id):
    filename = "test_imagecarousel_template.json"
    create_imagecarousel_template(source_id, filename)