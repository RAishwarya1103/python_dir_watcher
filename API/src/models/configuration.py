import logging
from database import database
from datetime import datetime


def get_config_list():
    logging.info("entered get_config_list")
    try:
        configurations = database.session.query(database.Configuration)
        logging.info("exiting get_config_list")
        return configurations
    except Exception as e:
        logging.error(str(e))


def get_active_config():
    logging.info("entered get_active_config")
    try:
        config = database.session.query(database.Configuration).filter(database.Configuration.isActive == True)
        logging.info("exiting get_active_config")
        return config
    except Exception as e:
        logging.error(str(e))


def add_config(directory, magic_string, is_active):
    logging.info("entered add_config")
    try:
        now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        config = database.Configuration(
            directory=directory,
            magicString=magic_string,
            isActive=is_active,
            createdAt=now,
            updatedAt=now,
        )
        database.session.add(config)
        database.session.commit()
        logging.info("exiting add_config")
        return config
    except Exception as e:
        logging.error(str(e))


def update_config_status(id, is_active):
    logging.info("entered update_config_status")
    try:
        now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        config = database.session.query(database.Configuration).filter(database.Configuration.id == id).first()
        print(config)
        config.isActive = is_active
        config.updatedAt = now
        database.session.commit()
        logging.info("exiting update_config_status")
        return config
    except Exception as e:
        logging.error(str(e))
