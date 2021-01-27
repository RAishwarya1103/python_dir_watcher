import os
from models import task
from utils import constants


def create_task_entry(config_id):
    result = task.Task.create_task_entry(config_id, constants.IN_PROGRESS)
    return result


def update_task_entry(id, status, magic_string_count, file_list):
    result = task.Task.update_task_entry(id, status, magic_string_count, file_list)
    return result


def start_task_process(magic_string, directory, config_id):
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
        return
    except ex as exception:
        
