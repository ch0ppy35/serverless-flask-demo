from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class SayHi(Resource):
    def get(self):
        return {"message": "Hi stranger"}

    def post(self):
        json_data = request.get_json()
        name = json_data["name"]
        return {"message": "Hi " + name}


api.add_resource(SayHi, "/hi")
