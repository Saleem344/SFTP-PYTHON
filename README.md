# SFTP-PYTHON
SFTP-PYTHON is developed for pushing the files to the SFTP servers based on time schedule.
The program is developed in way once the file is pushed to the SFTP server that perticular files will be moved to the local directory 
the local directory will store the files upto 30 days then it will cleared.
It will also maintain the logs for updo 30 days to cross check the records or any issues you can see the logs in logs directory.


# Requirements:
1. Python3.6 or greather than Python3.6
2. Pysftp

# Installation Steps:
Step1: Download or clone the library <br />

`sudo git clone https://github.com/Saleem344/SFTP-PYTHON.git` <br />

Step2: Create virtual environment <br />

`Python3 -m venv venv` <br />

Step3: Activate virtual environment <br />

`source venv/bin/activate` <br />

Step4: Install requirements.txt <br />

`sudo pip install -r requirements.txt` <br />

step5: Change the credential in `credential.py` file accourding to your requirement <br />

Ex :

    result['host'] = 'sftp-energy.systems'
    result['username'] = 'Admin'
    result['private_key'] = 'C:/Program Files/TEST_SFTP/.ssh/privetkey.pem'
    result['sftp_path'] ='/srv/data/sftp-users/Admin/powerdata/'
    result['local_path'] = 'C:/SFTP_DATA/'
    result['local_move_path'] = 'C:/SFTP_DATA/SFTP_DATA_OLD/'
    
Step6: Change the timing in schedule for how many minutes you want to push the files <br />

Ex: 
      `schedule.every(1).minutes.do(sftp.data_push,'Test','writedaily')` <br />
      
Step6: To test run your program <br />

`python app.py` <br />

Step7 : Install `app.py` as startup service.

# Create Service 

# 1. Linux 
Create Service 
Step1: The file the file must have `.service` extension under `/lib/systemd/system/ directory` <br/>

`$ sudo vi /lib/systemd/system/test-py.service` <br/>
Step2: Add some contant with python full path and description <br/>

          [Unit]
          Description=Test Service
          After=multi-user.target
          Conflicts=getty@tty1.service

          [Service]
          Type=simple
          ExecStart=/usr/bin/python /home/root/test_service.py
          StandardInput=tty-force

          [Install]
          WantedBy=multi-user.target 
          
Step3: Enable Newly Added Linux Service <br/>

Reload the systemctl daemon to read new file. You need to reload this deamon each time after making any changes in in .service file.

`$ sudo systemctl daemon-reload` <br/>

Step4: Now enable and start your new service <br/>

`$ sudo systemctl enable test-py.service` <br/>

`$ sudo systemctl start test-py.service` <br/>
Step5: Start/Restart/Status of Your New Service <br/>

For service status:

`$ sudo systemctl status test-py.service`

          test-py.service - Test Service
             Loaded: loaded (/lib/systemd/system/test-py.service; enabled; vendor preset: enabled)
             Active: active (running) since Fri 2020-02-28 14:57:03 IST; 2s ago
           Main PID: 32454 (python)
              Tasks: 1 (limit: 4915)
             CGroup: /system.slice/test-py.service
                     └─32454 /usr/bin/python /home/root/redis-key-expiry.py

        Feb 28 14:57:03 websofttechs-MS-7C02 systemd[1]: Started Test Service.
Step6: Below commands to stop, start and restart your service manual. <br/> 

`$ sudo systemctl stop dummy.service`          #To stop running service  <br/> 
`$ sudo systemctl start dummy.service`         #To start running service <br/> 
`$ sudo systemctl restart dummy.service`       #To restart running service <br/> 

# 2. Windows

Step1: Configure pm2 <br/> 

`npm i -g pm2` <br/> 

Step2: Copy C:\Users\USER\.pm2 to C:\etc\.pm2 <br/> 

Step3. Set a new System Variable (not user level) name: PM2_HOME value: c:\etc\.pm2 <br/> 

Step4: Runnning your app with pm2 <br/> 

run your pm2 app. ie: `pm2 start app.py --name=SFTP_PYTHON`. <br/> 

Step5: `pm2 save` to create a dump of the current apps running. <br/> 

Step6: Testing app <br/> 

Test everything is working, try: `pm2 kill` and then `pm2 resurrect` (app should be running, check with pm2 status should be online ) <br/> 

Step7: Run at startup <br/> 

now we need to perform the resurrect command at startup, so: <br/> 

`npm install -g @innomizetech/pm2-windows-service` <br/> 

`pm2-service-install -n PM2 --unattended` <br/> 

thats it.
