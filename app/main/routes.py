from flask import request, abort
from app import app, handler
from linebot.v3.exceptions import InvalidSignatureError
from app.modules.message_event_handler import handle_message
from app.modules.postback_event_handler import handle_postback
from app.modules.join_event_handler import handle_join

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'
