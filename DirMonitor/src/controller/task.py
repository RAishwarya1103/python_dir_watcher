import os
import logging
from models import task
from utils import constants


def create_task_entry(config_id):
    logging.info("entered create_task_entry")
    try:
        result = task.create_task_entry(config_id, constants.IN_PROGRESS)
        logging.info("exiting create_task_entry")
        return result
    except Exception as e:
        logging.error(str(e))


def update_task_entry(id, status, magic_string_count, file_list):
    logging.info("entered update_task_entry")
    try:
        result = task.update_task_entry(id, status, magic_string_count, file_list)
        logging.info("exiting update_task_entry")
        return result
    except Exception as e:
        logging.error(str(e))


def start_task_process(magic_string, directory, config_id):
    logging.info("entered start_task_process")
    try:
        task_id = create_task_entry(config_id)
        occurance_count = 0
        file_list = []
        with os.scandir(directory) as folder:
            for entry in folder:
                if os.path.isfile(entry):
                    file_list.append(entry.name)
                    with open(entry, "r") as searchfile:
                        data = searchfile.read()
                        occurance_count = occurance_count + data.count(magic_string)
        update_task_entry(task_id, constants.SUCCESS, occurance_count, " ".join(file_list))
        logging.info("exiting start_task_process")
        return "processed"
    except Exception as e:
        logging.error(str(e))
