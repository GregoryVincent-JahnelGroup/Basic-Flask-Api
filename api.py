# Gregory Vincent
# gvincent@Jjahnelgroup.com
# 6/19/23
# Basic API in Flask
from flask import Flask
from flask_restful import Api, Resource
import json
app = Flask(__name__)
api = Api(app)

# creating a resource
# override the REST methods you want for your specific api
class reqNameData(Resource):
   
   def get(self, name):
      with open('data.json', 'r') as file:
        # Load the JSON data
        data = json.load(file)
        return data["names"][name]
    
api.add_resource(reqNameData, "/getNameData/<string:name>")

if __name__ == "__main__":
    app.run(debug = True)  