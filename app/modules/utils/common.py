import json
import os
from ..services import text_message as stm
static_url = "./app/static"

# def handle_text_file():

#     with open(static_url + ) as file:
class CommonUtil():

    def __init__(self):
        pass
    
    def handle_json_file(self, file_url, file_name):
        # file_url = ""
        # file_name = "test.json"
        # current_directory = os.getcwd()
        # print(current_directory)
        print("\n=>\nfile loaction: ", static_url + "/" + file_url + "/" + file_name, "\n")
        with open(static_url + "/" + file_url + "/" + file_name, encoding='utf-8') as file:
            return json.load(file)

    def get_event_attr(self, event):
        src_user_id = getattr(event.source, 'user_id', None)
        src_group_id = getattr(event.source, 'group_id', None)
        src_type = getattr(event.source, 'type', None)
        reply_token = getattr(event, 'reply_token', None)

        if (event.type == "join"):
            return src_user_id, src_group_id, reply_token
        if (event.type == "message"):
            raw_msg_text = getattr(event.message, 'text', None)
            msg_text = stm.preprocess_message(src_type, raw_msg_text)
            return src_user_id, src_group_id, msg_text, reply_token

    def json2string(self, data):
        json_string = json.dumps(data)
        return json_string
