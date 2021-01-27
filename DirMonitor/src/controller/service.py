import requests
import logging

from config import get_config_URL


def get_config_detail():
    logging.info("entered get_config_detail")
    try:
        response = requests.get(get_config_URL)
        logging.info("exiting get_config_detail")
        return response.json()
    except Exception as e:
        logging.error(str(e))
