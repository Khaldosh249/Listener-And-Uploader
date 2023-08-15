import os 

from google.oauth2.service_account import Credentials
creds = Credentials.from_service_account_file('service_account.json') #################### Your Google Service Account Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
service = build('drive', 'v3', credentials=creds)
from googleapiclient.http import MediaFileUpload

