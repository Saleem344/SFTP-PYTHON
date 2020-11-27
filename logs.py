#import library
import os
import logging,logging.handlers
from datetime import datetime

#app logs
def app_logs(logggername):

    #create log file
    log_file = './logs/app.log'

    #create logger console
    logger = logging.getLogger(logggername)
    if not logger.hasHandlers():
        logger.setLevel(logging.DEBUG)

        # create console handler and set level to debug
        handler = logging.handlers.RotatingFileHandler(filename=log_file,maxBytes=12000000,backupCount=10)

        # create formatter
        formatter = logging.Formatter("%(asctime)s - %(name)s  - %(levelname)s - %(message)s","%Y-%m-%d %H:%M:%S")
        handler.setFormatter(formatter)
        
        #add handler
        logger.addHandler(handler)

    return logger

#file logs
def file_logs(logggername):

    #create log file
    log_file = './logs/SFTP_'+datetime.now().strftime('%Y%m%d')+'.log'

    #create logger console
    logger = logging.getLogger(logggername)
    if not logger.hasHandlers():
        logger.setLevel(logging.DEBUG)

        # create console handler and set level to debug
        handler = logging.handlers.RotatingFileHandler(filename=log_file,maxBytes=12000000,backupCount=10)

        # create formatter
        formatter = logging.Formatter("%(asctime)s - %(name)s  - %(levelname)s - %(message)s","%Y-%m-%d %H:%M:%S")
        handler.setFormatter(formatter)

        #add handler
        logger.addHandler(handler)

    return logger



