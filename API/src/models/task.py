import logging
from database import database
from datetime import datetime


## TODO: fetch total run time, files added and files deleted list
## TODO: exception handling
def get_all_task_detail():
    logging.info("entered get_all_task_detail")
    try:
        task_detail = database.session.query(database.TaskDetail)
        logging.info("exiting get_all_task_detail")
        return task_detail
    except Exception as e:
        logging.error(str(e))


def get_task_detail(id):
    logging.info("entered get_task_detail")
    try:
        task_detail = database.session.query(database.TaskDetail).filter(database.TaskDetail.id == id)
        logging.info("exiting get_task_detail")
        return task_detail
    except Exception as e:
        logging.error(str(e))
