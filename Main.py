import os
from upload_func import uploader





folder_id = ''                                                        #################### Google Drive Folder
path_to_watch = "./listener"                                          #################### edit to the path you want to listen

#print(f'Your folder path is {path_to_watch}')


links_save_to_file_path = "./links.txt"                              #################### edit file name and path >> file will contain links and id
folder_to_keep_uploaded = './Uploaded'                               #################### after uploading the script will move the uploaded file to this folder. MAKE SURE TO CREATE IT


before = []

while 1:
        after = os.listdir(path_to_watch)
        added = [f for f in after if not f in before]
        if added:
            for x in added:
                
                response = uploader( path_to_watch , file_name=x , folder_id=folder_id )
                
                file_object = open(links_save_to_file_path, 'a')
                file_object.write(f"""
###############################################################################################
Added New File with ID {response["id"]}
############################################################################################### File Name: {response['name']}
Download Link: {response['link']}
###############################################################################################
\n\n """)
                file_object.close()
                os.rename( os.path.join(path_to_watch,x) , os.path.join(folder_to_keep_uploaded,x) )
                #os.remove(file_path)
                
                
        else:
            pass



