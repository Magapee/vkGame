import logging
import datetime
import time

def logger():
    logging.basicConfig(filename="logs.log", level=logging.INFO, filemode="w")

def log(text, user_id = ""):
    print(str(time.time()) + "  " + str(text) + "   " + str(user_id))
    logging.info(datetime.datetime.now().strftime("%H:%M:%S") + "  " + str(text) + "   " + str(user_id))
