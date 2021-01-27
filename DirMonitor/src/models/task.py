import logging
from database import database
from datetime import datetime


def create_task_entry(config_id, status):
    logging.info("entered create_task_entry")
    try:
        now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        task = database.TaskDetail(configId=config_id, status=status, startTime=now, createdAt=now, updatedAt=now)
        database.session.add(task)
        database.session.commit()
        logging.info("exiting create_task_entry")
        return task.id
    except Exception as e
        logging.error(str(e))



def update_task_entry(id, status, magic_string_count, file_list):
    logging.info("entered update_task_entry")
    try:
        now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        task = database.session.query(database.TaskDetail).filter(database.TaskDetail.id == id).first()
        task.magicStringCount = magic_string_count
        task.status = status
        task.fileList = file_list
        task.updatedAt = now
        task.endTime = now
        database.session.commit()
        logging.info("exiting update_task_entry")
        return task
    except Exception as e
        logging.error(str(e))

