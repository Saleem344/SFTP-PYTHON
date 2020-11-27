#import library
import os
from logs import app_logs as app
from credential import push_SFTP


#clear logs
def delete_logs():
    
    logger = app('deletelogs')
    logger.info('Delete logs function execution starting')
    try:

        #local path
        path = './logs/'
        sftp_logs = sorted(list(os.listdir(path)),reverse=True)
        for item in sftp_logs:
            os.remove(path+item)
            logger.info(item+' File is removed successfully')
    except:
        logger.error('Please check your path!')
    logger.info('Delete logs function execution finished')

#delete backup files
def delete_files():
    credential = push_SFTP()
    logger = app('deletefiles')
    logger.info('Delete file function execution starting')
    try:

        #local path
        pushed_files = os.listdir(credential['local_move_path'])
        
        if(len(pushed_files)>30):
            for item in pushed_files:
                os.remove(credential['local_move_path']+item)
                logger.info(item+' File is removed successfully')
        else:
            logger.warning('Could not delete files!,because files are less than 30 days')

    except:
        logger.error('Please check your path!')
    logger.info('Delete files function execution finished')
