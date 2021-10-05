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
        if name!= "" and email !="" and password !="" and   id_number  != "": 
            qr = tools()
            token = qr.generate_token(data,admin_number)
            image_path  = token[2]
            db = mongo_conn()
            file_name = "test1.png"
            file_data = open(image_path,"rb")
            data = file_data.read()
            fs  = gridfs.GridFS(db)
            personal_qr = fs.put(data ,filename=file_name)
            #delete image
            
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
                "token":personal_qr
            }
            mongo.db.admin.insert_one(signup_payload)
            q1= tools()
            q1.emailing_services(email,name,admin_number,"signup",image_path,"","","")
            status = 200
            resp = {"message":"succeessful","status":f"{status}"}  
                
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
        if name!= "" and email !="" and password !="" and   id_number  != "":
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
                "token":[]
            }
            teacher  = mongo.db.teacher.insert_one(signup_payload)
            q1= tools()
            q1.emailing_services(email,name,staff_number,"signup","","","","")
            status = 200
            resp = {"message":"succeessful","status":f"{status}"}       
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
        print(staff_number)
        if name!= "" and email !="" and password !="" and   id_number  != "":
        
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
                "token":[]
            }
            mongo.db.security.insert_one(signup_payload)
            q1= tools()
            q1.emailing_services(email,name,staff_number,"signup","","","","")
            status = 200
            resp = {"message":"succeessful","status":f"{status}"}       
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
        if name!= "" and email !="" and password !="" and   id_number  != "":
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
                "token":[]
            }
            mongo.db.domestic.insert_one(signup_payload)
            q1= tools()
            q1.emailing_services(email,name,staff_number,"signup","","","","")
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
        
        if name!= "" and email !="" and password !="" and   id_number  != "":
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
                "pg_phone_number ":f"{pg_phone_number}",
                "acess_level":0,
                "token":[]
            }
            mongo.db.student.insert_one(signup_payload)
            q1= tools()
            q1.emailing_services(email,name,student_number,"signup","","","","")
            q1.emailing_services(pg_email,pg_name,"","pg_signup","","","","")
            status = 200
            resp = {"message":"succeessful","status":f"{status}"}       
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
        if name!= "" and email !="" and password !="" and   id_number  != "":
            uuid_number = tools()
            visitor_number = uuid_number.id_number_genrator() 
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
                "token":[]
            }
            print(signup_payload)
            mongo.db.visitor.insert_one(signup_payload)
            q1= tools()
            q1.emailing_services(email,name,visitor_number,"signup","","","","")
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
            print(parse_json(admin))
            print(parse_json(teacher))
            if parse_json(teacher) != None:
                print("Teacher")
                data = parse_json(teacher)
                database_password = data["password"]   
                if database_password  == password:
                    print("welcome user")
                    status = 200
                    resp = {"message":"Welcome","status":status,"token":"active","user":data,"type_user":"teacher"}
                else:
                    print("Password is incorrect")
                    status = 400
                    resp = {"message":"Fail in check password","status":status}  
            if parse_json(admin) != None:
                print("Admin")
                data = parse_json(admin)
                database_password = data["password"]   
                if database_password  == password:
                    print("welcome user")
                    status = 200
                    resp = {"message":"Welcome","status":status,"token":"active","user":data,"type_user":"admin"}
                else:
                    print("Password is incorrect")
                    status = 400
                    resp = {"message":"Fail in check password","status":status} 
            if parse_json(student) != None:
                print("Student")
                data = parse_json(student)
                database_password = data["password"]   
                if database_password  == password:
                    print("welcome user")
                    status = 200
                    resp = {"message":"Welcome","status":status,"token":"active","user":data,"type_user":"student"}
                else:
                    print("Password is incorrect")
                    status = 400
                    resp = {"message":"Fail in check password","status":status} 
            if parse_json(security) != None:
                print("Security")
                data = parse_json(security)
                database_password = data["password"]   
                if database_password  == password:
                    print("welcome user")
                    status = 200
                    resp = {"message":"Welcome","status":status,"token":"active","user":data,"type_user":"security"}
                else:
                    print("Password is incorrect")
                    status = 400
                    resp = {"message":"Fail in check password","status":status}  
            if parse_json(domestic) != None:
                print("Domestic")
                data = parse_json(domestic)
                database_password = data["password"]   
                if database_password  == password:
                    print("welcome user")
                    status = 200
                    resp = {"message":"Welcome","status":status,"token":"active","user":data,"type_user":"domestic"}
                else:
                    print("Password is incorrect")
                    status = 400
                    resp = {"message":"Fail in check password","status":status}  
            if parse_json(visitor) != None:
                print("Vistor")
                data = parse_json(visitor)
                database_password = data["password"]   
                if database_password  == password:
                    print("welcome user")
                    status = 200
                    resp = {"message":"Welcome","status":status,"token":"active","user":data}
                else:
                    print("Password is incorrect")
                    status = 400
                    resp = {"message":"Fail in check password","status":status}  
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
            token = qr.genrate_grounds_qr() 
            security  = mongo.db.security.find_one({"staff_number":f"{user_number}"})
            if parse_json(security) != None:
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
            if parse_json(teacher) != None:
                print("Teacher")
                data = parse_json(teacher)
                name = data["name"]
                surname =data["surname"]
                user_number = data["staff_number"]
                email= data["email"]
                qr = data["token"]
                on_grounds_payload  ={
                        "name":f"{name}",
                        "surname":f"{surname}",
                        "user_number":f"{user_number}",
                        "email":f"{email}",
                        "token":qr
                    }
        
                mongo.db.ongrounds.insert_one(on_grounds_payload)
                status  = 200
                resp ={"message":"successful","status":status}
            if parse_json(admin) != None:
                print("Admin")
                data = parse_json(admin)
                name = data["name"]
                surname =data["surname"]
                user_number = data["admin_number"]
                email= data["email"]
                qr = data["token"]["$oid"]
                on_grounds_payload  ={
                        "name":f"{name}",
                        "surname":f"{surname}",
                        "user_number":f"{user_number}",
                        "email":f"{email}",
                        "token":qr
                    }
        
                mongo.db.ongrounds.insert_one(on_grounds_payload)
                status  = 200
                resp ={"message":"successful","status":status}
            if parse_json(student) != None:
                print("Student")
                data = parse_json(student)
                name = data["name"]
                surname =data["surname"]
                user_number = data["staff_number"]
                email= data["pg_email"]

                qr= data["token"]
                on_grounds_payload  ={
                        "name":f"{name}",
                        "surname":f"{surname}",
                        "user_number":f"{user_number}",
                        "email":f"{email}",
                        "token":qr
                    }
        
                mongo.db.ongrounds.insert_one(on_grounds_payload)
                status  = 200
                resp ={"message":"successful","status":status} 
            if parse_json(security) != None:
                print("Security")
                data = parse_json(security)
                name = data["name"]
                surname =data["surname"]
                user_number = data["staff_number"]
                email= data["email"]

                qr= data["token"]
                on_grounds_payload  ={
                        "name":f"{name}",
                        "surname":f"{surname}",
                        "user_number":f"{user_number}",
                        "email":f"{email}",
                        "token":qr
                    }
        
                mongo.db.ongrounds.insert_one(on_grounds_payload)
                status  = 200
                resp ={"message":"successful","status":status}  
            if parse_json(domestic) != None:
                print("Domestic")
                data = parse_json(domestic)
                name = data["name"]
                surname =data["surname"]
                user_number = data["staff_number"]
                email= data["email"]

                qr= data["token"]
                on_grounds_payload  ={
                        "name":f"{name}",
                        "surname":f"{surname}",
                        "user_number":f"{user_number}",
                        "email":f"{email}",
                        "token":qr
                    }
        
                mongo.db.ongrounds.insert_one(on_grounds_payload)
                status  = 200
                resp ={"message":"successful","status":status}  
            if parse_json(visitor) != None:
                print("Vistor")
                data = parse_json(visitor)
                name = data["name"]
                surname =data["surname"]
                user_number = data["visitor_number"]
                email= data["email"]

                qr= data["token"]
                on_grounds_payload  ={
                        "name":f"{name}",
                        "surname":f"{surname}",
                        "user_number":f"{user_number}",
                        "email":f"{email}",
                        "token":qr
                    }
        
                mongo.db.ongrounds.insert_one(on_grounds_payload)
                status  = 200
                resp ={"message":"successful","status":status} 
        else :
            status = 200 
            resp  = {"message":"missing credential", "status":status}
    except Exception as e :
        status = 400
        resp = {"message":"ERROR on /Enter/Grounds","status":f"{status}",}
        print("ERROR:/Enter/Grounds->",e)
    return jsonify(resp),status
@app.route("/Verify/Personal/QR",methods = ["GET"])
def generate_personal_qr():
    status= 200
    resp = {}
    try:
        data= request.get_json("data")
        user_numer = data["data"]["user_number"]
        if user_number != "":
            print("helo")

        else:
            status  = 400
            resp = {"message":"missing credential","status":status}
    except Exception as e:
        status = 400
        resp = {"message":"ERROR on /Enter/Grounds","status":f"{status}",}
        print("ERROR:/Enter/Grounds->",e)
    return jsonify(resp),status

@app.route("/Verifiy/Token", methods=["POST"])
def verify():
    status  = 200
    resp = {}
    try :
        data  = request.get_json("data")
        user_number  = data["data"]["user_number"]
        if user_number != "":
            qr = tools()
            qr_data= qr.retreive_qr_info(token)
            qr_user_number = qr_data[1]
            qr_creation_date =qr_data[2] 
        
        if user_number == qr_user_number :
            print("working")

        if user_number != "" and token != "":
            if user_type == "staff":
                teacher = mongo.db.teacher.find_one({"staff_number":f"{user_number}"})
                security = mongo.db.security.find_one({"staff_number":f"{user_number}"})
                domestic = mongo.db.domestic.find_one({"staff_number":f"{user_number}"})
                if parse_json(teacher) != None:
                    data = parse_json(teacher)
                    token_list = data["token"]
                    current= len(token_list)
                    
                    qr = tools()
                    qr_data= qr.retreive_qr_info(token)
                    qr_user_number = qr_data[1]
                    qr_creation_date =qr_data[2] 
                    email = data["email"]
                    name = data["name"] 
                    qr.emailing_services(email,name,user_number,"qr_code",token,"","","")
                    status = 200 
                    resp = {"message":"Toke sent","status":f"{status}"}
                else :
                    status = 400 
                    resp = {"message":"User not found","status":f"{status}"}
                
                if parse_json(security) != None:
                    data = parse_json(security)
                    qr = tools()
                    token = qr.generate_token(data,user_number)
                    email = data["email"]
                    name = data["name"] 
                    qr.emailing_services(email,name,user_number,"qr_code",token,"","","")
                    status = 200 
                    resp = {"message":"Toke sent","status":f"{status}"}
                else :
                    status = 400 
                    resp = {"message":"User not found","status":f"{status}"}

                if parse_json(domestic) != None:
                    print("Domestic")
                    data = parse_json(domestic)
                    qr = tools()
                    print(data)
                    token = qr.generate_token(data,user_number)
                    email = data["email"]
                    name = data["name"] 
                    qr.emailing_services(email,name,user_number,"qr_code",token,"","","")
                    status = 200 
                    resp = {"message":"Toke sent","status":f"{status}"}
                else :
                    status = 400 
                    token = resp = {"message":"User not found","status":f"{status}"}



        else:
            status  = 400 
            resp = {"message":"misssing credentials","status":status} 
    except Exception as e :
        status = 400
        resp = {"message":"ERROR on /Verifiy/Token","status":f"{status}",}
        print("ERROR:/Verifiy/Token-->",e)
    return jsonify(resp),status


@app.route("/Generate/Class/RegisterQR",methods=["POST"])
def generate_token():
    status  = 200
    resp= {}
    try:
        #user_number is not SA id number its user specific number 
        data = request.get_json("data")
        user_number = data["data"]["user_number"]
        print(user_number,user_type)
        if user_number != "" :
                teacher = mongo.db.teacher.find_one({"staff_number":f"{user_number}"})
                if parse_json(teacher) != None:
                    data = parse_json(teacher)
                    name = data["name"]
                    register_class = data["register_class"]
                    subject= data["subject"]
                    qr = tools()
                    token = qr.generate_token(name,user_number)
                    email = data["email"]
                    name = data["name"] 
                    image = token[0]
                    log = token[1]
                    qr.emailing_services(email,name,user_number,"qr_code",image,"","","")
                    # #adding token record to database
                    # teacher = mongo.db.teacher.find_one({"staff_number":f"{user_number}"})
                    # if parse_json(teacher) != []:
                    #     user = parse_json(teacher)
                    #     #token adding
                    #     array =[]
                    #     for i in user["token"]:
                    #         array.append(i)
                    #     array.append(log)
                    #     #saving
                    #     mongo.db.teacher.update_one({"staff_number":f"{user_number}"},{ "$set": { "token": f"{array}" } })
                    #     status = 200 
                    #     resp = {"message":"Toke sent","status":f"{status}"}
                else :
                    status = 400 
                    resp = {"message":"User not found","status":f"{status}"}
               

    except Exception as e :
        status = 400
        resp = {"message":"ERROR on /generate/token","status":f"{status}",}
        print("ERROR:/generate/token-->",e)
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
            if response != None:
                print("working d")
                status = 200
                return_response = parse_json(response)
                resp = {"response":return_response,"message":"user retieved","status":status}
        elif database_name == "teacher":
            users = mongo.db.teacher
            response  = users.find()
            if response != None:
                print("working t")
                status = 200
                return_response = parse_json(response)
                resp = {"response":return_response,"message":"user retieved","status":status}

        elif database_name == "student":
            users = mongo.db.student
            response  = users.find()
            if response != None:
                print("working st")
                status = 200
                return_response = parse_json(response)
                resp = {"response":return_response,"message":"user retieved","status":status}

        elif database_name == "security":
            users = mongo.db.security
            response  = users.find()
            if response != None:
                print("working se")
                status = 200
                return_response = parse_json(response)
                resp = {"response":return_response,"message":"user retieved","status":status}

        elif database_name == "visitor":
            users = mongo.db.visitor
            response  = users.find()
            if response != None:
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
                if response != None:
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
                if response != None:
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
                if response != None:
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
                if response != None:
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
                if response != None:
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

@app.route("/Get/User",methods=["GET"])
def get_user():
    status = 200
    resp = {}
    try:
        data= request.get_json("data")
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
            if parse_json(teacher) != None:
                print("Teacher")
                data = parse_json(teacher) 
                status= 200
                resp = {"status":status,"token":"active","user":data}
                
            if parse_json(admin) != None:
                print("Admin")
                data = parse_json(admin)
                status= 200
                resp = {"status":status,"token":"active","user":data}
            if parse_json(student) != None:
                print("Student")
                data = parse_json(student)
                status= 200
                resp = {"status":status,"token":"active","user":data}
            if parse_json(security) != None:
                print("Security")
                data = parse_json(security)
                status= 200
                resp = {"status":status,"token":"active","user":data}
            if parse_json(domestic) != None:
                print("Domestic")
                data = parse_json(domestic)
                status= 200
                resp = {"status":status,"token":"active","user":data}
            if parse_json(visitor) != None:
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
        if new_crediatials != {}  and user_number != "":
            teacher = mongo.db.teacher.find_one({"staff_number":f"{user_number}"})
            admin = mongo.db.admin.find_one({ "admin_number":f"{user_number}"})
            student = mongo.db.student.find_one({"student_number":f"{user_number}"})
            domestic = mongo.db.domestic.find_one({"staff_number":f"{user_number}"})
            security = mongo.db.security.find_one({"staff_number":f"{user_number}"})
            visitor = mongo.db.visitor.find_one({"visitor_number":f"{user_number}"})
            if parse_json(teacher) != None:
                print("Teacher")
                name = new_crediatials["data"]["name"]
                surname = new_crediatials["data"]["surname"]
                id_number = new_crediatials["data"]["id_number"]
                date_of_birth = new_crediatials["data"]["date_of_birth"]
                email = new_crediatials["data"]["email"]
                phone_number= new_crediatials["data"]["phone_number"]
                address= new_crediatials["data"]["address"]
                city= new_crediatials["data"]["city"]
                pcode= new_crediatials["data"]["pcode"]
                password = new_crediatials["data"]["password"]
                staff_number = new_crediatials["data"]["staff_number"]
                position= new_crediatials["data"]["position"]
                subject= new_crediatials["data"]["subject"]
                register_class = new_crediatials["data"]["register_class"]
            
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
            if parse_json(admin) != None:
                    print("Admin")
                    name = new_crediatials["data"]["name"]
                    surname = new_crediatials["data"]["surname"]
                    id_number = new_crediatials["data"]["id_number"]
                    date_of_birth = new_crediatials["data"]["date_of_birth"]
                    email = new_crediatials["data"]["email"]
                    phone_number= new_crediatials["data"]["phone_number"]
                    address= new_crediatials["data"]["address"]
                    city= new_crediatials["data"]["city"]
                    pcode= new_crediatials["data"]["pcode"]
                    password = new_crediatials["data"]["password"]
                    admin_number = new_crediatials["data"]["admin_number"]
                    

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
            if parse_json(student) != None:
                    print("Student")
                    name = new_crediatials["data"]["name"]
                    surname = new_crediatials["data"]["surname"]
                    id_number = new_crediatials["data"]["id_number"]
                    date_of_birth = new_crediatials["data"]["date_of_birth"]
                    email = new_crediatials["data"]["email"]
                    phone_number= new_crediatials["data"]["phone_number"]
                    address= new_crediatials["data"]["address"]
                    city= new_crediatials["data"]["city"]
                    pcode= new_crediatials["data"]["pcode"]
                    password = new_crediatials["data"]["password"]
                    student_number = new_crediatials["data"]["student_number"]
                    register_class = new_crediatials["data"]["register_class"]
                    pg_name = new_crediatials["data"]["pg_name"]
                    pg_surname= new_crediatials["data"]["pg_surname"]
                    pg_email  = new_crediatials["data"]["pg_email"]
                    pg_id_number =new_crediatials["data"]["pg_id_number"]
                    pg_phone_number = new_crediatials["data"]["pg_cnum"]

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
                    "pg_phone_number ":f"{pg_phone_number}" }
                     }
                    mongo.db.student.update_one({"staff_number":f"{user_number}"},newvalues)
                    status = 200
                    resp ={"message":"successful","token":"true" ,"status":status} 
            if parse_json(security) != None:
                    print("Security")
                    name = new_crediatials["data"]["name"]
                    surname = new_crediatials["data"]["surname"]
                    id_number = new_crediatials["data"]["id_number"]
                    date_of_birth = new_crediatials["data"]["date_of_birth"]
                    email = new_crediatials["data"]["email"]
                    phone_number= new_crediatials["data"]["phone_number"]
                    address= new_crediatials["data"]["address"]
                    city= new_crediatials["data"]["city"]
                    pcode= new_crediatials["data"]["pcode"]
                    password = new_crediatials["data"]["password"]
                    staff_number = new_crediatials["data"]["staff_number"]
                    position= new_crediatials["data"]["position"]
                    petrol_sector = new_crediatials["data"]["petrol_sector"]
                  

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
            if parse_json(domestic) != None:
                    print("Domestic")
                    name = new_crediatials["data"]["name"]
                    surname = new_crediatials["data"]["surname"]
                    id_number = new_crediatials["data"]["id_number"]
                    date_of_birth = new_crediatials["data"]["date_of_birth"]
                    email = new_crediatials["data"]["email"]
                    phone_number= new_crediatials["data"]["phone_number"]
                    address= new_crediatials["data"]["address"]
                    city= new_crediatials["data"]["city"]
                    pcode= new_crediatials["data"]["pcode"]
                    password = new_crediatials["data"]["password"]
                    staff_number = new_crediatials["data"]["staff_number"]
                    position= new_crediatials["data"]["position"]
                    job_title  = new_crediatials["data"]["job_title"]

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
            if parse_json(visitor) != None:
                    print("Vistor")
                    name = new_crediatials["data"]["name"]
                    surname = new_crediatials["data"]["surname"]
                    id_number = new_crediatials["data"]["id_number"]
                    date_of_birth = new_crediatials["data"]["date_of_birth"]
                    email = new_crediatials["data"]["email"]
                    phone_number= new_crediatials["data"]["phone_number"]
                    address= new_crediatials["data"]["address"]
                    city= new_crediatials["data"]["city"]
                    pcode= new_crediatials["data"]["pcode"]
                    password = new_crediatials["data"]["password"]
                    purpose_of_visit  = new_crediatials["data"]["purpose_of_visit"]

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
        print("ERORR (/delete/user route)--->",e)
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
            if parse_json(teacher) != None:
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

            if parse_json(admin) != None:
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

            if parse_json(student) != None:
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

            if parse_json(security) != None:
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

            if parse_json(domestic) != None:
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

            if parse_json(visitor) != None:
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
            if parse_json(forgort_password_user) != None:
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
#QR code checking area
# student add to attedndence 
@app.route("/add/attendence",methods=["POST"])
def register_add():
    status =200
    resp = {}
    try:
        data= request.get_json("data") 
        if data != None:
            resp = {"message":"working "}
            status = 200 
    except Exception as e :
        status  = 400
        resp={"message":f"{e}","status":status}  
        print("ERORR (/add/attendence route)--->",e)
    return jsonify(resp),status
# @app.route("/QR/check", methods=["POST"])



##############################################################
###############################################################
##################################################################
###############################################
# BREACH ALARM section 

@app.route("/breachalarm",methods= ["POST"])
def make_alarm():
    status = 200
    resp = {}
    try:
        data = request.get_json("data")
        name = data["data"]["name"]
        surname = data["data"]["surname"]
        id_number = data["data"]["id_number"]
        password = data["data"]["password"]
        email = data["data"]["email"]
        quadrant = data["data"]["quadrant"]
        breach_type = data["data"]["breach type"]

        if name!= "" and email !="" and password !="" and   id_number  != "":
            breachAlarm_payload = {
                "name":f"{name}",
                "surname":f"{surname}",
                "id_number":f"{id_number}",
                "password": f"{password}",
                "email":f"{email}",
                "phone_number":f"{quadrant}",
                "breach type":f"{breach_type}"
            }

    except Exception as e :
        status  = 400
        resp={"message":f"{e}","status":status}  
        print("ERORR (/breachalarm route)--->",e)
    return jsonify(resp),status

@app.route("/breachalarm/check",methods= ["GET"])
def check_alarm():
    status = 200
    resp = {}
    try:
        data = request.get_json("data")
        database_name = data["data"]["database_name"]
        if database_name == "breach_alarm":
            users = mongo.db.breach_alarm
            response  = users.find()
            if response != None:
                print("working d")
                status = 200
                return_response = parse_json(response)
                resp = {"response":return_response,"message":"Report found","status":status}

            else:
                status  = 400
                resp={"message":f"{e}","status":status}  
                print("ERORR (/breachalarm/check route)--->",e)
                return jsonify(resp),status
            
        else:
            print("no report found for that database")

    except Exception as e :
        status  = 400
        resp={"message":f"{e}","status":status}  
        print("ERORR (/breachalarm/check route)--->",e)
    return jsonify(resp),status

@app.route("/breachalarm/delete",methods= ["DELETE"])
def delete_alarm():
    status = 200
    resp = {}
    try:
        data = request.get_json("data")
        name = data["data"]["name"]
        surname = data["data"]["surname"]
        user_number= data["data"]["user_number"]
        user_type =data["data"]["user_type"]

        if name != "" and surname !="" and user_number != "" and user_type != "":
            database  = mongo.db.patients.find_one({"name":f"{user_name}","surname":f"{user_surnmae}","id_number":f"{user_id_number}"})
            if database_name != "breach_alarm":
                print("user is in database ")
                user_database_id  = patient_in_database["_id"]
                print(user_database_id)
                if user_database_id != "":
                    mongo.db.patients.delete_one({"_id":f"{patient_database_id}"})
                    status =200
                    resp = {"message":"User profile has been deleted","status":status}
                else:
                    status =400
                    resp = {"message":"Could not get User _id ","status":status}

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
            print(name,message,email)
            if name != "" and message  !="" and  email != "":
                payload  ={
                        "name":f"{name}",
                        "email":f"{email}",
                        "message":f"{message}"
                    }
                print(payload)
                mongo.db.messages.insert(payload)
                q1= tools()
                q1.emailing_services(email,name,"","message","","","","")
                status = 200
                resp = {"message":"successful", "status":status}
                # mongo.db.craeteCollection(messages)
                # number = mongo.db.messages.count()
                # meassage_number = int(number) + 1 
                # if (number != null):
                #     payload  ={
                #         "name":f"{name}",
                #         "email":f"{email}",
                #         "message":f"{message}"
                #     }
                #     mongo.db.messages.insert(payload)
                #     q1= tools()
                #     q1.emailing_services(email,name,"","message","","","","")
                #     status = 200
                #     resp = {"message":"successful", "status":status}

                # else :
                #     print("collection count flail please check")   

        else:
            status = 400
            resp = {"message": "message was not added"}
    except Exception as e:
        status  = 400
        resp={"message":f"{e}","status":status}  
        print("ERORR (/Leave/comment route)--->",e)
    return jsonify(resp),status

@app.route ("/Delete/Messages",methods=["Delete"])
def delete_messages():
    status = 200
    resp ={}
    try:
        data = request.get_json("data")
        messsage_number  = data["data"]["message_number"]
        if message_number != "":
            messages = mongo.db.messages.find_one({"message_number":f"{message_number}"})
            if messages != None:
                status = 200
                return_response = parse_json(messages)
                user_database_id  = return_response["_id"]
                if user_database_id != "":
                    mongo.db.visitor.delete_one({"_id":f"{user_database_id}"})
                    status =200
                    resp = {"message":"user profile has been deleted","status":status}
                else:
                    status =400
                    resp = {"message":"Could not get messsage _id ","status":status}
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
            message_number 
            response_message 
        else:
            status=400
            resp = {"message":"no response recieved ","status":status}
        
    except Exception as e:
        status  = 400
        resp={"message":f"{e}","status":status}  
        print("ERORR (/Retrieve/Messages route)--->",e)

@app.route("/Retrieve/Messages", methods=["GET"])
def messages():
    status  = 200
    resp = {}
    try:
        messages_r = mongo.db.messages.find()
        if messages_r != None :
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
    

if __name__  =="__main__":
    app.run(debug=True)
    # app.run(host='0.0.0.0',port=5000)