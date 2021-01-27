import logging
from flask_restful import Resource, reqparse, abort, marshal_with, fields, inputs
from flask import jsonify

from models import task


# Query data to be formatted to the following JSON format
task_detail_field = {
    "id": fields.Integer,
    "startTime": fields.DateTime,
    "endTime": fields.DateTime,
    "status": fields.String,
    "configId": fields.Integer,
    "magicStringCount": fields.Integer,
    "fileList": fields.String,
    "createdAt": fields.DateTime,
    "updatedAt": fields.DateTime,
}
task_detail_field_list = {"task_detail": fields.List(fields.Nested(task_detail_field), attribute="items")}


class TaskDetail(Resource):
    @marshal_with(task_detail_field)
    def get(self, id):
        logging.info("entered GET of TaskDetail")
        try:
            task_detail = task.get_task_detail(id).first()
            if not task_detail:
                abort(404, message=f"Task detail for the id {id} is not found.")
            logging.info("exiting GET of TaskDetail")
            return task_detail
        except Exception as e:
            logging.error(str(e))


class TaskDetails(Resource):
    @marshal_with(task_detail_field_list)
    def get(self):
        logging.info("entered GET of TaskDetails")
        try:
            task_details = task.get_all_task_detail()
            if not task_details:
                abort(404, message="task details are not found.")
            logging.info("exiting GET of TaskDetails")
            return {"items": task_details}
        except Exception as e:
            logging.error(e)
