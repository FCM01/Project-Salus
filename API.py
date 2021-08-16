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
app.config["MONGO_URI"] = "mongodb://localhost:27017/School"

mongo  = PyMongo(app)
CORS(app)


@app.route("/Admin/Signup",metheds=["POST"])
def signup():
    status= 200
    resp ={}
    try:
        name = request.json.get("name")
        surname = request.json.get("surname")
        id_number = request.json.get("id_number")
        date_of_birth = request.json.get("date_of_birth")
        email = request.json.get("email")
        phone_number= request.json.get("phone_number")
        address= request.json.get("address")
        password = request.json.get("password")
        if name!= "" and email !="" and password !="" and   id_number  != "":
            uuid_number = tools()
            admin_number = uuid_number.id_number_genrator() 
            signup_payload = {
                "name":f"{name}",
                "surnmae":f"{surname}",
                "id_number":f"{id_number}",
                "date_of_birth": f"{date_of_birth}",
                "email":f"{email}",
                "phone_number":f"{phone_number}",
                "address":f"{address}",
                "password":f"{password}",
                "admin_number":f"{admin_number}",
                "acess_level":0,
                "token":[]
            }
            teacher  = mongo.db.teacher.insert(signup_payload)
            status = 200
            resp = {"message":"succeessful","status":f"{status}"}       
    except Exception as e:
        status = 400
        resp = {"message":"ERROR on /User/Signup","status":f"{status}",}
        print("ERROR:/User/Signup-->",e)
    return jsonify(resp),status


@app.route("/Teacher/Signup",metheds=["POST"])
def signup():
    status= 200
    resp ={}
    try:
        name = request.json.get("name")
        surname = request.json.get("surname")
        id_number = request.json.get("id_number")
        date_of_birth = request.json.get("date_of_birth")
        email = request.json.get("email")
        phone_number= request.json.get("phone_number")
        address= request.json.get("address")
        password = request.json.get("password")
        position= request .json.get("position")
        subject= request.json.get("subject")
        register_class = request.json.get("register_class")
        if name!= "" and email !="" and password !="" and   id_number  != "":
            uuid_number = tools()
            staff_number = uuid_number.id_number_genrator() 
            signup_payload = {
                "name":f"{name}",
                "surnmae":f"{surname}",
                "id_number":f"{id_number}",
                "date_of_birth": f"{date_of_birth}",
                "email":f"{email}",
                "phone_number":f"{phone_number}",
                "address":f"{address}",
                "password":f"{password}",
                "staff_number":f"{staff_number}",
                "position":f"{position}",
                "subject":f"{subject}",
                "register_class":f"{register_class}",
                "acess_level":2,
                "token":[]
            }
            teacher  = mongo.db.teacher.insert(signup_payload)
            status = 200
            resp = {"message":"succeessful","status":f"{status}"}       
    except Exception as e:
        status = 400
        resp = {"message":"ERROR on /User/Signup","status":f"{status}",}
        print("ERROR:/User/Signup-->",e)
    return jsonify(resp),status


        
@app.route("/Securtity/Signup",metheds=["POST"])
def signup():
    status= 200
    resp ={}
    try:
        name = request.json.get("name")
        surname = request.json.get("surname")
        id_number = request.json.get("id_number")
        date_of_birth = request.json.get("date_of_birth")
        email = request.json.get("email")
        phone_number= request.json.get("phone_number")
        address= request.json.get("address")
        password = request.json.get("password")
        position= request .json.get("position")
        petrol_sector = request.json.get("petrol_sector") 
        if name!= "" and email !="" and password !="" and   id_number  != "":
            uuid_number = tools()
            staff_number = uuid_number.id_number_genrator() 
            signup_payload = {
                "name":f"{name}",
                "surnmae":f"{surname}",
                "id_number":f"{id_number}",
                "date_of_birth": f"{date_of_birth}",
                "email":f"{email}",
                "phone_number":f"{phone_number}",
                "address":f"{address}",
                "password":f"{password}",
                "staff_number":f"{staff_number}",
                "position":f"{position}",
                "petrol_sector":f"{petrol_sector}",
                "acess_level":2,
                "token":[]
            }
            teacher  = mongo.db.teacher.insert(signup_payload)
            status = 200
            resp = {"message":"succeessful","status":f"{status}"}       
    except Exception as e:
        status = 400
        resp = {"message":"ERROR on /User/Signup","status":f"{status}",}
        print("ERROR:/User/Signup-->",e)
    return jsonify(resp),status


@app.route("/Domestic/Signup",metheds=["POST"])
def signup():
    status= 200
    resp ={}
    try:
        name = request.json.get("name")
        surname = request.json.get("surname")
        id_number = request.json.get("id_number")
        date_of_birth = request.json.get("date_of_birth")
        email = request.json.get("email")
        phone_number= request.json.get("phone_number")
        address= request.json.get("address")
        password = request.json.get("password")
        position= request .json.get("position")
        job_title = request.json.get("job_title") 
        if name!= "" and email !="" and password !="" and   id_number  != "":
            uuid_number = tools()
            staff_number = uuid_number.id_number_genrator() 
            signup_payload = {
                "name":f"{name}",
                "surnmae":f"{surname}",
                "id_number":f"{id_number}",
                "date_of_birth": f"{date_of_birth}",
                "email":f"{email}",
                "phone_number":f"{phone_number}",
                "address":f"{address}",
                "password":f"{password}",
                "staff_number":f"{staff_number}",
                "position":f"{position}",
                "job_title":f"{job_title}",
                "acess_level":1,
                "token":[]
            }
            teacher  = mongo.db.teacher.insert(signup_payload)
            status = 200
            resp = {"message":"succeessful","status":f"{status}"}       
    except Exception as e:
        status = 400
        resp = {"message":"ERROR on /User/Signup","status":f"{status}",}
        print("ERROR:/User/Signup-->",e)
    return jsonify(resp),status



@app.route("/Student/Signup",metheds=["POST"])
def signup():
    status= 200
    resp ={}
    try:
        name = request.json.get("name")
        surname = request.json.get("surname")
        id_number = request.json.get("id_number")
        date_of_birth = request.json.get("date_of_birth")
        email = request.json.get("email")
        phone_number= request.json.get("phone_number")
        address= request.json.get("address")
        password = request.json.get("password")
        register_class = request.json.get("register_class")
        subject_combo = request.json.get("subject_combo")
        time_table = request.jso.get("time_table")
        guardian_name  = request.json.get("guardian_name")
        guardian_surname = request.json.get("guardian_surname")
        gaurdian_email  = request.json.get(" gaurdian_email")
        gaurdian_phone_number = request.json.get("gaurdian_phone_number")
        
        if name!= "" and email !="" and password !="" and   id_number  != "":
            uuid_number = tools()
            student_number = uuid_number.id_number_genrator() 
            signup_payload = {
                "name":f"{name}",
                "surnmae":f"{surname}",
                "id_number":f"{id_number}",
                "date_of_birth": f"{date_of_birth}",
                "email":f"{email}",
                "phone_number":f"{phone_number}",
                "address":f"{address}",
                "password":f"{password}",
                "student_number":f"{student_number}",
                "register_class":f"{register_class}",
                "subject_combo":f"{subject_combo}",
                "time_table":time_table,
                "guardian_name":f"{guardian_name}",
                "guardian_surname":f"{guardian_surname}",
                "gaurdian_email":f"{gaurdian_email}",
                "gaurdian_phone_number":f"{gaurdian_phone_number}",
                "acess_level":0,
                "token":[]
            }
            teacher  = mongo.db.teacher.insert(signup_payload)
            status = 200
            resp = {"message":"succeessful","status":f"{status}"}       
    except Exception as e:
        status = 400
        resp = {"message":"ERROR on /User/Signup","status":f"{status}",}
        print("ERROR:/User/Signup-->",e)
    return jsonify(resp),status


@app.route("/Visitor/Signup",metheds=["POST"])
def signup():
    status= 200
    resp ={}
    try:
        name = request.json.get("name")
        surname = request.json.get("surname")
        id_number = request.json.get("id_number")
        date_of_birth = request.json.get("date_of_birth")
        email = request.json.get("email")
        phone_number= request.json.get("phone_number")
        address= request.json.get("address")
        password = request.json.get("password")
        purpose_of_visit= request .json.get("purpose_of_visit")
        time_in = request.json.get("time_in") 
        time_out = request.json.get("time_out") 
        if name!= "" and email !="" and password !="" and   id_number  != "":
            uuid_number = tools()
            visitor_number = uuid_number.id_number_genrator() 
            signup_payload = {
                "name":f"{name}",
                "surnmae":f"{surname}",
                "id_number":f"{id_number}",
                "date_of_birth": f"{date_of_birth}",
                "email":f"{email}",
                "phone_number":f"{phone_number}",
                "address":f"{address}",
                "password":f"{password}",
                "visitor_number":f"{visitor_number}",
                "purpose_of_visit":f"{purpose_of_visit}",
                "time_in":f"{time_in}",
                "time_out":f"{time_out}",
                "acess_level":0,
                "token":[]
            }
            teacher  = mongo.db.teacher.insert(signup_payload)
            status = 200
            resp = {"message":"succeessful","status":f"{status}"}       
    except Exception as e:
        status = 400
        resp = {"message":"ERROR on /User/Signup","status":f"{status}",}
        print("ERROR:/User/Signup-->",e)
    return jsonify(resp),status









if __name__  =="__main__":
    app.run(debug=True)