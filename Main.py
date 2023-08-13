import os

from google.oauth2.service_account import Credentials
creds = Credentials.from_service_account_file('service_account.json') #################### Your Google Service Account Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
service = build('drive', 'v3', credentials=creds)
from googleapiclient.http import MediaFileUpload

fold_id = ''                         #################### Google Drive Folder

path_to_watch = "./listener"                                          #################### edit to your listener path
#print(f'Your folder path is {path_to_watch}')

links_save_to_file_path = "../links.txt"                              #################### edit file name and path >> file will contain links and id




before = []

while 1:
        after = os.listdir (path_to_watch)
        added = [f for f in after if not f in before]
        if added:
            for x in added:
                file_name = x
                file_metadata = {
                    'name': file_name,
                    'parents' : [fold_id]
                }
                
                file_path = os.path.join(path_to_watch , file_name)
                media = MediaFileUpload(file_path)
                file = service.files().create(
                    body=file_metadata,
                    media_body=media,
                    fields='id'
                ).execute()
                
                #print(f'File ID: {file.get("id")}')
                
                
                """ req_body = {
                    'role' : 'reader',
                    'type' : 'anyone'
                }
                
                service.permissions().create(
                    fileId=file.get("id"),
                    body=req_body
                ).execute() """            ######### if you want your file to be public >> by defult its public if your folder is public
                
                link = service.files().get(
                    fileId=file.get("id"),
                    fields='webViewLink'
                ).execute()
                
                #print(link['webViewLink'])
                
                file_object = open(links_save_to_file_path, 'a')
                file_object.write(f"""
###############################################################################################
Added New File with ID {file.get("id")}
############################################################################################### File Name: {file_name}
Download Link: {link['webViewLink']}
###############################################################################################
\n\n """)
                file_object.close()
                os.remove(file_path)
                
                
        else:
            pass