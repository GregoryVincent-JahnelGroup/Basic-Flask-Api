# Gregory Vincent
# gvincent@jahnelgroup.com
# 6/19/23
# Basic API in Flask
from flask import Flask, request
from flask_restful import Api, Resource
import json

app = Flask(__name__)
api = Api(app)

# creating a resource
class reqNameData(Resource):
    def get(self, name):
        with open("data.json", "r") as file:
            # Load the JSON data
            data = json.load(file)
            return data["names"][name]

    def post(self, name):
        sentData = request.get_json()
        with open("data.json", "r") as file:
            # Load the current json data
            current_json = json.load(file)
        #edit the current json ton include the sentData at the new name index
        current_json["names"][name] = sentData

        with open("data.json", "w") as file:
          # write to the file the updated contents of current_json
          json.dump(current_json,file)



api.add_resource(reqNameData, "/nameData/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)
