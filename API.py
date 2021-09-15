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

#signup routes ////
@app.route("/Admin/Signup",methods=["POST"])
def a_signup():
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
        admin_number = request.json.get("admin_number")
        if name!= "" and email !="" and password !="" and   id_number  != "":
            # uuid_number = tools()
            # admin_number = uuid_number.id_number_genrator() 
            signup_payload = {
                "name":f"{name}",
                "surname":f"{surname}",
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
            teacher  = mongo.db.admin.insert(signup_payload)
            status = 200
            resp = {"message":"succeessful","status":f"{status}"}       
    except Exception as e:
        status = 400
        resp = {"message":"ERROR on /Admin/Signup","status":f"{status}",}
        print("ERROR:/Admin/Signup-->",e)
    return jsonify(resp),status


@app.route("/Teacher/Signup",methods=["POST"])
def t_signup():
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
        staff_number = request.json.get("staff_number")
        position= request .json.get("position")
        subject= request.json.get("subject")
        register_class = request.json.get("register_class")
        if name!= "" and email !="" and password !="" and   id_number  != "":
            # uuid_number = tools()
            # staff_number = uuid_number.id_number_genrator() 
            signup_payload = {
                "name":f"{name}",
                "surname":f"{surname}",
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
        resp = {"message":"ERROR on /Teacher/Signup","status":f"{status}",}
        print("ERROR:/Teacher/Signup-->",e)
    return jsonify(resp),status


        
@app.route("/Security/Signup",methods=["POST"])
def se_signup():
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
            # uuid_number = tools()
            # staff_number = uuid_number.id_number_genrator() 
            signup_payload = {
                "name":f"{name}",
                "surname":f"{surname}",
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
            teacher  = mongo.db.security.insert(signup_payload)
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
        name = request.json.get("name")
        surname = request.json.get("surname")
        id_number = request.json.get("id_number")
        date_of_birth = request.json.get("date_of_birth")
        email = request.json.get("email")
        phone_number= request.json.get("phone_number")
        address= request.json.get("address")
        password = request.json.get("password")
        staff_number= request.json.get("staff_number")
        position= request .json.get("position")
        job_title = request.json.get("job_title") 
        if name!= "" and email !="" and password !="" and   id_number  != "":
            # uuid_number = tools()
            # staff_number = uuid_number.id_number_genrator() 
            signup_payload = {
                "name":f"{name}",
                "surname":f"{surname}",
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
            teacher  = mongo.db.domestic.insert(signup_payload)
            status = 200
            resp = {"message":"succeessful","status":f"{status}"}       
    except Exception as e:
        status = 400
        resp = {"message":"ERROR on /Domestic/Signup","status":f"{status}",}
        print("ERROR:/Domestic/Signup-->",e)
    return jsonify(resp),status



@app.route("/Student/Signup",methods=["POST"])
def stu_signup():
    print("hello")
    status= 200
    resp ={}
    try:
        name = request.json.get("name")
        print(name)
        surname = request.json.get("surname")
        id_number = request.json.get("id_number")
        date_of_birth = request.json.get("date_of_birth")
        email = request.json.get("email")
        phone_number= request.json.get("phone_number")
        address= request.json.get("address")
        password = request.json.get("password")
        student_number = request.json.get("student_number")
        register_class = request.json.get("register_class")
        subject_combo = request.json.get("subject_combo")
        time_table = request.json.get("time_table")
        guardian_name  = request.json.get("guardian_name")
        guardian_surname = request.json.get("guardian_surname")
        gaurdian_email  = request.json.get(" gaurdian_email")
        gaurdian_phone_number = request.json.get("gaurdian_phone_number")
        
        if name!= "" and email !="" and password !="" and   id_number  != "":
            # uuid_number = tools()
            # student_number = uuid_number.id_number_genrator()
            # print("st-->",student_number) 
            signup_payload = {
                "name":f"{name}",
                "surname":f"{surname}",
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
            print(signup_payload)
            teacher  = mongo.db.student.insert(signup_payload)
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
        name = request.json.get("name")
        surname = request.json.get("surname")
        id_number = request.json.get("id_number")
        date_of_birth = request.json.get("date_of_birth")
        email = request.json.get("email")
        phone_number= request.json.get("phone_number")
        address= request.json.get("address")
        password = request.json.get("password")
        purpose_of_visit= request.json.get("purpose_of_visit")
        time_in = request.json.get("time_in") 
        time_out = request.json.get("time_out") 
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
                "password":f"{password}",
                "visitor_number":f"{visitor_number}",
                "purpose_of_visit":f"{purpose_of_visit}",
                "time_in":f"{time_in}",
                "time_out":f"{time_out}",
                "acess_level":0,
                "token":[]
            }
            print(signup_payload)
            teacher  = mongo.db.visitor.insert(signup_payload)
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
            admin = mongo.db.teacher.find_one({ "admin_number":f"{user_number}"})
            student = mongo.db.student.find_one({"student_number":f"{user_number}"})
            domestic = mongo.db.domestic.find_one({"staff_number":f"{user_number}"})
            security = mongo.db.security.find_one({"staff_number":f"{user_number}"})
            visitor = mongo.db.visitor.find_one({"visitor_number":f"{user_number}"})
            print(parse_json(domestic))
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
            # else:
            #     status = 400
            #     resp = {"message":"Your does not exsist","status":status,"token":"down"}
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
            # else:
            #     status = 400
            #     resp = {"message":"Your does not exsist","status":status,"token":"down"}
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
            # else:
            #     status = 400
            #     resp = {"message":"Your does not exsist","status":status,"token":"down"}
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
            # else:
            #     status = 400
            #     resp = {"message":"Your does not exsist","status":status,"token":"down"}
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
            # else:
            #     status = 400
            #     resp = {"message":"Your does not exsist","status":status,"token":"down"}
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
            # else:
            #     status = 400
            #     resp = {"message":"Your does not exsist","status":status,"token":"down"}
        else:
            print("missing credential on sign up ")
            status = 400
            resp = {"message":"ERROR on /User/login missing credential","status":f"{status}",}
    except Exception as e :
        status = 400
        resp = {"message":"ERROR on /User/login","status":f"{status}",}
        print("ERROR:/User/login-->",e)
    return jsonify(resp),status

@app.route("/generate/token",methods=["POST"])
def generate_token():
    status  = 200
    resp= {}
    try:
        #user_number is not SA id number its user specific number 
        data = request.json_get("data")
        user_number = data["data"]["user_number"]
        user_type = data["data"]["user_type"]
        print(user_number,user_type)
        if user_number != "" and user_type != "":

            if user_type == "staff":
                teacher = mongo.db.teacher.find_one({"staff_number":f"{user_number}"})
                security = mongo.db.security.find_one({"staff_number":f"{user_number}"})
                domestic = mongo.db.domestic.find_one({"staff_number":f"{user_number}"})
                print(parse_json(teacher))
                print(parse_json(security))
                print(parse_json(domestic))

                if parse_json(teacher) != None:
                    data = parse_json(teacher)
                    qr = tools()
                    token = qr.generate_token(data,user_number)
                    email = data["email"]
                    name = data["name"] 
                    qr.emailing_services(email,name,user_number,"qr_code",token)
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
                    qr.emailing_services(email,name,user_number,"qr_code",token)
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
                    qr.emailing_services(email,name,user_number,"qr_code",token)
                    status = 200 
                    resp = {"message":"Toke sent","status":f"{status}"}
                else :
                    status = 400 
                    token = resp = {"message":"User not found","status":f"{status}"}

            elif user_type == "student":
                student = mongo.db.student.find_one({"student_number":f"{user_number}"})
                if  parse_json(student) != None:
                    qr = tools()
                    token = qr.generate_token(student,user_number)
                    email = student["email"]
                    name = student["name"] 
                    qr.emailing_services(email,name,"qr_code",token)
                    status = 200 
                    resp = {"message":"Toke sent","status":f"{status}"}
                else :
                    status = 400 
                    resp = {"message":"User not found","status":f"{status}"}
            
            elif user_type == "vistor":
                visitor = mongo.db.visitor.find_one({"visitor_number":f"{user_number}"})
                if parse_json(visitor)  != None:
                    data = parse_json(visitor)
                    qr = tools()
                    token = qr.generate_token(data,user_number)
                    email = data["email"]
                    name = data["name"] 
                    qr.emailing_services(email,name,user_number,"qr_code",token)
                    status = 200 
                    resp = {"message":"Toke sent","status":f"{status}"}
                else :
                    status = 400 
                    resp = {"message":"User not found","status":f"{status}"}

            elif user_type  == "admin":
                admin = mongo.db.teacher.find_one({ "admin_number":f"{user_number}"})
                if parse_json(admin) != []:
                    data = parse_json(admin)
                    qr = tools()
                    token = qr.generate_token(data,user_number)
                    email = data["email"]
                    name = data["name"] 
                    qr.emailing_services(email,name,user_number,"qr_code",token)
                    status = 200 
                    resp = {"message":"Toke sent","status":f"{status}"}
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

@app.route("/retrieve/User",methods=["POST","GET"])
def get_patient_list():
    status = 200
    resp  = {}
    try:
        database_name = request.json.get("database_name")
        if database_name != "":
            patients = mongo.db.database_name
            response  = patients.find()
            if response != None:
                status = 200
                patients_array =[]
                for i in response:
                    patients_array.append(i)
                return_response = parse_json(patients_array)
                resp = {"response":return_response,"message":"patients retieved","status":status}
        else:
            status  = 400
            resp={"message":"missing database name to retrieve from","status":status}
    except Exception as e :
        status  = 400
        resp={"message":f"{e}","status":status}  
        print("ERORR (patients retrieve route)--->",e)
    return jsonify(resp),status
#############################################################################
#########################################################
#############################################
#Delete user area
@app.route("/delete/user",methods=["DELETE"])
def user_delete():
    status = 200
    resp  ={}
    try:
        data = request.json_get("data")
        name = data["data"]["name"]
        surname = data["data"]["surname"]
        user_number= data["data"]["user_number"]
        user_type =data["data"]["user_type"]

        if name != "" and surname !="" and user_number != "" and user_type != "":
            database  = mongo.db.patients.find_one({"name":f"{patient_name}","surname":f"{patient_surnmae}","id_number":f"{patient_id_number}"})
            if database != None:
                print("user is in database ")
                patient_database_id  = patient_in_database["_id"]
                print(patient_database_id)
                if patient_database_id != "":
                    mongo.db.patients.delete_one({"_id":f"{patient_database_id}"})
                    status =200
                    resp = {"message":"User profile has been deleted","status":status}
                else:
                    status =400
                    resp = {"message":"Could not get User _id ","status":status}

            else:
                status =400
                resp = {"message":"There is no patient in the database with these credentials","status":status}
        else:
            status = 500
            resp = {"message":"Missing credential to make query","status":status}
    except Exception as e:
        status  = 400
        resp={"message":f"{e}","status":status}  
        print("ERORR (/delete/user route)--->",e)
    return jsonify(resp),status



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
            admin = mongo.db.teacher.find_one({ "email":f"{email}"})
            student = mongo.db.student.find_one({"email":f"{email}"})
            domestic = mongo.db.domestic.find_one({"email":f"{email}"})
            security = mongo.db.security.find_one({"email":f"{email}"})
            visitor = mongo.db.visitor.find_one({"email":f"{email}"})
            print(parse_json(domestic))
            if parse_json(teacher) != None:
                print("Teacher")
                data = parse_json(teacher)
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
        data = request.json_get("data")
        verification_number = data["data"]["verification_number"]
        if verification_number != "":
            forgort_password_user = mongo.db.forgot.find_one({"verification_number":f"{verification_number}"})
            if parson_json(forgort_password_user) != None:
                data  = parson_json(forgort_password_user) 
                database_veri_num = data["verification_number"]
                if verification_number == database_veri_num:
                    email = data["email"]
                    name = data["name"]
                    user_number  = data["user_number"] 
                    password  = data["password"]
                    q1 = tools()
                    q1.emailing_services(email,name,user_number,"forgot_password_send","","",number,password)
                    status = 200
                    resp = {"message":"success","status":status}
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

########################################################################
########################################################
#########################################
#QR code checking area

# @app.route("/QR/check", methods=["POST"])

if __name__  =="__main__":
    app.run(debug=True)
    # app.run(host='0.0.0.0',port=5000)