
def push_SFTP():
    result = {}
    result['host'] = 'sftp-sterling-wilson.energymeteo.systems'
    result['username'] = 'sterling-wilson2'
    result['private_key'] = 'C:/Program Files/ARMAX_SFTP/.ssh/privetkey.pem'
    result['sftp_path'] ='/srv/data/sftp-users/sterling-wilson2/powerdata/Oman/'
    result['local_path'] = 'C:/SFTP_DATA/'
    result['local_move_path'] = 'C:/SFTP_DATA/SFTP_DATA_OLD/'
    return result

def data(fname):
    if fname == 'writedaily':
        result = push_SFTP()
    return result