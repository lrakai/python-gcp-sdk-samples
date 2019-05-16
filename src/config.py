import os

CONFIG = {
    'client_id'      : os.environ.get('CREDENTIAL_ID'),
    'client_secret'  : os.environ.get('CREDENTIAL_KEY')
}

EVENT_CONFIG = {
    'credentials': {
        'credential_id' : CONFIG['client_id'],
        'credential_key': CONFIG['client_secret']
    }
}