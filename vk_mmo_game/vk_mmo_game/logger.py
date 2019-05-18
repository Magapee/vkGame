import logging
import datetime

def logger():
    logging.basicConfig(filename="logs.log", level=logging.INFO, filemode="w")

def log(text, user_id = ""):
    logging.info(datetime.datetime.now().strftime("%H:%M") + "  " + str(text) + "   " + str(user_id))
