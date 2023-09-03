from flask import Flask
from config import DevelopmentConfig, ProductionConfig
from linebot.v3 import WebhookHandler
from linebot.v3.messaging import Configuration
import argparse


app = Flask(__name__)
app.config.from_object('config')

parser = argparse.ArgumentParser(description="Run the Flask app")
parser.add_argument("-dev", action="store_true", help="Run in development mode")

args, unknown = parser.parse_known_args()

if args.dev:
    app.config.from_object(DevelopmentConfig)
else:
    app.config.from_object(ProductionConfig)

secret = app.config['LINE_CHANNEL_SECRET']

handler = WebhookHandler(secret)
configuration = Configuration(access_token=app.config['LINE_CHANNEL_ACCESS_TOKEN'])

from app.main import routes
