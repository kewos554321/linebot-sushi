from flask import Flask
from config import LINE_CHANNEL_SECRET, LINE_CHANNEL_ACCESS_TOKEN
from linebot.v3 import WebhookHandler

app = Flask(__name__)
app.config.from_object('config')

handler = WebhookHandler(LINE_CHANNEL_SECRET)

from app.main import routes
