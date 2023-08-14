# Listener-And-Uploader
This is python script that listen to specific folder, once a new file added , the script will upload the file to google drive and delete the file, and save file link!


# Quick Start!

1. sign in to [Google Cloud Console](https://console.cloud.google.com/).
2. Make a service account.
3. Download account's Credentials and put them in the same dirctory with the main File and put the credential's file name in the code.
4. Create a Folder in your personal Google Drive and paste the folder's id in the code.
5. Share the folder with the service account's email and put the role "Edit" to let the service account edit your folder and upload files in it.


# Make the script service in Linux

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

# Wait for updates Soon!