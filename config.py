
import os
import logging
from logging.handlers import RotatingFileHandler


# Get a bot token from botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1474138123:AAFvvAz62r-Rc7B2add1Y6fwwgxJGUL_pa4")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("APP_ID", "1813445"))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("API_HASH", "8f45dabd56be5ad1619df16af9eca560")

# Generate a user session string 
TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQBImQwNKi7sah7jXUvXUrwM3bYktU0Qw2DeBSNxwYuDXjTJUIJOBEpJKtZ6TnpJp6rk3SVKJtbsgFIVinrcXgeN68ixk2LGA1GxFv_tO8OjC8668XqgOF0QAW-uvQeC4DghoIhN-Oh_S97iezfkNUAv9Uzv_nOpYNCwioJ0plARRLpvkZm5eAC3IGti9i3efvkCCKL30-U_GAuovVum8s6-4csnvMStIHYeiC69jsOQIjDdIaPvfIAAWDXG4vtJlZaZkfhi6M1BACNtlu0-NssFe3kZ8LYuQTrId0NXbxCOF5jvkoGL3bnkP_Me3FWGb5cWCE66JeiJU4Xx9p9yVGZLU2K9uQA")

# ID of Channel from which the bot shoul search files
MAINCHANNEL_ID = os.environ.get("MAINCHANNEL_ID", "-1001341487697")




TG_BOT_SESSION = os.environ.get("TG_BOT_SESSION", "bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
LOG_FILE_NAME = "filterbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
