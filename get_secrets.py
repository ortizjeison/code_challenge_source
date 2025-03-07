import json
from env_manager import base_path

proxy_config_path = base_path()+'secrets/service_account_big_query'

def get_service_account():
    with open(proxy_config_path) as f:
        get_service_account = json.load(f)
    
    return get_service_account