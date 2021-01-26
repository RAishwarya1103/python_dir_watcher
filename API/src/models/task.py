from database import database
from datetime import datetime


class Task:
    def __init__(self):
        pass

    ## TODO: fetch total run time, files added and files deleted list
    ## TODO: exception handling
    ## TODO: logging

    def get_all_task_detail():
        task_detail = database.session.query(database.TaskDetail)
        return task_detail

    def get_task_detail(id):
        task_detail = database.session.query(database.TaskDetail).filter(database.TaskDetail.id == id)
        return task_detail
