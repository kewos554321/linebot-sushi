from linebot.v3.messaging import MessageAction, PostbackAction, URIAction, AltUri, DatetimePickerAction

class ActionService():

    def __init__(self):
        pass

    def create_action(self, action):
        print("\naction", action)
        if action["type"] == "message":
            return self.create_message_action(action)
        if action["type"] == "postback":
            return self.create_postback_action(action)
        if action["type"] == "uri":
            return self.create_uri_action(action)
        if action["type"] == "datetimepicker": 
            return self.create_datetimepicker_action(action)

    def create_message_action(self, action):
        return MessageAction(label=action["label"], text=action["text"])
    
    def create_postback_action(self, action):
        return PostbackAction(label=action["label"], data=action["data"], display_text=action["display_text"])

    def create_uri_action(self, action):
        return URIAction(label=action["label"], uri=action["uri"], alt_uri=AltUri(desktop=action["altUri"]))

    def create_datetimepicker_action(self, action):
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
