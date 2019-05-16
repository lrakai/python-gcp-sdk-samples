import json
import time

from config import EVENT_CONFIG

from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

def handler(event, context):
    credentials = get_credentials(event)
    service = build('compute', 'v1', credentials=credentials)
    result = service.instances().list(project=credentials.project_id, zone='us-central1-a').execute()
    return True if 'items' in result else False

def get_credentials(event):
    service_account_info = json.loads(event['credentials']['credential_key'])
    credentials = Credentials.from_service_account_info(service_account_info)
    credentials = credentials.with_scopes(['https://www.googleapis.com/auth/cloud-platform'])
    return credentials

def timed_handler(event, context):
    start = time.time()

    result = handler(event, context)

    end = time.time()
    print(end - start)

    return result

if __name__ == "__main__":
    result = timed_handler(EVENT_CONFIG, None)
    print(result)