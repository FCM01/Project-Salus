from flask import Flask, request, json, jsonify,render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson.json_util import dumps
from bson import json_util
from flask_cors import CORS
import json

import gridfs
from pymongo import MongoClient
from microfunction import tools


def parse_json(data):
    return json.loads(json_util.dumps(data))


app=Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/School"

mongo  = PyMongo(app)
CORS(app)

def mongo_conn():
    try:
        conn = MongoClient(host ="127.0.0.1",port =27017)
        print("Mongo Connected",conn)
        return conn.grid_file
    except Exception  as e :
        print(e)

#signup routes ////
@app.route("/Admin/Signup",methods=["POST"])
def a_signup():
    status= 200
    resp ={}
    image_path = ""
    try:
        data =request.get_json("data")
        name = data["data"]["name"]
        surname = data["data"]["surname"]
        id_number = data["data"]["id_number"]
        date_of_birth = data["data"]["date_of_birth"]
        email = data["data"]["email"]
        phone_number= data["data"]["phone_number"]
        address= data["data"]["address"]
        city= data["data"]["city"]
        pcode= data["data"]["pcode"]
        password = data["data"]["password"]
        admin_number = data["data"]["admin_number"]
        email_data = mongo.db.admin.find({"email":f"{email}"})
        if email_data == []:

            if name!= "" and email !="" and password !="" and   id_number  != "": 
                qr = tools()
                token = qr.generate_token(data,admin_number,"admin")
                signup_payload = {
                    "name":f"{name}",
                    "surname":f"{surname}",
                    "id_number":f"{id_number}",
                    "date_of_birth": f"{date_of_birth}",
                    "email":f"{email}",
                    "phone_number":f"{phone_number}",
                    "address":f"{address}",
                    "city":f"{city}",
                    "pcode":f"{pcode}",
                    "password":f"{password}",
                    "admin_number":f"{admin_number}",
                    "acess_level":0,
                    "pqr":token
                }
                mongo.db.admin.insert_one(signup_payload)
                mongo.db.teacher.insert_one(signup_payload)
                mongo.db.security.insert_one(signup_payload)
                q1= tools()
                q1.emailing_services(email,name,admin_number,"signup",image_path,"","","")
                status = 200
                resp = {"message":"succeessful","status":f"{status}"}  
            else:
                status = 200
                resp = {"message":"Email is already in use","status":f"{status}"}  

    except Exception as e:
        status = 400
        resp = {"message":"ERROR on /Admin/Signup","status":f"{status}",}
        print("ERROR:/Admin/Signup-->",e)
    return jsonify(resp),status
    
@app.route("/Purge/QR/Codes",methods= ["POST"])
def delete_qr_codes():
    status = 200
    resp ={}
    try:
        data = request.get_json("data")
        command = data["data"]["command"]
        print(command)
        if command != "":
            if command =="purge":
                com = tools()
                response = com.purge_qr_codes()
                if response == 1:
                    status = 200
                    resp ={"message":"successful","stutus":status}
                elif response == 0:
                    status = 400
                    resp ={"message":"fail","stutus":status}
    except Exception as e :
        status = 400
        resp = {"message":"ERROR on /Admin/Signup","status":f"{status}",}
        print("ERROR:/Admin/Signup-->",e)
    return jsonify(resp),status



@app.route("/Teacher/Signup",methods=["POST"])
def t_signup():
    status= 200
    resp ={}
    try:
        data = request.get_json("data")
        name = data["data"]["name"]
        surname = data["data"]["surname"]
        id_number = data["data"]["id_number"]
        date_of_birth = data["data"]["date_of_birth"]
        email = data["data"]["email"]
        phone_number= data["data"]["phone_number"]
        address= data["data"]["address"]
        city= data["data"]["city"]
        pcode= data["data"]["pcode"]
        password = data["data"]["password"]
        staff_number = data["data"]["staff_number"]
        position= data["data"]["position"]
        subject= data["data"]["subject"]
        register_class = data["data"]["register_class"]

        email_data = mongo.db.admin.find({"email":f"{email}"})
        if email_data == []:
            if name!= "" and email !="" and password !="" and   id_number  != "":
                qr = tools()
                token = qr.generate_token(name,staff_number,"teacher")
                signup_payload = {
                    "name":f"{name}",
                    "surname":f"{surname}",
                    "id_number":f"{id_number}",
                    "date_of_birth": f"{date_of_birth}",
                    "email":f"{email}",
                    "phone_number":f"{phone_number}",
                    "address":f"{address}",
                    "city":f"{city}",
                    "pcode":f"{pcode}",
                    "password":f"{password}",
                    "staff_number":f"{staff_number}",
                    "position":f"{position}",
                    "subject":f"{subject}",
                    "register_class":f"{register_class}",
                    "acess_level":2,
                    "pqr":token
                }
                teacher  = mongo.db.teacher.insert_one(signup_payload)
                q1= tools()
                q1.emailing_services(email,name,staff_number,"signup","","","","")
                status = 200
                resp = {"message":"succeessful","status":f"{status}"} 

            else:
                status  = 200 
                resp = {"message":"Email is already in use","status":f"{status}"}  

    except Exception as e:
        status = 400
        resp = {"message":"ERROR on /Teacher/Signup","status":f"{status}",}
        print("ERROR:/Teacher/Signup-->",e)
    return jsonify(resp),status


        
@app.route("/Security/Signup",methods=["POST"])
def se_signup():
    status= 200
    resp ={}
    try:
        data = request.get_json("data")
        print(data)
        name = data["data"]["name"]
        surname = data["data"]["surname"]
        id_number = data["data"]["id_number"]
        staff_number = data["data"]["staff_number"]
        date_of_birth = data["data"]["date_of_birth"]
        email = data["data"]["email"]
        phone_number= data["data"]["phone_number"]
        address= data["data"]["address"]
        city= data["data"]["city"]
        pcode= data["data"]["pcode"]
        password = data["data"]["password"]
        position= data["data"]["position"]
        petrol_sector = data["data"]["petrol_sector"]

        email_data = mongo.db.admin.find({"email":f"{email}"})
        if email_data == []:
            if name!= "" and email !="" and password !="" and   id_number  != "":
                qr = tools()
                token = qr.generate_token(name,staff_number,"security")
                signup_payload = {
                    "name":f"{name}",
                    "surname":f"{surname}",
                    "id_number":f"{id_number}",
                    "date_of_birth": f"{date_of_birth}",
                    "email":f"{email}",
                    "phone_number":f"{phone_number}",
                    "address":f"{address}",
                    "city":f"{city}",
                    "pcode":f"{pcode}",
                    "password":f"{password}",
                    "staff_number":f"{staff_number}",
                    "position":f"{position}",
                    "petrol_sector":f"{petrol_sector}",
                    "acess_level":2,
                    "pqr":token
                }
                mongo.db.security.insert_one(signup_payload)
                q1= tools()
                q1.emailing_services(email,name,staff_number,"signup","","","","")
                status = 200
                resp = {"message":"succeessful","status":f"{status}"} 
            else:
                status = 200
                resp = {"message":"Email is already in use","status":f"{status}"} 

    except Exception as e:
        status = 400
        resp = {"message":"ERROR on /Security/Signup","status":f"{status}",}
        print("ERROR:/Security/Signup-->",e)
    return jsonify(resp),status


@app.route("/Domestic/Signup",methods=["POST"])
def dom_signup():
    status= 200
    resp ={}
    try:
        data = request.get_json("data")
        name = data["data"]["name"]
        surname = data["data"]["surname"]
        id_number = data["data"]["id_number"]
        date_of_birth = data["data"]["date_of_birth"]
        email = data["data"]["email"]
        phone_number= data["data"]["phone_number"]
        address= data["data"]["address"]
        city= data["data"]["city"]
        pcode= data["data"]["pcode"]
        password = data["data"]["password"]
        staff_number= data["data"]["staff_number"]
        job_title = data["data"]["job_title"]

        email_data = mongo.db.admin.find({"email":f"{email}"})
        if email_data == []:
            if name!= "" and email !="" and password !="" and   id_number  != "":
                qr = tools()
                token = qr.generate_token(name,staff_number,"domestic")
                signup_payload = {
                    "name":f"{name}",
                    "surname":f"{surname}",
                    "id_number":f"{id_number}",
                    "date_of_birth": f"{date_of_birth}",
                    "email":f"{email}",
                    "phone_number":f"{phone_number}",
                    "address":f"{address}",
                    "city":f"{city}",
                    "pcode":f"{pcode}",
                    "password":f"{password}",
                    "staff_number":f"{staff_number}",
                    "job_title":f"{job_title}",
                    "acess_level":1,
                    "pqr":token
                }
                mongo.db.domestic.insert_one(signup_payload)
                q1= tools()
                q1.emailing_services(email,name,staff_number,"signup","","","","")
                status = 200
                resp = {"message":"succeessful","status":f"{status}"}
            else:
                status = 200
                resp = {"message":"succeessful","status":f"{status}"}

    except Exception as e:
        status = 400
        resp = {"message":"ERROR on /Domestic/Signup","status":f"{status}",}
        print("ERROR:/Domestic/Signup-->",e)
    return jsonify(resp),status



@app.route("/Student/Signup",methods=["POST"])
def stu_signup():
    status= 200
    resp ={}
    try:
        data = request.get_json("data")
        print(data)
        name = data["data"]["name"]
        surname = data["data"]["surname"]
        id_number = data["data"]["id_number"]
        date_of_birth = data["data"]["date_of_birth"]
        email = data["data"]["email"]
        phone_number= data["data"]["phone_number"]
        address= data["data"]["address"]
        city= data["data"]["city"]
        pcode= data["data"]["pcode"]
        password = data["data"]["password"]
        student_number = data["data"]["student_number"]
        register_class = data["data"]["register_class"]
        pg_name = data["data"]["pg_name"]
        pg_surname= data["data"]["pg_surname"]
        pg_email  = data["data"]["pg_email"]
        pg_id_number =data["data"]["pg_id_number"]
        pg_phone_number = data["data"]["pg_cnum"]
        
        email_data = mongo.db.student.find({"email":f"{email}"})
        print("email_data-->",parse_json(email_data))
        if email_data == []:

            if name!= "" and email !="" and password !="":
                qr = tools()
                token = qr.generate_token(name,student_number,"student")
                signup_payload = {
                    "name":f"{name}",
                    "surname":f"{surname}",
                    "id_number":f"{id_number}",
                    "date_of_birth": f"{date_of_birth}",
                    "email":f"{email}",
                    "phone_number":f"{phone_number}",
                    "address":f"{address}",
                    "city":f"{city}",
                    "pcode":f"{pcode}",
                    "password":f"{password}",
                    "student_number":f"{student_number}",
                    "register_class":f"{register_class}",
                    "pg_name":f"{pg_name}",
                    "pg_surname":f"{pg_surname}",
                    "pg_email":f"{pg_email}",
                    "pg_id_number":f"{pg_id_number}",
                    "pg_phone_number":f"{pg_phone_number}",
                    "acess_level":0,
                    "pqr":token
                }
                mongo.db.student.insert_one(signup_payload)
                q1= tools()
                q1.emailing_services(email,name,student_number,"signup","","","","")
                q1.emailing_services(pg_email,pg_name,"","pg_signup","","","","")
                status = 200   
                resp = {"message":"succeessful","status":f"{status}"}
        else:
            status = 200   
            resp = {"message":"succeessful","status":f"{status}"} 
        print(resp)
    except Exception as e:
        status = 400
        resp = {"message":"ERROR on /Student/Signup","status":f"{status}","e":f"{e}"}
        print("ERROR:/Student/Signup-->",e)
    return jsonify(resp),status


@app.route("/Visitor/Signup",methods=["POST"])
def v_signup():
    status= 200
    resp ={}
    try:
        data = request.get_json("data")
        name = data["data"]["name"]
        surname = data["data"]["surname"]
        id_number = data["data"]["id_number"]
        date_of_birth = data["data"]["date_of_birth"]
        email = data["data"]["email"]
        phone_number= data["data"]["phone_number"]
        address= data["data"]["address"]
        city= data["data"]["city"]
        pcode= data["data"]["pcode"]
        password = data["data"]["password"]
        purpose_of_visit= data["data"]["purpose_of_visit"]

        email_data = mongo.db.admin.find({"email":f"{email}"})
        if email_data == []:
            if name!= "" and email !="" and password !="" and   id_number  != "":
                v_number = tools()
                visitor_number = v_number.random_number_creation() 
                qr = tools()
                token = qr.generate_token(name,visitor_number,"visitor")
                signup_payload = {
                    "name":f"{name}",
                    "surname":f"{surname}",
                    "id_number":f"{id_number}",
                    "date_of_birth": f"{date_of_birth}",
                    "email":f"{email}",
                    "phone_number":f"{phone_number}",
                    "address":f"{address}",
                    "city":f"{city}",
                    "pcode":f"{pcode}",
                    "password":f"{password}",
                    "visitor_number":f"{visitor_number}",
                    "purpose_of_visit":f"{purpose_of_visit}",
                    "visits":[],
                    "acess_level":0,
                    "pqr":token
                }
                print(signup_payload)
                mongo.db.visitor.insert_one(signup_payload)
                q1= tools()
                q1.vistor_emailing_services(email,name,visitor_number)
                status = 200
                resp = {"message":"succeessful","status":f"{status}"}
            else:
                status = 200
                resp = {"message":"succeessful","status":f"{status}"}
       

    except Exception as e:
        status = 400
        resp = {"message":"ERROR on /Visitor/Signup","status":f"{status}",}
        print("ERROR:/Visitor/Signup-->",e)
    return jsonify(resp),status


#login routes ///
@app.route("/User/login",methods=["POST"])
def login_user():
    status = 200
    resp = {}
    try:
        data = request.get_json("data")
        user_number = data["data"]["user_number"]
        password = data["data"]["password"]
        print(user_number,password)
        if user_number != "" and password != "":
            teacher = mongo.db.teacher.find_one({"staff_number":f"{user_number}"})
            admin = mongo.db.admin.find_one({ "admin_number":f"{user_number}"})
            student = mongo.db.student.find_one({"student_number":f"{user_number}"})
            domestic = mongo.db.domestic.find_one({"staff_number":f"{user_number}"})
            security = mongo.db.security.find_one({"staff_number":f"{user_number}"})
            visitor = mongo.db.visitor.find_one({"visitor_number":f"{user_number}"})
            if parse_json(teacher) != []:
                print("Teacher")
                data = parse_json(teacher)
                database_password = data["password"]   
                if database_password  == password:
                    print("welcome user")
                    status = 200
                    resp = {"message":"Welcome","status":status,"token":"active","user":data,"type_user":"teacher"}
                else:
                    print("Password is incorrect")
                    status = 200
                    resp = {"message":"Incorrect password","token":"down","status":status}  
            else:
                status = 200 
                resp = {"message":"No such user exists","token":"down","status":status}  
                
            if parse_json(admin) != []:
                print("Admin")
                data = parse_json(admin)
                database_password = data["password"]   
                if database_password  == password:
                    print("welcome user")
                    status = 200
                    resp = {"message":"Welcome","status":status,"token":"active","user":data,"type_user":"admin"}
                else:
                    print("Password is incorrect")
                    status = 200
                    resp = {"message":"Incorrect password","token":"down","status":status} 
            else:
                status = 200 
                resp = {"message":"No such user exists","token":"down","status":status}  
            if parse_json(student) != []:
                print("Student")
                data = parse_json(student)
                database_password = data["password"]   
                if database_password  == password:
                    print("welcome user")
                    status = 200
                    resp = {"message":"Welcome","status":status,"token":"active","user":data,"type_user":"student"}
                else:
                    print("Password is incorrect")
                    status = 200
                    resp = {"message":"Incorrect password","token":"down","status":status}
            else:
                status = 200 
                resp = {"message":"No such user exists","token":"down","status":status}   
            if parse_json(security) != []:
                print("Security")
                data = parse_json(security)
                database_password = data["password"]   
                if database_password  == password:
                    print("welcome user")
                    status = 200
                    resp = {"message":"Welcome","status":status,"token":"active","user":data,"type_user":"security"}
                else:
                    print("Password is incorrect")
                    status = 200
                    resp = {"message":"Incorrect password","token":"down","status":status} 
            else:
                status = 200 
                resp = {"message":"No such user exists","token":"down","status":status}   
            if parse_json(domestic) != []:
                print("Domestic")
                data = parse_json(domestic)
                database_password = data["password"]   
                if database_password  == password:
                    print("welcome user")
                    status = 200
                    resp = {"message":"Welcome","status":status,"token":"active","user":data,"type_user":"domestic"}
                else:
                    print("Password is incorrect")
                    status = 200
                    resp = {"message":"Incorrect password","token":"down","status":status}  
            else:
                status = 200 
                resp = {"message":"No such user exists","token":"down","status":status}  
            if parse_json(visitor) != []:
                print("Vistor")
                data = parse_json(visitor)
                database_password = data["password"]   
                if database_password  == password:
                    print("welcome user")
                    status = 200
                    resp = {"message":"Welcome","status":status,"token":"active","user":data,"type_user":"visitor"}
                else:
                    print("Password is incorrect")
                    status = 200
                    resp = {"message":"Incorrect password","token":"down","status":status}
            else:
                status = 200 
                resp = {"message":"No such user exists","token":"down","status":status}  
        else:
            print("missing credential on sign up ")
            status = 400
            resp = {"message":"ERROR on /User/login missing credential","status":f"{status}",}
    except Exception as e :
        status = 400
        resp = {"message":"ERROR on /User/login","status":f"{status}",}
        print("ERROR:/User/login-->",e)
    return jsonify(resp),status
#####################################################
####################################################
###################################################
#####################################################
#register check routes 

@app.route("/Enter/Grounds/QR",methods=["POST"])
def genrate_grounds_token():
    status = 200
    resp = {}
    try:
        data = request.get_json("data")
        user_number = data["data"]["user_number"]
        if user_number != "" :
            qr = tools()
            token = qr.genrate_grounds_qr(user_number) 
            security  = mongo.db.security.find_one({"staff_number":f"{user_number}"})
            if parse_json(security) != []:
                    data = parse_json(security)
                    email = data["email"]
                    name = data["name"] 
                    image = token[0]
                    qr.emailing_service_grounds_qr(email,name,image)
                    status = 200 
                    resp = {"message":"Toke sent","status":f"{status}"}
                    surname = data["surname"]
                    on_grounds_payload  ={
                        "name":f"{name}",
                        "surname":f"{surname}",
                        "user_number":f"{user_number}",
                        "email":f"{email}",
                    }
                    mongo.db.ongrounds.insert_one(on_grounds_payload)
                    status  = 200
                    resp ={"messge":"token sent","status":status}
            else :
                status = 400 
                resp = {"message":"User not found","status":f"{status}"}
    except Exception as e :
        status = 400
        resp = {"message":"ERROR on /Enter/Grounds/QR","status":f"{status}",}
        print("ERROR:/Enter/Grounds/QR-->",e)
    return jsonify(resp),status

@app.route("/Mark/Present",methods=["POST"])
def mark_present():
    status =200
    resp = {}
    try:
        data = request.get_json("data")
        user_number = data["data"]["user_number"]
        subject = data["data"]["subject"] 
        register_class  = data["data"]["register_class"]

        if user_number !="" and subject != "" and register_class != "":
            student = mongo.db.student.find_one({"student_number":f"{user_number}"})
            if parse_json(student) != []:
                print("Student")
                data = parse_json(student)
                name = data["name"]
                surname =data["surname"]
                user_number = data["student_number"]
                email= data["pg_email"]
                on_grounds_payload  ={
                        "name":f"{name}",
                        "surname":f"{surname}",
                        "user_number":f"{user_number}",
                        "email":f"{email}",
                        "register":f"{register_class}",
                        "subject":f"{subject}"
                    }
        
                mongo.db.inclass.insert_one(on_grounds_payload)
                status  = 200
                resp ={"message":"successful","status":status} 

    except Exception as e :
        status = 400
        resp = {"message":"ERROR on /Mark/Present","status":f"{status}",}
        print("ERROR:/Mark/Present /QR-->",e)
    return jsonify(resp),status
@app.route("/Enter/Grounds",methods=["POST"])
def enter_grounds():
    status = 200
    resp = {}
    try:
        data = request.get_json("data")
        user_number = data["data"]["user_number"]
        if user_number != "":
            teacher = mongo.db.teacher.find_one({"staff_number":f"{user_number}"})
            admin = mongo.db.admin.find_one({"admin_number":f"{user_number}"})
            student = mongo.db.student.find_one({"student_number":f"{user_number}"})
            domestic = mongo.db.domestic.find_one({"staff_number":f"{user_number}"})
            security = mongo.db.security.find_one({"staff_number":f"{user_number}"})
            visitor = mongo.db.visitor.find_one({"visitor_number":f"{user_number}"})
            if parse_json(teacher) != []:
                print("Teacher")
                data = parse_json(teacher)
                name = data["name"]
                surname =data["surname"]
                user_number = data["staff_number"]
                email= data["email"]
                on_grounds_payload  ={
                        "name":f"{name}",
                        "surname":f"{surname}",
                        "user_number":f"{user_number}",
                        "email":f"{email}"
                    }
                mongo.db.ongrounds.insert_one(on_grounds_payload)
                status  = 200
                resp ={"message":"successful","status":status}
            if parse_json(admin) != []:
                print("Admin")
                data = parse_json(admin)
                name = data["name"]
                surname =data["surname"]
                user_number = data["admin_number"]
                email= data["email"]
                on_grounds_payload  ={
                        "name":f"{name}",
                        "surname":f"{surname}",
                        "user_number":f"{user_number}",
                        "email":f"{email}"
                    }
        
                mongo.db.ongrounds.insert_one(on_grounds_payload)
                status  = 200
                resp ={"message":"successful","status":status}
            if parse_json(student) != []:
                print("Student")
                data = parse_json(student)
                print(data)
                name = data["name"]
                surname =data["surname"]
                user_number = data["student_number"]
                email= data["pg_email"]
                on_grounds_payload  ={
                        "name":f"{name}",
                        "surname":f"{surname}",
                        "user_number":f"{user_number}",
                        "email":f"{email}",
                    }
                print(on_grounds_payload)
                mongo.db.ongrounds.insert_one(on_grounds_payload)
                status  = 200
                resp ={"message":"successful","status":status} 
            if parse_json(security) != []:
                print("Security")
                data = parse_json(security)
                name = data["name"]
                surname =data["surname"]
                user_number = data["staff_number"]
                email= data["email"]
                on_grounds_payload  ={
                        "name":f"{name}",
                        "surname":f"{surname}",
                        "user_number":f"{user_number}",
                        "email":f"{email}"
                    }
        
                mongo.db.ongrounds.insert_one(on_grounds_payload)
                status  = 200
                resp ={"message":"successful","status":status}  
            if parse_json(domestic) != []:
                print("Domestic")
                data = parse_json(domestic)
                name = data["name"]
                surname =data["surname"]
                user_number = data["staff_number"]
                email= data["email"]
                on_grounds_payload  ={
                        "name":f"{name}",
                        "surname":f"{surname}",
                        "user_number":f"{user_number}",
                        "email":f"{email}"
                    }
        
                mongo.db.ongrounds.insert_one(on_grounds_payload)
                status  = 200
                resp ={"message":"successful","status":status}  
            if parse_json(visitor) != []:
                print("Vistor")
                data = parse_json(visitor)
                name = data["name"]
                surname =data["surname"]
                user_number = data["visitor_number"]
                email= data["email"]
                on_grounds_payload  ={
                        "name":f"{name}",
                        "surname":f"{surname}",
                        "user_number":f"{user_number}",
                        "email":f"{email}"
                    }
        
                mongo.db.ongrounds.insert_one(on_grounds_payload)
                status  = 200
                resp ={"message":"successful","status":status} 
        else :
            status = 400
            resp  = {"message":"missing credential", "status":status}
    except Exception as e :
        status = 400
        resp = {"message":"ERROR on /Enter/Grounds","status":f"{status}",}
        print("ERROR:/Enter/Grounds->",e)
    return jsonify(resp),status


@app.route("/Verify/Personal/QR",methods = ["POST"])
def generate_personal_qr():
    status= 200
    resp = {}
    try:
        data= request.get_json("data")
        print(data)
        user_number = data["data"]["user_number"]
        user_type = data["data"]["user_type"]
        print(user_number,user_type)
        if user_number != "" and user_type != "":
            if user_type == "teacher":
                teacher = mongo.db.teacher.find_one({"staff_number":f"{user_number}"})
                if parse_json(teacher) != []:
                    data = parse_json(teacher)
                    email = data["email"]
                    get_qr= tools()
                    get_qr.verify_user_qr(user_number,user_type,email)
                    status = 200
                    resp  = {"message":"successful","status":status}
            if user_type =="security":
                security = mongo.db.security.find_one({"staff_number":f"{user_number}"})    
                if parse_json(security) != []:
                    data = parse_json(security)
                    token = qr.generate_token(name,user_number)
                    email = data["email"]
                    get_qr= tools()
                    get_qr.verify_user_qr(user_number,user_type,email)
                    status = 200
                    resp  = {"message":"successful","status":status}
            elif user_type =="domestic":
                domestic = mongo.db.domestic.find_one({"staff_number":f"{user_number}"})
                if parse_json(domestic) != []:
                    print("Domestic")
                    data = parse_json(domestic)
                    email = data["email"]
                    get_qr= tools()
                    get_qr.verify_user_qr(user_number,user_type,email)
                    status = 200
                    resp  = {"message":"successful","status":status}

            elif user_type == "student":
                student = mongo.db.student.find_one({"student_number":f"{user_number}"})
                if  parse_json(student) != []:
                    data = parse_json(student)
                    email = student["email"]
                    get_qr= tools()
                    get_qr.verify_user_qr(user_number,user_type,email)
                    status = 200
                    resp  = {"message":"successful","status":status}
            
            elif user_type == "vistor":
                visitor = mongo.db.visitor.find_one({"visitor_number":f"{user_number}"})
                if parse_json(visitor)  != []:
                    data = parse_json(visitor)
                    email = data["email"]
                    get_qr= tools()
                    get_qr.verify_user_qr(user_number,user_type,email)
                    status = 200
                    resp  = {"message":"successful","status":status}
                    
            elif user_type  == "admin":
                admin = mongo.db.admin.find_one({"admin_number":f"{user_number}"})
                if parse_json(admin) != []:
                    data = parse_json(admin)
                    email = data["email"]
                    get_qr= tools()
                    get_qr.verify_user_qr(user_number,user_type,email)
                    status = 200
                    resp  = {"message":"successful","status":status}

        else:
            status  = 400
            resp = {"message":"missing credential","status":status}
    except Exception as e:
        status = 400
        resp = {"message":"ERROR on /Enter/Grounds","status":f"{status}",}
        print("ERROR:/Enter/Grounds->",e)
    return jsonify(resp),status


@app.route("/Generate/Class/RegisterQR",methods=["POST"])
def generate_token():
    status  = 200
    resp= {}
    try:
        data = request.get_json("data")
        user_number = data["data"]["user_number"]
        print(user_number)
        if user_number != "" :
            qr = tools()
            token = qr.class_register_qr_code(user_number) 
            teacher = mongo.db.teacher.find_one({"staff_number":f"{user_number}"})
            if parse_json(teacher) != []:
                data = parse_json(teacher)
                email = data["email"]
                name = data["name"] 
                image = token[0]
                qr.emailing_service_class_register(email,name,image)
                status = 200 
                resp = {"message":"Toke sent","status":f"{status}"}
            else :
                status = 400 
                resp = {"message":"User not found","status":f"{status}"}
    except Exception as e :
        status = 400
        resp = {"message":"ERROR on /Generate/Class/RegisterQR","status":f"{status}",}
        print("ERROR:/Generate/Class/RegisterQR-->",e)
    return jsonify(resp),status
##############################################################################
#######################################################################
################################################
#RETRIVE USER SECTION


@app.route("/retrieve/users",methods=["POST"])
def get_user_list():
    status = 200
    resp  = {}
    try:
        data = request.get_json("data")
        database_name = data["data"]["database_name"]
        if database_name == "domestic":
            users = mongo.db.domestic
            response  = users.find()
            if response != []:
                print("working d")
                status = 200
                return_response = parse_json(response)
                resp = {"response":return_response,"message":"user retieved","status":status}
        elif database_name == "teacher":
            users = mongo.db.teacher
            response  = users.find()
            if response != []:
                print("working t")
                status = 200
                return_response = parse_json(response)
                resp = {"response":return_response,"message":"user retieved","status":status}

        elif database_name == "student":
            users = mongo.db.student
            response  = users.find()
            if response != []:
                print("working st")
                status = 200
                return_response = parse_json(response)
                resp = {"response":return_response,"message":"user retieved","status":status}

        elif database_name == "security":
            users = mongo.db.security
            response  = users.find()
            if response != []:
                print("working se")
                status = 200
                return_response = parse_json(response)
                resp = {"response":return_response,"message":"user retieved","status":status}

        elif database_name == "visitor":
            users = mongo.db.visitor
            response  = users.find()
            if response != []:
                print("working v")
                status = 200
                return_response = parse_json(response)
                print(return_response)
                resp = {"response":return_response,"message":"user retieved","status":status}

        elif database_name == "admin":
            users = mongo.db.admin
            response  = users.find()
            if response != []:
                print("working v")
                status = 200
                return_response = parse_json(response)
                print(return_response)
                resp = {"response":return_response,"message":"user retieved","status":status}
    except Exception as e :
        status  = 400
        resp={"message":f"{e}","status":status}  
        print("ERORR (user retrieve route)--->",e)
    return jsonify(resp),status
#############################################################################
#########################################################
#############################################
#SUB SERVICES
#Delete user area
@app.route("/Delete/User",methods=["POST"])
def user_delete():
    status = 200
    resp  ={}
    try:
        data = request.get_json("data")
        print(data)
        name = data["data"]["name"]
        surname = data["data"]["surname"]
        user_type =data["data"]["user_type"]

        if name != "" and surname !="" and user_type != "":
            if user_type == "domestic":              
                users = mongo.db.domestic
                response  = users.find_one({"name":f"{name}","surname":f"{surname}"})
                if response != []:
                    print("working d")
                    status = 200
                    return_response = parse_json(response)
                    user_database_id  = return_response["_id"]
                    if user_database_id != "":
                        mongo.db.domestic.delete_one({"name":f"{name}","surname":f"{surname}"})
                        status =200
                        resp = {"message":"deleted","status":status}
                    else:
                        status =400
                        resp = {"message":"Could not get User _id ","status":status}
            elif user_type == "teacher":
                users = mongo.db.teacher
                response  = users.find_one({"name":f"{name}","surname":f"{surname}"})
                if response != []:
                    print("working t")
                    status = 200
                    return_response = parse_json(response)
                    user_database_id  = return_response["_id"]
                    if user_database_id != "":
                        mongo.db.teacher.delete_one({"name":f"{name}","surname":f"{surname}"})
                        status =200
                        resp = {"message":"deleted","status":status}
                    else:
                        status =400
                        resp = {"message":"Could not get User _id ","status":status}

            elif user_type == "student":
                users = mongo.db.student
                response  = users.find_one({"name":f"{name}","surname":f"{surname}"})
                if response != []:
                    print("working st")
                    status = 200
                    return_response = parse_json(response)
                    print(return_response)
                    user_database_id  = return_response["_id"]
                    if user_database_id != "":
                        mongo.db.student.delete_one({"name":f"{name}","surname":f"{surname}"})
                        status =200
                        resp = {"message":"deleted","status":status}
                    else:
                        status =400
                        resp = {"message":"Could not get User _id ","status":status}

            elif user_type == "security":
                users = mongo.db.security
                response  = users.find_one({"name":f"{name}","surname":f"{surname}"})
                if response != []:
                    print("working se")
                    status = 200
                    return_response = parse_json(response)
                    user_database_id  = return_response["_id"]
                    if user_database_id != "":
                        mongo.db.security.delete_one({"name":f"{name}","surname":f"{surname}"})
                        status =200
                        resp = {"message":"deleted","status":status}
                    else:
                        status =400
                        resp = {"message":"Could not get User _id ","status":status}

            elif user_type == "visitor":
                users = mongo.db.visitor
                response  = users.find_one({"name":f"{name}","surname":f"{surname}"})
                if response != []:
                    print("working v")
                    status = 200
                    return_response = parse_json(response)
                    print(return_response)
                    user_database_id  = return_response["_id"]
                    if user_database_id != "":
                        mongo.db.visitor.delete_one({"name":f"{name}","surname":f"{surname}"})
                        status =200
                        resp = {"message":"deleted","status":status}
                    else:
                        status =400
                        resp = {"message":"Could not get User _id ","status":status}
            else:
                status =400
                resp = {"message":"There is no user in the database with these credentials","status":status}
        else:
            status = 500
            resp = {"message":"Missing credential to make query","status":status}
    except Exception as e:
        status  = 400
        resp={"message":f"{e}","status":status}  
        print("ERORR (/delete/user route)--->",e)
    return jsonify(resp),status

@app.route("/Get/User",methods=["POST"])
def get_user():
    status = 200
    resp = {}
    try:
        data= request.get_json("data")
        print(data)
        user_number = data["data"]["user_number"]
        if user_number != "":
            teacher = mongo.db.teacher.find_one({"staff_number":f"{user_number}"})
            admin = mongo.db.admin.find_one({ "admin_number":f"{user_number}"})
            student = mongo.db.student.find_one({"student_number":f"{user_number}"})
            domestic = mongo.db.domestic.find_one({"staff_number":f"{user_number}"})
            security = mongo.db.security.find_one({"staff_number":f"{user_number}"})
            visitor = mongo.db.visitor.find_one({"visitor_number":f"{user_number}"})
            print(parse_json(admin))
            print(parse_json(teacher))
            if parse_json(teacher) != []:
                print("Teacher")
                data = parse_json(teacher) 
                status= 200
                resp = {"status":status,"token":"active","user":data}
                
            if parse_json(admin) != []:
                print("Admin")
                data = parse_json(admin)
                status= 200
                resp = {"status":status,"token":"active","user":data}
            if parse_json(student) != []:
                print("Student")
                data = parse_json(student)
                status= 200
                resp = {"status":status,"token":"active","user":data}
            if parse_json(security) != []:
                print("Security")
                data = parse_json(security)
                status= 200
                resp = {"status":status,"token":"active","user":data}
            if parse_json(domestic) != []:
                print("Domestic")
                data = parse_json(domestic)
                status= 200
                resp = {"status":status,"token":"active","user":data}
            if parse_json(visitor) != []:
                print("Vistor")
                data = parse_json(visitor)
                status= 200
                resp = {"status":status,"token":"active","user":data}

    except Exception as e :
        status  = 400
        resp={"message":f"{e}","status":status}  
        print("ERORR (/Get/User route)--->",e)
    return jsonify(resp),status


@app.route("/Edit/User",methods= ["POST"])
def edit_user():
    status = 200 
    resp  = {}
    try:
        data =request.get_json("data")
        new_crediatials = data["data"]["user_profile"]
        user_number = data["data"]["user_number"]
        print(new_crediatials,user_number)
        if new_crediatials != {}  and user_number != "":
            teacher = mongo.db.teacher.find_one({"staff_number":f"{user_number}"})
            admin = mongo.db.admin.find_one({ "admin_number":f"{user_number}"})
            student = mongo.db.student.find_one({"student_number":f"{user_number}"})
            domestic = mongo.db.domestic.find_one({"staff_number":f"{user_number}"})
            security = mongo.db.security.find_one({"staff_number":f"{user_number}"})
            visitor = mongo.db.visitor.find_one({"visitor_number":f"{user_number}"})
            if parse_json(teacher) != []:
                print("Teacher")
                name = new_crediatials["name"]
                surname = new_crediatials["surname"]
                id_number = new_crediatials["id_number"]
                date_of_birth = new_crediatials["date_of_birth"]
                email = new_crediatials["email"]
                phone_number= new_crediatials["phone_number"]
                address= new_crediatials["address"]
                city= new_crediatials["city"]
                pcode= new_crediatials["pcode"]
                password = new_crediatials["password"]
                staff_number = new_crediatials["staff_number"]
                position= new_crediatials["position"]
                subject= new_crediatials["subject"]
                register_class = new_crediatials["register_class"]
            
                newvalues = { "$set": { 
                "name":f"{name}",
                "surname":f"{surname}",
                "id_number":f"{id_number}",
                "date_of_birth": f"{date_of_birth}",
                "email":f"{email}",
                "phone_number":f"{phone_number}",
                "address":f"{address}",
                "city":f"{city}",
                "pcode":f"{pcode}",
                "password":f"{password}",
                "staff_number":f"{staff_number}",
                "position":f"{position}",
                "subject":f"{subject}",
                "register_class":f"{register_class}" } }
                mongo.db.teacher.update_one({"staff_number":f"{user_number}"},newvalues)
                status = 200
                resp ={"message":"successful","token":"true" ,"status":status}
            if parse_json(admin) != []:
                    print("Admin")
                    name = new_crediatials["name"]
                    surname = new_crediatials["surname"]
                    id_number = new_crediatials["id_number"]
                    date_of_birth = new_crediatials["date_of_birth"]
                    email = new_crediatials["email"]
                    phone_number= new_crediatials["phone_number"]
                    address= new_crediatials["address"]
                    city= new_crediatials["city"]
                    pcode= new_crediatials["pcode"]
                    password = new_crediatials["password"]
                    admin_number = new_crediatials["admin_number"]
                    

                    newvalues = { "$set": { 
                    "name":f"{name}",
                    "surname":f"{surname}",
                    "id_number":f"{id_number}",
                    "date_of_birth": f"{date_of_birth}",
                    "email":f"{email}",
                    "phone_number":f"{phone_number}",
                    "address":f"{address}",
                    "city":f"{city}",
                    "pcode":f"{pcode}",
                    "password":f"{password}",
                    "admin_number":f"{admin_number}"} 
                    }
                    mongo.db.admin.update_one({"staff_number":f"{user_number}"},newvalues)
                    status = 200
                    resp ={"message":"successful","token":"true" ,"status":status}
            if parse_json(student) != []:
                    print("Student")
                    name = new_crediatials["name"]
                    surname = new_crediatials["surname"]
                    id_number = new_crediatials["id_number"]
                    date_of_birth = new_crediatials["date_of_birth"]
                    email = new_crediatials["email"]
                    phone_number= new_crediatials["phone_number"]
                    address= new_crediatials["address"]
                    city= new_crediatials["city"]
                    pcode= new_crediatials["pcode"]
                    password = new_crediatials["password"]
                    student_number = new_crediatials["student_number"]
                    register_class = new_crediatials["register_class"]
                    pg_name = new_crediatials["pg_name"]
                    pg_surname= new_crediatials["pg_surname"]
                    pg_email  = new_crediatials["pg_email"]
                    pg_id_number =new_crediatials["pg_id_number"]
                    pg_phone_number = new_crediatials["pg_cnum"]

                    newvalues = { "$set": { 
                    "name":f"{name}",
                    "surname":f"{surname}",
                    "id_number":f"{id_number}",
                    "date_of_birth": f"{date_of_birth}",
                    "email":f"{email}",
                    "phone_number":f"{phone_number}",
                    "address":f"{address}",
                    "city":f"{city}",
                    "pcode":f"{pcode}",
                    "password":f"{password}",
                    "student_number":f"{student_number}",
                    "register_class":f"{register_class}",
                    "pg_name":f"{pg_name}",
                    "pg_surname":f"{pg_surname}",
                    "pg_email":f"{pg_email}",
                    "pg_id_number":f"{pg_id_number}",
                    "pg_phone_number":f"{pg_phone_number}" }
                     }
                    mongo.db.student.update_one({"student_number":f"{user_number}"},newvalues)
                    status = 200
                    resp ={"message":"successful","token":"true" ,"status":status} 
            if parse_json(security) != []:
                    print("Security")
                    name = new_crediatials["name"]
                    surname = new_crediatials["surname"]
                    id_number = new_crediatials["id_number"]
                    date_of_birth = new_crediatials["date_of_birth"]
                    email = new_crediatials["email"]
                    phone_number= new_crediatials["phone_number"]
                    address= new_crediatials["address"]
                    city= new_crediatials["city"]
                    pcode= new_crediatials["pcode"]
                    password = new_crediatials["password"]
                    staff_number = new_crediatials["staff_number"]
                    position= new_crediatials["position"]
                    petrol_sector = new_crediatials["petrol_sector"]
                  

                    newvalues = { "$set": { 
                    "name":f"{name}",
                    "surname":f"{surname}",
                    "id_number":f"{id_number}",
                    "date_of_birth": f"{date_of_birth}",
                    "email":f"{email}",
                    "phone_number":f"{phone_number}",
                    "address":f"{address}",
                    "city":f"{city}",
                    "pcode":f"{pcode}",
                    "password":f"{password}",
                    "staff_number":f"{staff_number}",
                    "position":f"{position}",
                    "petrol_sector":f"{petrol_sector}" } }
                    mongo.db.security.update_one({"staff_number":f"{user_number}"},newvalues)
                    status = 200
                    resp ={"message":"successful","token":"true" ,"status":status}
            if parse_json(domestic) != []:
                    print("Domestic")
                    name = new_crediatials["name"]
                    surname = new_crediatials["surname"]
                    id_number = new_crediatials["id_number"]
                    date_of_birth = new_crediatials["date_of_birth"]
                    email = new_crediatials["email"]
                    phone_number= new_crediatials["phone_number"]
                    address= new_crediatials["address"]
                    city= new_crediatials["city"]
                    pcode= new_crediatials["pcode"]
                    password = new_crediatials["password"]
                    staff_number = new_crediatials["staff_number"]
                    position= new_crediatials["position"]
                    job_title  = new_crediatials["job_title"]

                    newvalues = { "$set": { 
                        "name":f"{name}",
                        "surname":f"{surname}",
                        "id_number":f"{id_number}",
                        "date_of_birth": f"{date_of_birth}",
                        "email":f"{email}",
                        "phone_number":f"{phone_number}",
                        "address":f"{address}",
                        "city":f"{city}",
                        "pcode":f"{pcode}",
                        "password":f"{password}",
                        "staff_number":f"{staff_number}",
                        "job_title":f"{job_title}" } }
                    mongo.db.domestic.update_one({"staff_number":f"{user_number}"},newvalues)
                    status = 200
                    resp ={"message":"successful","token":"true" ,"status":status}  
            if parse_json(visitor) != []:
                    print("Vistor")
                    name = new_crediatials["name"]
                    surname = new_crediatials["surname"]
                    id_number = new_crediatials["id_number"]
                    date_of_birth = new_crediatials["date_of_birth"]
                    email = new_crediatials["email"]
                    phone_number= new_crediatials["phone_number"]
                    address= new_crediatials["address"]
                    city= new_crediatials["city"]
                    pcode= new_crediatials["pcode"]
                    password = new_crediatials["password"]
                    purpose_of_visit  = new_crediatials["purpose_of_visit"]
                    visitor_number=new_crediatials["visitor_number"]
                    newvalues = { "$set": { 
                        "name":f"{name}",
                        "surname":f"{surname}",
                        "id_number":f"{id_number}",
                        "date_of_birth": f"{date_of_birth}",
                        "email":f"{email}",
                        "phone_number":f"{phone_number}",
                        "address":f"{address}",
                        "city":f"{city}",
                        "pcode":f"{pcode}",
                        "password":f"{password}",
                        "visitor_number":f"{visitor_number}",
                        "purpose_of_visit":f"{purpose_of_visit}" } }
                    mongo.db.visitor.update_one({"staff_number":f"{user_number}"},newvalues)
                    status = 200
                    resp ={"message":"successful","token":"true" ,"status":status}

    except Exception as e :
        status  = 400
        resp={"message":f"{e}","status":status}  
        print("ERORR (/Edit/User route)--->",e)
    return jsonify(resp),status


###############################################
################################################
##############################################
# Forget password and Change password 

@app.route("/forgot/passowrd1",methods=["POST"])
def forgot_password1():
    status =200
    resp = {}
    try:
        print("fogotten password")
        data = request.get_json("data")
        email = data["data"]["email"]
        if email != "":
            teacher = mongo.db.teacher.find_one({"email":f"{email}"})
            admin = mongo.db.admin.find_one({ "email":f"{email}"})
            student = mongo.db.student.find_one({"email":f"{email}"})
            domestic = mongo.db.domestic.find_one({"email":f"{email}"})
            security = mongo.db.security.find_one({"email":f"{email}"})
            visitor = mongo.db.visitor.find_one({"email":f"{email}"})
            if parse_json(teacher) != []:
                print("Teacher")
                data = parse_json(teacher)
                email = data["email"]
                name = data["name"]
                user_number  = data["staff_number"]
                password = data["password"]
                #checinking if code has been made
                #getting a token
                q1 = tools()
                number = q1.random_number_creation()
                if number != "":
                    q1.emailing_services(email,name,user_number,"forgot_password","","",number)
                    forgot_user_payload={
                        "name":f"{name}",
                        "email":f"{email}",
                        "user_number":f"{user_number}",
                        "verification_number":f"{number}",
                        "password":f"{password}"
                    }
                    mongo.db.forgot.insert_one(forgot_user_payload)
                    status = 200
                    resp ={"meassage":"email sent","token":"active"}
                else:
                    print("Verification number was not created")
                    status = 400
                    resp = {"message":"Verification number was not created","status":status} 

            if parse_json(admin) != []:
                print("Admin")
                data = parse_json(admin)
                email = data["email"]
                name = data["name"]
                user_number  = data["admin_number"]
                password = data["password"]
                #getting a token
                q1 = tools()
                number = q1.random_number_creation()
                if number != "":
                    q1.emailing_services(email,name,user_number,"forgot_password","","",number)
                    forgot_user_payload={
                        "name":f"{name}",
                        "email":f"{email}",
                        "user_number":f"{user_number}",
                        "verification_number":f"{number}",
                        "password":f"{password}"

                    }
                    mongo.db.forgot.insert_one(forgot_user_payload)
                    status = 200
                    resp ={"meassage":"email sent","token":"active"}
                else:
                    print("Verification number was not created")
                    status = 400
                    resp = {"message":"Verification number was not created","status":status} 

            if parse_json(student) != []:
                print("Student")
                data = parse_json(student)
                email = data["email"]
                name = data["name"]
                user_number  = data["student_number"]
                password = data["password"]
                #getting a token
                q1 = tools()
                number = q1.random_number_creation()
                if number != "":
                    q1.emailing_services(email,name,user_number,"forgot_password","","",number)
                    forgot_user_payload={
                        "name":f"{name}",
                        "email":f"{email}",
                        "user_number":f"{user_number}",
                        "verification_number":f"{number}",
                        "password":f"{password}"
                    }
                    mongo.db.forgot.insert_one(forgot_user_payload)
                    status = 200
                    resp ={"meassage":"email sent","token":"active"}
                else:
                    print("Verification number was not created")
                    status = 400
                    resp = {"message":"Verification number was not created","status":status} 

            if parse_json(security) != []:
                print("Security")
                data = parse_json(security)
                email = data["email"]
                name = data["name"]
                user_number  = data["staff_number"]
                password = data["password"]
                #getting a token
                q1 = tools()
                number = q1.random_number_creation()
                if number != "":
                    q1.emailing_services(email,name,user_number,"forgot_password","","",number)
                    forgot_user_payload={
                        "name":f"{name}",
                        "email":f"{email}",
                        "user_number":f"{user_number}",
                        "verification_number":f"{number}",
                        "password":f"{password}"
                    }
                    mongo.db.forgot.insert_one(forgot_user_payload)
                    status = 200
                    resp ={"meassage":"email sent","token":"active"}
                else:
                    print("Verification number was not created")
                    status = 400
                    resp = {"message":"Verification number was not created","status":status} 

            if parse_json(domestic) != []:
                print("Domestic")
                data = parse_json(domestic)
                email = data["email"]
                name = data["name"]
                user_number  = data["staff_number"]
                password = data["password"]
                print(name)
                #getting a token
                q1 = tools()
                number = q1.random_number_creation()
                print(number)
                if number != "":
                    q1.emailing_services(email,name,user_number,"forgot_password","","",number,"")
                    forgot_user_payload={
                        "name":f"{name}",
                        "email":f"{email}",
                        "user_number":f"{user_number}",
                        "verification_number":f"{number}",
                        "password":f"{password}"
                    }
                    mongo.db.forgot.insert_one(forgot_user_payload)
                    status = 200
                    resp ={"meassage":"email sent","token":"active"}
                else:
                    print("Verification number was not created")
                    status = 400
                    resp = {"message":"Verification number was not created","status":status}  

            if parse_json(visitor) != []:
                print("Vistor")
                data = parse_json(visitor)
                email = data["email"]
                name = data["name"]
                user_number  = data["visitor_number"]
                password = data["password"]
                #getting a token
                q1 = tools()
                number = q1.random_number_creation()
                if number != "":
                    q1.emailing_services(email,name,user_number,"forgot_password","","",number)
                    forgot_user_payload={
                        "name":f"{name}",
                        "email":f"{email}",
                        "user_number":f"{user_number}",
                        "verification_number":f"{number}",
                        "password":f"{password}"
                    }
                    mongo.db.forgot.insert_one(forgot_user_payload)
                    status = 200
                    resp ={"meassage":"email sent","token":"active"}
                else:
                    print("Verification number was not created")
                    status = 400
                    resp = {"message":"Verification number was not created","status":status} 

        else:
            status = 400
            resp = {"message":"Missing credential","status":status}
    except Exception as e:
        status  = 400
        resp={"message":f"{e}","status":status}  
        print("ERORR (/forgot/passowrd1 route)--->",e)
    return jsonify(resp),status


@app.route("/forgot/passoword/send",methods=["POST"])
def forgot_paswword_send():
    status = 200
    resp ={}
    try:
        data = request.get_json("data")
        verification_number = data["data"]["verification_number"]
        if verification_number != "":
            forgort_password_user = mongo.db.forgot.find_one({"verification_number":f"{verification_number}"})
            if parse_json(forgort_password_user) != []:
                data  = parse_json(forgort_password_user) 
                database_veri_num = data["verification_number"]
                if verification_number == database_veri_num:
                    email = data["email"]
                    name = data["name"]
                    user_number  = data["user_number"] 
                    password  = data["password"]
                    q1 = tools()
                    q1.emailing_services(email,name,user_number,"forgot_password_send","","","",password)
                    mongo.db.forgot.delete_many({"email":f"{email}"})
                    status = 200
                    resp = {"message":"sucess","status":status}
                else:
                    print("verification number incorect not found")
                    status = 400
                    resp = {"message":"verification number incorect not found","response":"false","status":status}

            else:
                print("forgort_password_user not found")
                status = 400
                resp = {"message":"forgort_password_user not found","status":status}

        else:
            print("Data payload is  empty")
            status = 400
            resp = {"message":"Data payload is  empty","status":status}

    except Exception as e:
        status  = 400
        resp={"message":f"{e}","status":status}  
        print("ERORR (/forgot/passowrd1 route)--->",e)
    return jsonify(resp),status
########################################################################
########################################################
#########################################
#Purge/Daily checking area
# collection daily purge function
@app.route("/Purge/Daily",methods=["POST"]) 
def purge():
    status = 200
    resp ={}
    try:
        response = mongo.db.ongrounds.find_one()
        response_return = mongo.db.inclass.find_one()
        if parse_json(response) != [] and parse_json(response_return) != []:
            mongo.db.ongrounds.remove()
            mongo.db.inclass.remove()
            status = 200
            resp = {"message":"deleted", "status":status}
        else:
            status = 400
            resp = {"message":"not deleted", "status":status}  
    except Exception as e :
        status  = 400
        resp={"message":f"{e}","status":status}  
        print("ERORR (/Purge/Daily route)--->",e)
    return jsonify(resp),status


@app.route("/Purge/Local/logs",methods=["POST"]) 
def purge_local_log():
    status = 200
    resp ={}
    try:
        purge = tools()
        purge.purge_qr_codes()
        status = 200
        resp = {"message": "deleted", "status":status}

    except Exception as e :
        status  = 400
        resp={"message":f"{e}","status":status}  
        print("ERORR (/Purge/Daily route)--->",e)
    return jsonify(resp),status


##############################################################
###############################################################
##################################################################
###############################################
# BREACH ALARM section 

@app.route("/Make/Breachalarm",methods= ["POST"])
def make_alarm():
    status = 200
    resp = {}
    try:
        data = request.get_json("data")
        print(data)
        user_number = data["data"]["user_number"]
        quadrant = data["data"]["quadrant"]
        breach_type = data["data"]["breach_type"]
        breach = tools()
        breach_number = breach.random_number_creation()
        if breach_type != "" and breach_number != "" and quadrant != "" and user_number != "":
            if (breach_type  == "Robbery"):
                #print("The breach is at:" + quadrant) 
                people_profiles = mongo.db.ongrounds.find()
                profiles = parse_json(people_profiles)
                number_of_users= mongo.db.ongrounds.count_documents({})
                c = tools()
                c.breach_alram_email_service(breach_type) 
                c.retrieve(profiles,number_of_users,breach_type)

            elif(breach_type  == "Fire"):
                #print("The breach happend in quadrant:" + quadrant) 
                people_profiles = mongo.db.ongrounds.find()
                profiles = parse_json(people_profiles)
                number_of_users= mongo.db.ongrounds.count_documents({})
                c = tools()
                c.breach_alram_email_service(breach_type)
                c.retrieve(profiles,number_of_users,breach_type)

            elif(breach_type == "Intruder"):
                #print("The breach happend in quadrant:" + quadrant)
                people_profiles = mongo.db.ongrounds.find()
                profiles = parse_json(people_profiles)
                number_of_users= mongo.db.ongrounds.count_documents({})
                c = tools()
                c.breach_alram_email_service(breach_type)
                c.retrieve(profiles,number_of_users,breach_type)

            elif(breach_type  == "Terrorism"):
                #print("The breach happend in quadrant:" + quadrant)
                people_profiles = mongo.db.ongrounds.find()
                profiles = parse_json(people_profiles)
                number_of_users= mongo.db.ongrounds.count_documents({})
                print(number_of_users)
                c = tools()
                c.breach_alram_email_service(breach_type)
                c.retrieve(profiles,number_of_users,breach_type)

            elif(breach_type  == "Medical Emergency"):
                #print("The breach happend in quadrant:" + quadrant)            
                people_profiles = mongo.db.ongrounds.find()
                number_of_users= mongo.db.ongrounds.count_documents({})
                c = tools()
                c.breach_alram_email_service(breach_type)


            not_at_school = []
            missing = []
            in_school = []
        
            student_number = mongo.db.student.find()
            present = mongo.db.ongrounds.find()
            inclass = mongo.db.inclass.find()
            if(student_number != [] and present != [] and inclass != []):
                data_present = parse_json(present) 
                ongrounds_array = []
                for i in data_present:
                    ongrounds_array.append(i["user_number"])

                data_student_number =parse_json(student_number)
                student_array = []
                for i in data_student_number:
                    student_array.append(i["student_number"])

                data_in_class =parse_json(inclass)
                inclass_array = []
                for  i in data_in_class:
                    inclass_array.append(i["user_number"]) 


                count = mongo.db.ongrounds.count_documents({})
                for i in ongrounds_array:
                    for j  in student_array:
                        if  j == i :
                            if j in not_at_school: 
                                print("here")
                            else:
                                not_at_school.append(j)
                        else:
                            if j in in_school: 
                                print("here")
                            else:
                                in_school.append(j)
                            
                print("those in school-->",in_school)
                here= ""
                for i in in_school:
                    for j in inclass_array:
                        if i == j :
                            here = ""
                        else:
                            if i in missing: 
                                here = ""
                            else:
                                missing.append(i)
                breachAlarm_payload = {
                "breach_number":f"{breach_number}",
                "user_number":f"{user_number}",
                "quadrant":f"{quadrant}",
                "breach_type":f"{breach_type}",
                "students_missing":missing,
                "stundents_not_at_school":not_at_school,
                "status":""
            }
            breach.log_breach(breach_type,quadrant,user_number,breach_number)

            mongo.db.breach_alarm.insert_one(breachAlarm_payload)
            status =200
            resp = {"message":"successful","status":status,"missing":missing ,"not_at_school":not_at_school}
        else:
            status = 400
            resp = {"message":"Unsuccesful","status":status}

    except Exception as e :
        status  = 400
        resp={"message":f"{e}","status":status}  
        print("ERORR (/Make/Breachalarm route)--->",e)
    return jsonify(resp),status

@app.route("/Breachalarm/Update",methods= ["POST"])
def update_alarm():
    status = 200
    resp = {}
    try:
        data = request.get_json("data")
        breach_number =data["data"]["breach_number"]
        if breach_number != "":
            breach = mongo.db.breach_alarm
            response  = breach.find()
            if response != []:
                mongo.db.breach_alarm.update_one({"breach_number":f"{breach_number}"},{ "$set": { "status":"onroute"}})
                status = 200
                resp ={"message":"successful","token":"true" ,"status":status}  
            else:
                status = 200
                resp = {"message":"unsuccessful","status":status}
                     
        else:
            status =200
            resp = {"message":"missing credentials","status":status}

    except Exception as e :
        status  = 400
        resp={"message":f"{e}","status":status}  
        print("ERORR (/Breachalarm/Update route)--->",e)
    return jsonify(resp),status

@app.route("/Breachalarm/Check",methods= ["GET"])
def check_alarm():
    status = 200
    resp = {}
    try:
        breach = mongo.db.breach_alarm.find()
        if breach  != []:
            response = parse_json(breach)
            status = 200
            resp ={"message":"breach is present","response":response[0] ,"status":status}  
        else:
            status = 200
            resp = {"message":"no breach availble","status":status}
                     

    except Exception as e :
        status  = 400
        resp={"message":f"{e}","status":status}  
        print("ERORR (/Breachalarm/Check route)--->",e)
    return jsonify(resp),status

@app.route("/Breachalarm/Delete",methods= ["POST"])
def delete_alarm():
    status = 200
    resp = {}
    try:
        data = request.get_json("data")
        print(data)
        breach_number =data["data"]["breach_number"]
        if breach_number != "":
            database  = mongo.db.breach_alarm.find_one({"breach_number":f"{breach_number}"})
            if database != []:
                    mongo.db.breach_alarm.delete_one({"breach_number":f"{breach_number}"})
                    status =200
                    resp = {"message":"Breach has been deleted","status":status}
            else:
                status =400
                resp = {"message":"Breach not in database ","status":status}

    except Exception as e :
        status  = 400
        resp={"message":f"{e}","status":status}  
        print("ERORR (/breachalarm/delete route)--->",e)
    return jsonify(resp),status



#####################################################
##################################################
################################################
##############################################
# SUB functions

@app.route("/Leave/comment", methods=["POST"])
def leave_comment():
    status=200
    resp ={}
    try:
        data = request.get_json("data")
        if data != {}:
            print(data)
            name = data["data"]["name"]
            message = data["data"]["message"]
            email = data["data"]["email"]
            if name != "" and message  !="" and  email != "":
                number = tools()
                message_number = number.random_number_creation()
                payload  ={
                        "name":f"{name}",
                        "email":f"{email}",
                        "message":f"{message}",
                        "message_number":f"{message_number}"
                    }
                mongo.db.messages.insert(payload)
                q1= tools()
                q1.emailing_services(email,name,"","message","","","","")
                status = 200
                resp = {"message":"successful", "status":status}
        else:
            status = 400
            resp = {"message": "message was not added"}
    except Exception as e:
        status  = 400
        resp={"message":f"{e}","status":status}  
        print("ERORR (/Leave/comment route)--->",e)
    return jsonify(resp),status

@app.route ("/Delete/Message",methods=["POST"])
def delete_messages():
    status = 200
    resp ={}
    try:
        data = request.get_json("data")
        message_number  = data["data"]["message_number"]
        if message_number != "":
            messages = mongo.db.messages.find_one({"message_number":f"{message_number}"})
            if messages != []:
                status = 200
                return_response = parse_json(messages)
                if return_response != []:
                    mongo.db.messages.delete_one({"message_number":f"{message_number}"})
                    status =200
                    resp = {"message":"message has been deleted","status":status}
                else:
                    status =400
                    resp = {"message":"could not get messsage  ","status":status}
        else :
            status = 400
            resp ={"message": "The message number is no in the database please verify","status":status}
    
    except Exception as e :
        status  = 400
        resp={"message":f"{e}","status":status}  
        print("ERORR (/Delete/Messagese route)--->",e)
    return jsonify(resp),status

@app.route("/Message/Response",methods=["POST"])
def respose_to_messages():
    status =200
    resp = {}
    try:
        data  = request.get_json("data")
        if data != "":
            message_number= data["data"]["message_number"] 
            response_message =data["data"]["response_message"]

            if message_number !="" and response_message != "":
                response = mongo.db.messages.find_one({"message_number":f"{message_number}"})
                data = parse_json(response)
                email = data["email"]
                name  = data["name"]
                qr = tools()
                qr.emailing_message_response(email,name,response_message)
                status=200
                resp = {"message":"successful","status":status}
        else:
            status=400
            resp = {"message":"no response recieved ","status":status}
        
    except Exception as e:
        status  = 400
        resp={"message":f"{e}","status":status}  
        print("ERORR (/Retrieve/Messages route)--->",e)
    return jsonify(resp),status
@app.route("/Retrieve/Messages", methods=["GET"])
def messages():
    status  = 200
    resp = {}
    try:
        messages_r = mongo.db.messages.find()
        if messages_r != [] :
            status = 200
            messages = parse_json(messages_r)
            resp = {"response":messages,"message":"messages retieved","status":status}
        else:
            status = 400
            resp = {"message": "messges not found  ", "status":status}
    except Exception as e :
        status  = 400
        resp={"message":f"{e}","status":status}  
        print("ERORR (/Retrieve/Messages route)--->",e)
    return jsonify(resp),status
##############################################
############################################
###########################################
#reports area 

@app.route("/Report",methods=["GET"])
def get_report():
    status =200
    resp = {}
    try:
        number_of_teacher = 0
        number_of_admin = 0
        number_of_student = 0
        number_of_domestic = 0
        number_of_security = 0
        number_of_visitor = 0

        teacher = mongo.db.teacher.find()
        admin = mongo.db.admin.find()
        student = mongo.db.student.find()
        domestic = mongo.db.domestic.find()
        security = mongo.db.security.find()
        visitor = mongo.db.visitor.find()

        if teacher != []:
            number_of_teacher = mongo.db.teacher.count()

        if admin != []:
            number_of_admin = mongo.db.admin.count()

        if student != []:
            number_of_student = mongo.db.student.count()

        if domestic != []:
            number_of_domestic = mongo.db.domestic.count()

        if security != []:
            number_of_security = mongo.db.security.count()

        if visitor != []:
            number_of_visitor = mongo.db.visitor.count()

        numbers = tools()
        usage_report =numbers.activity_report()

        br=usage_report[0]
        ong=usage_report[1]
        rc=usage_report[2]
      

        status = 200
        resp ={"message":"successful", "number_of_teacher":number_of_teacher, "number_of_admin": number_of_admin, "number_of_student": number_of_student, "number_of_domestic": number_of_domestic, "number_of_security": number_of_security, "number_of_visitor": number_of_visitor, "breaches":br,"ongrounds":ong,"registerclass":rc ,"status":status}
    except Exception as e :
        status  = 400
        resp={"message":f"{e}","status":status}  
        print("ERORR (/Report route)--->",e)
    return jsonify(resp),status

if __name__  =="__main__":
    app.run(debug=True)
    # app.run(host='0.0.0.0',port=5000)