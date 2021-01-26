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
        task_detail = task.Task.get_task_detail(id).first()
        if not task_detail:
            abort(404, message=f"Task detail for the id {id} is not found.")
        return task_detail


class TaskDetails(Resource):
    @marshal_with(task_detail_field_list)
    def get(self):
        task_details = task.Task.get_all_task_detail()
        if not task_details:
            abort(404, message="task details are not found.")
        return {"items": task_details}
