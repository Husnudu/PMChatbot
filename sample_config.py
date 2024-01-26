#-------------------------------------- https://github.com/m4mallu/PMChatbot ------------------------------------------#
import os
from config import Config

 TG_BOT_TOKEN = "6913569473:AAE4zUbMO8VkRQgMxI7Ue8yWwP90DM_9yBQ"
class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN")
    APP_ID = int(os.environ.get("APP_ID"))
    API_HASH = os.environ.get("API_HASH")
    ADMIN = int(os.environ.get("ADMIN"))
