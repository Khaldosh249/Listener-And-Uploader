# Listener-And-Uploader
This is python script that listen to specific folder, once a new file added , the script will upload the file to google drive and delete the file, and save file link!


# To Edit before start

1. Paste service account credentials file name in service_file here.
2. Paste your Google Drive Folder here.
3. Edit to the path you want to listen here.
4. Edit and create the folder that will save the uploaded files here.
5. Install all libraries.


# Quick Start!

1. Sign in to [Google Cloud Console](https://console.cloud.google.com/).
2. Enable Google Drive API.
3. Create a service account.
4. Download account Credentials file and paste it in the same directory with the main File and put the credentials file name in the code.
5. Create a Folder in your personal Google Drive and paste the folder's id in the code.
Folder id is in the folder's link
`https://drive.google.com/drive/folders/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
6. Share the folder with the service account's email and make the role "Edit" to let the service account edit your folder and upload files in it.
7. Feel free to search about how to create service account in Youtube.


# Make the script service in Linux

run this script to create service file
`sudo vi /etc/systemd/system/YOUR_SERVICE_NAME.service`

the edit and paste following code
```
[Unit]
Description=Google Drive Uploader
After=network.target
[Service]
Type=simple
Restart=always
ExecStart=/usr/bin/python3 /home/your_username/your_path_to_main.py
[Install]
WantedBy=multi-user.target
```

run
`systemctl enable YOUR_SERVICE_NAME`

run 
`systemctl daemon-reload`
to reload services

then
`systemctl start YOUR_SERVICE_NAME`
to start your service



# Wait for updates Soon!