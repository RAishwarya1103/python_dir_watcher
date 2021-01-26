from flask import Flask
from flask_restful import Api

from controller import configuration, task


app = Flask(__name__)

api = Api(app)
api.add_resource(configuration.ActiveConfig, "/activeConfig")
api.add_resource(configuration.Config, "/config")
api.add_resource(task.TaskDetail, "/taskDetail/<int:id>")
api.add_resource(task.TaskDetails, "/taskDetails")
