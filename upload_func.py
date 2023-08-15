from service_file import service, MediaFileUpload , os


def uploader(working_dir , file_name , folder_id ):

    file_metadata = {
        'name': file_name,
        'parents' : [folder_id]
    }
    
    file_path = os.path.join(working_dir , file_name)
    media = MediaFileUpload(file_path , resumable=True)
    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id',
        uploadType='resumable'
    ).execute()
    
    #print(f'File ID: {file.get("id")}')
    
    
    """ req_body = {
        'role' : 'reader',
        'type' : 'anyone'
    }
    
    service.permissions().create(
        fileId=file.get("id"),
        body=req_body
    ).execute() """        ######### if you want your file to be public >> by defult its public if your folder is public
    
    link = service.files().get(
        fileId=file.get("id"),
        fields='webViewLink'
    ).execute()
    
    print(link['webViewLink'])
    
    return {
        'id' : file.get("id"),
        'link' : link['webViewLink'],
        'name' : file_name
    }