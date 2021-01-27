import requests

from config import get_config_URL


def get_config_detail():
    try:
        response = requests.get(get_config_URL)
        return response.json()
    except:
        pass
