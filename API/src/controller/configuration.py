from flask_restful import Resource, reqparse, abort, marshal_with, fields, inputs
from flask import jsonify

from models import configuration

# Query data to be formatted to the following JSON format
config_field = {
    "id": fields.Integer,
    "directory": fields.String,
    "magicString": fields.String,
    "isActive": fields.Boolean,
    "createdAt": fields.DateTime,
    "updatedAt": fields.DateTime,
}
config_field_list = {"configs": fields.List(fields.Nested(config_field), attribute="items")}


# request input validators
config_post_args = reqparse.RequestParser()
config_post_args.add_argument("directory", type=str, help="Directory to be searced is required", required=True)
config_post_args.add_argument("magicString", type=str, help="magic string to be searched is required", required=True)
config_post_args.add_argument("isActive", type=inputs.boolean, help="isActive config is required", required=True)

config_put_args = reqparse.RequestParser()
config_put_args.add_argument("id", type=int, help="id of the config to be updated is required", required=True)
config_put_args.add_argument("isActive", type=inputs.boolean, help="isActive config is required", required=True)


class ActiveConfig(Resource):
    @marshal_with(config_field)
    def get(self):
        active_config = configuration.Configuration.get_active_config().first()
        if not active_config:
            abort(404, message="Active config is not found.")
        return active_config


class Config(Resource):
    @marshal_with(config_field_list)
    def get(self):
        configurations = configuration.Configuration.get_config_list()
        if not configurations:
            abort(404, message="Config is not found.")
        return {"items": configurations}

    def post(self):
        args = config_post_args.parse_args()
        directory = args["directory"]
        magic_string = args["magicString"]
        is_active = args["isActive"]
        result = configuration.Configuration.add_config(directory, magic_string, is_active)
        return {"message": "Config added successfully"}

    def put(self):
        args = config_put_args.parse_args()
        id = args["id"]
        is_active = args["isActive"]
        result = configuration.Configuration.update_config_status(id, is_active)
        return {"message": f"the config with id {id} is updated to {is_active}"}
