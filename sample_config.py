#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "clonebot-ui.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1802241986:AAGLVHJZmsFib7MdQF7a54IkBfYCg0Tlbek")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "6452078"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "a0dd41063f741506b67fe85704fcb81c")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BAA2Drp2OFemJdCLkNewlule37n4QNthDU_sTVUnRrQ2dO2G-0l2qtCYr5MFn1NLz-K3cVuhGsx3cvZ05SmphAzaWKjTL6v-d11jIXytMY4DDPnD8YmkJvzmcwnhzwQwOP7nktUkeagnfYGq9zIlTN1VWRIrEE65nHtcim-ZTFuHh5mB8-mTAIZxRJHzBtBnfZDh0oQy7G6YzbfzD4yzFj3AgN2MqCpYwbNZ2czrfhPBO0ny4CBnFz4hYp6cMH_ilTgzwf1Iva2d-uK0BrCV2rrANVKOOojUqZ5HLJCbS-7L_0zxiUDrOxHBt4kiJuhu-It228Lo3fzrgjCLjRe2tMoWYYvQrQA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "postgres://ufstudio:jins2010@misselvirabot.cxcgpm4dmurj.us-east-2.rds.amazonaws.com:5432/MissElviraBot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
