#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = "5852172455:AAFKcokgg2cgsAJSFAvO3tqiP6ivsqm8LLY"

    # Get from my.telegram.org
    APP_ID = 21090748

    # Get from my.telegram.org
    API_HASH = "1683713ec971f3366259f428e4aea107"

    # Authorized users to use this bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5163706369").split())

    # Generate a user session string
    TG_USER_SESSION = "BQC-84ergJSnJgRTe5IEke1Jbtrau7e0nohG6JNZ7BEaNRLGMNlqZ_ZhTRT75EpeD1zvFP5_HqD-Re3-avmoycUGsmvWULcgq43jb07kDhtzNdOgCaSAS90TMjw3qPrxle9gHhpH8e-7p9ihnLLeKnM3J_3qZ0p8Td_dz_Hwmj4x9eEEkWATZuigD2E_oMZcbqHSRhDRWj5Z5FbwetD1T7ALIu9lbgMCgFjoEPUWJn59txuftitgPqSBERIMs8ZZCOHubNjt9KWvNjIWbKTs3gBdsZ_PNoUJ6YZflBaRex0zW5tMzU1uypzOmI5jkhrfIxFLYYLPjXeh18dRazicS6sDAAAAAW8HBfYA"

    # Database URI
    DB_URI = "mongodb+srv://Cenwenex:WHx8S1A2mqgTRh29@cluster0.yffuuzl.mongodb.net/?retryWrites=true&w=majority"


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
