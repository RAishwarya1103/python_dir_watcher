from database import database
from datetime import datetime


class Configuration:
    def __init__(self):
        pass

    def get_config_list():
        configurations = database.session.query(database.Configuration)
        return configurations

    def get_active_config():
        config = database.session.query(database.Configuration).filter(database.Configuration.isActive == True)
        return config

    def add_config(directory, magic_string, is_active):
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
        return config

    def update_config_status(id, is_active):
        now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        config = database.session.query(database.Configuration).filter(database.Configuration.id == id).first()
        print(config)
        config.isActive = is_active
        config.updatedAt = now
        database.session.commit()
        return config
