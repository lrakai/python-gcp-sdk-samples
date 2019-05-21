from config import EVENT_CONFIG
from credentials import credential_helper
from timed_handler import timed_handler

from googleapiclient.discovery import build

def handler(event, context):
    credentials = credential_helper.get_credentials(event)
    project_id = event['environment_params']['project_id']
    
    service = build('compute', 'v1', credentials=credentials)
    result = service.instances().list(project=project_id, zone='us-central1-a').execute()
    return True if 'items' in result else False

if __name__ == "__main__":
    result = timed_handler.time_handler(handler, EVENT_CONFIG, None)
    print(result)