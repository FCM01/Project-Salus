from flask import Flask, request, json, jsonify,render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson.json_util import dumps
from bson import json_util
from flask_cors import CORS
import json

from microfunction import tools


def parse_json(data):
    return json.loads(json_util.dumps(data))


app=Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/"

mongo  = PyMongo(app)
CORS(app)


@app.route("/User/Signup",metheds=["POST"])
def signup():
    status= 200
    resp ={}
    try:
        username = request.json.get("username")
        email = request.json.get("email")
        password = request.json.get("password")
        user_type= request.json.get("user_type")
        if username!= "" and email !="" and password !="" and user_type != "":
            signup_payload = {
                "username":f"{username}",
                "email":f"{email}",
                "pasword":f"{password}",
                "user_type":f"{user_type}"
            }


        
    except Exception as e:
        status = 400
        resp = {"message":"ERROR on /User/Signup","status":f"{status}",}
        print("ERROR:/User/Signup-->",e)

        






















if __name__  =="__main__":
    app.run(debug=True)