import json
import time

from config import EVENT_CONFIG

from googleapiclient.discovery import build
from credentials import credential_helper

def handler(event, context):
    credentials = credential_helper.get_credentials(event)
    service = build('compute', 'v1', credentials=credentials)
    result = service.instances().list(project=credentials.project_id, zone='us-central1-a').execute()
    return True if 'items' in result else False

def timed_handler(event, context):
    start = time.time()

    result = handler(event, context)

    end = time.time()
    print(end - start)

    return result

if __name__ == "__main__":
    result = timed_handler(EVENT_CONFIG, None)
    print(result)