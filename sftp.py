#import library
import pysftp
import os
from datetime import datetime
from credential import data
from logs import file_logs


#Push
def data_push(filename,fname):
    push = data(fname)
    #create log fil
    logger = file_logs('writedaily')
    logger.info('Write daily function execution starting')
    try:
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None
        #connection
        with pysftp.Connection(push['host'],username=push['username'],private_key=push['private_key'], port=22,cnopts=cnopts) as sftp:           
            logger.info('SFTP connection is successful')
            
            #file paths
            logger.info('Assigned local path ' +push['local_path'])
            logger.info('Assigned backup path '+push['local_move_path']+' to move files after pushed')
            logger.info('Assigned SFTP path '+push['sftp_path'])

            #files list
            sftp_files = sorted(list(sftp.listdir(push['sftp_path'])),reverse=True)
            logger.info('SFTP directory files count '+str(len(sftp_files)))

            #files list
            local_files = sorted(list(os.listdir(push['local_path'])),reverse=True)
            logger.info('Workig directory files count '+str(len(local_files)))
            
            # backup file list
            backup_files = sorted(list(os.listdir(push['local_move_path'])),reverse=True)
            logger.info('Backup directory files count '+str(len(backup_files)))

            #check file count
            if(len(local_files)>0):
                #loop for files
                for i,item in enumerate(local_files):
                     #check file is already available
                    if(i<len(sftp_files)):
                        if (item != sftp_files[i]):
                            #push file
                            sftp.put(push['local_path']+item,push['sftp_path']+item)
                            logger.info(item+' file successfully pushed to '+push['sftp_path'])                   
                        else:
                            logger.warning('Unable to push '+item+' file is already available in SFTP server directory')
                    else:
                        #push file
                        sftp.put(push['local_path']+item,push['sftp_path']+item)
                        logger.info(item+' file successfully pushed to '+push['sftp_path'])
                    
                    #check file is already available in backup 
                    if(i<len(backup_files)):
                        if (item != backup_files[i]):
                            if(os.path.isfile(push['local_move_path']+item)):
                                logger.warning('Unable to move '+item+' file is already available in local directory')
                                continue
                            else:
                                #move file to backup directory
                                os.rename(push['local_path']+item,push['local_move_path']+item)
                                logger.info(item+' is successfully moved to local directory')                   
                        else:
                            logger.warning('Unable to move '+item+' file is already available in local directory')
                    else:
                        #move file to backup directory
                        os.rename(push['local_path']+item,push['local_move_path']+item)
                        logger.info(item+' is successfully moved to local directory')
            else:
                logger.info('No files available to push')
        #close conn                
        sftp.close()
        logger.info('Connection closed')
        logger.info('SFTP program execution successfully finished')            
    except IOError:
        logger.error('IO Error while pulling data, please check remote and local paths!')
        logger.error('SFTP program execution stopped')
    except IndexError:
        logger.error('Index Error while matching files with backup files, please check file counts!')
        logger.error('SFTP program execution stopped')
    except:
        logger.error('Unable to connect to SFTP server,please check the device connection status')
        logger.error('SFTP program execution stopped')
    logger.info('Write daily function execution finished')
