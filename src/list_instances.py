import json

from config import EVENT_CONFIG

from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

def handler(event, context):
    credentials, subscription_id = get_credentials(event)
    service = build('compute', 'v1', credentials)
        
    return False

def get_service(credential_id, credential_key, scopes, api_name='compute', api_version='v1'):
    service_account_info = json.loads(credential_key)
    credentials = Credentials.from_service_account_info(service_account_info)
    #admin_credentials = credentials.create_delegated(credential_id)

def get_credentials(event):
    subscription_id = event['environment_params']['subscription_id']
    credentials = ServicePrincipalCredentials(
        client_id=event['credentials']['credential_id'],
        secret=event['credentials']['credential_key'],
        tenant=event['environment_params']['tenant']
    )
    return credentials, subscription_id

def timed_handler(event, context):
    start = time.time()

    result = handler(event, context)

    end = time.time()
    print(end - start)

    return result

if __name__ == "__main__":
    result = timed_handler(EVENT_CONFIG, None)
    print(result)