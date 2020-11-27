#import libraries
import sftp,delete
import schedule,time
from datetime import datetime
from logs import app_logs

# create logger
logger = app_logs('app')
logger.info('SFTP app program started')

# # push
schedule.every(1).minutes.do(sftp.data_push,'Oman','writedaily')

# # Delete logs
schedule.every(30).days.do(delete.delete_logs)

# # Delete backup files
schedule.every(30).days.do(delete.delete_files)


while True:
    schedule.run_pending()
    time.sleep(1)

