from database import database
from datetime import datetime


class Task:
    def create_task_entry(config_id, status):
        now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        task = database.TaskDetail(configId=config_id, status=status, startTime=now, createdAt=now, updatedAt=now)
        database.session.add(task)
        database.session.commit()
        return task.id

    def update_task_entry(id, status, magic_string_count, file_list):
        now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        task = database.session.query(database.TaskDetail).filter(database.TaskDetail.id == id).first()
        task.magicStringCount = magic_string_count
        task.status = status
        task.fileList = file_list
        task.updatedAt = now
        task.endTime = now
        database.session.commit()
        return task
