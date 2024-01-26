#-------------------------------------- https://github.com/m4mallu/PMChatbot ------------------------------------------#
import os
import logging

from pyrogram import Client

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

if bool(os.environ.get("ENV", False)):
    from sample_config import Config
else:
    from config import Config

if __name__ == "__main__":
    plugins = dict(root="plugins")
    bot = Client(
        "pmbot",
        bot_token="6913569473:AAE4zUbMO8VkRQgMxI7Ue8yWwP90DM_9yBQ",
        api_id="23415390",
        api_hash="893de33dd3b9df2e9f06c762d5979e9c",
        plugins=plugins
    )
    bot.run()
