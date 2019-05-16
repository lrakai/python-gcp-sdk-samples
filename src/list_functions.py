from config import EVENT_CONFIG
from credentials import credential_helper
from timed_handler import timed_handler

from googleapiclient.discovery import build

def handler(event, context):
    credentials = credential_helper.get_credentials(event)
    service = build('cloudfunctions', 'v1', credentials=credentials)
    result = service.projects().locations().functions().list(parent='projects/'+credentials.project_id+'/locations/-').execute()
    return True if 'functions' in result and len(result['functions']) >= 1 else False

if __name__ == "__main__":
    result = timed_handler.time_handler(handler, EVENT_CONFIG, None)
    print(result)