import logging
import datetime

def logger():
    logging.basicConfig(filename="logs.log", level=logging.INFO, filemode="w")

def log(text, user_id = ""):
    outs = datetime.datetime.now().strftime("%H:%M:%S:%f") + "  " + str(text) + "   " + str(user_id)
    print(outs)
    logging.info(outs)
