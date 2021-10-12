import random
import string
import smtplib
import os
import json
import imghdr
from email.message import EmailMessage
from datetime import datetime
import uuid
#QR module import
import qrcode
from PIL import Image
import cv2 as cv

def find_all(name, path):
    result = 0
    for root, dirs, files in os.walk(path):
        if name in files:
            result = 1
    return result
class tools :
        def id_number_genrator(self):
            id_number = uuid.uuid1()
            print(id_number)
            return id_number

        def purge_qr_codes(self):
            try:
                files =[] 
                for directory ,subdirectories,filenames in os.walk("resources/PQR/visitor_user"):
                    for filename in filenames:
                        files.append(filename)
                    print(files)
                for i in range (0,len(files)):
                    os.remove("resources/PQR/visitor_user/"+files[i])

                files2 =[] 
                for directory ,subdirectories,filenames in os.walk("resources/PQR/teacher_user"):
                    for filename in filenames:
                        files2.append(filename)
                for i in range (0,len(files2)):
                    os.remove("resources/PQR/teacher_user/"+files2[i])
                    

                files3 =[] 
                for directory ,subdirectories,filenames in os.walk("resources/PQR/domestic_user"):
                    for filename in filenames:
                        files3.append(filename)
                for i in range (0,len(files3)):
                    os.remove("resources/PQR/domestic_user/"+files3[i])


                files4 =[] 
                for directory ,subdirectories,filenames in os.walk("resources/PQR/security_user"):
                    for filename in filenames:
                        files4.append(filename)
                for i in range (0,len(files4)):
                    os.remove("resources/PQR/security_user/"+files4[i])

                files5 =[] 
                for directory ,subdirectories,filenames in os.walk("resources/PQR/student_user"):
                    for filename in filenames:
                        files5.append(filename)
                for i in range (0,len(files5)):
                    os.remove("resources/PQR/student_user/"+files5[i])

                files6 =[] 
                for directory ,subdirectories,filenames in os.walk("resources/PQR/admin_user"):
                    for filename in filenames:
                        files6.append(filename)
                for i in range (0,len(files6)):
                    os.remove("resources/PQR/admin_user/"+files6[i])
            except Exception as e :
                print("[purge_qr_codes] purge_qr_codes() error:",e)
                return 0
            return 1
            
        def retrieve(self,users,number_of_users,type_alram):
            print("working")
            print(number_of_users)
            try:
                array_of_emails=[]
                for i in users:
                    array_of_emails.append(i["email"])
                for i in range(0,number_of_users):
                    email_address  ="dummyjackson8@gmail.com"
                    email_password  ="dummy101@1"      
                    email_recieve = (array_of_emails[i])
                   
                    msg = EmailMessage()
                    msg['Subject'] = 'Security Breach'
                    msg['From'] = email_address
                    msg['To']= email_recieve
                    msg.add_alternative(f"""
                            <!DOCTYPE html>
                            <html>
                                <body>
                                    <h1 style ="color:#ff0000;">Security Breach</h1> 
                                    <h2 style ="color:#ff0000;">{type_alram}</h2>
                                    <p>There has been a breach.</p>
                                    <p>This email has been sent to inform you that a breach of the type above has occured on shool campus with has be idetified as a danger to persons of this facility</p>
                                    <p>Please stand by for instruction and make plans to leave school grounds after evcuation</p>
                                    <p style ="color:#ff0000;">Please parents make plan to fecth your children</p>
                                    <p>Please  feel safe under Salus</p>
                                    <p> We care about your well being </p>
                                    <p>Yours sincerly</p>
                                    <p>The Salus team</p>
                                </body>
                            </html>
                            """,subtype= "html")                    
                    files = ["saluswithname.jpg"]
                    for images in files:
                        with open(f"{images}","rb") as image :
                            file_data = image.read()
                            file_type = imghdr.what(image.name)
                            file_name= image.name
                            msg.add_attachment(file_data,maintype="image",subtype=file_type,filename =file_name) 
                    with smtplib.SMTP_SSL("smtp.gmail.com" ,465) as smtp:
                        smtp.login(email_address,email_password)
                        smtp.send_message(msg)
            except Exception as e :
                 print("[retrieve] retrieve() error:",e)
        def generate_token(self,name,user_number,user_type):
            try:
                path = ""
                payload_image= f"{name},{user_number};{user_type}"
                qr = qrcode.QRCode(
                        version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_H,
                        box_size=10,
                        border=4,
                    )
                qr.add_data(payload_image)
                qr.make(fit=True)
                image = qr.make_image(fill_color="black", back_color="white").convert('RGB')
                if user_type =="admin":
                    image.save(f"resources/PQR/admin_user/{user_number}.png")
                    path = f"resources/PQR/admin_user/{user_number}.png"
                elif user_type =="student":
                    image.save(f"resources/PQR/student_user/{user_number}.png")
                    path = f"resources/PQR/student_user/{user_number}.png"
                elif user_type =="domestic":
                    image.save(f"resources/PQR/domestic_user/{user_number}.png")
                    path = f"resources/PQR/domestic_user/{user_number}.png"
                elif user_type =="visitor":
                    image.save(f"resources/PQR/visitor_user/{user_number}.png")
                    path = f"resources/PQR/visitor_user/{user_number}.png"
                elif user_type =="security":
                    image.save(f"resources/PQR/security_user/{user_number}.png")
                    path = f"resources/PQR/security_user/{user_number}.png" 
            except Exception as e :
                print("[generate_token] generate_token() error:",e)
            return path 
        def verify_user_qr(self, user_number,user_type,reciver_email):
            path  = ""
            try:
                if user_type =="admin":
                    path = f"resources/PQR/admin_user/{user_number}.png"
                elif user_type =="student":
                    path = f"resources/PQR/student_user/{user_number}.png"
                elif user_type =="domestic":
                    path = f"resources/PQR/domestic_user/{user_number}.png"
                elif user_type =="visitor":
                    path = f"resources/PQR/visitor_user/{user_number}.png"
                elif user_type =="security":
                    path = f"resources/PQR/security_user/{user_number}.png" 

                email_address  ="dummyjackson8@gmail.com"
                email_password  ="dummy101@1"
                email_recieve = reciver_email
                msg = EmailMessage()
                msg['Subject'] = 'Personal QR code'
                msg['From'] = email_address
                msg['To']= email_recieve
                msg.add_alternative(f"""
                        <!DOCTYPE html>
                        <html>
                            <body>
                                <h2 style ="color:#96c8cc;">For :{user_number}</h2>
                                <p>Please find the attached image containing your personal QR code</p>
                                <p>Please  feel safe under Salus</p>
                                <p> We care about your well being </p>
                                <p>Yours sincerly</p>
                                <p>The Salus team</p>
                            </body>
                        </html>
                        """,subtype= "html")
                files = [f"{user_number}.png"]
                for images in files:
                    with open(f"{path}","rb") as image :
                        file_data = image.read()
                        file_type = imghdr.what(image.name)
                        file_name= image.name
                        msg.add_attachment(file_data,maintype="image",subtype=file_type,filename =file_name)
                with smtplib.SMTP_SSL("smtp.gmail.com" ,465) as smtp:
                    smtp.login(email_address,email_password)
                    smtp.send_message(msg)
                    print("Email has been sent")
            except Exception as e :
                print("[verify_user_qr] verify_user_qr() error:",e) 
        def genrate_grounds_qr(self,user_number):
                try:
            
                    creation_point = datetime.now()
                    date = str(creation_point.year)+"-"+str(creation_point.month)+"-"+str(creation_point.day)
                    payload_image= "http://localhost:4200/ongroundscheck"
                    qr = qrcode.QRCode(
                            version=1,
                            error_correction=qrcode.constants.ERROR_CORRECT_H,
                            box_size=10,
                            border=4,
                        )
                    qr.add_data(payload_image)
                    qr.make(fit=True)
                    image = qr.make_image(fill_color="black", back_color="white").convert('RGB')

                    make = find_all("log.json","resources/OGQR/")
                    if make == 1:
                        array_of_qr = []
                        with open("resources/OGQR/log.json") as outfile:
                            data = json.loads(outfile.read())
                            print(data)
                            array  = data["qr"]
                            for  i in array :
                                array_of_qr.append(i)
                            qr_new_object = {
                                "date":date,
                                "user_number":user_number,
                                "pay_load":payload_image
                            }
                            array_of_qr.append(qr_new_object)
                            with open("resources/OGQR/log.json","w") as infile:
                                file_object = {
                                    "qr":array_of_qr
                                }
                                json.dump(file_object,infile)
                    elif make == 0 : 
                        array_of_qr = []
                        qr_new_object = {
                                "date":date,
                                "user_number":user_number,
                                "pay_load":payload_image
                            }
                        array_of_qr.append(qr_new_object)
                        with open("resources/OGQR/log.json","w") as infile:
                            file_object = {
                                    "qr":array_of_qr
                                }
                            json.dump(file_object,infile)         
                except Exception as e :
                    print("[genrate_grounds_qr] genrate_grounds_qr() error:",e)
                return image, qr 
                
        def retreive_qr_info(self,log):
            info1=""
            user_number =""
            creation_date = ""
            try:
                image = log.make_image(fill_color="black", back_color="white").convert('RGB')
                image.save("QRcodes/test1.png")
                #qr data reading area 
                im = cv.imread("QRcodes/test1.png")
                det = cv.QRCodeDetector()
                retval, points, straight_qrcode = det.detectAndDecode(im)
                message  = retval 

                split_point = 0
                split_point2 = 0
                for i in range (0,len(message)):

                    if message[i] == ",":
                        split_point = i 
                    if message[i] == ";":
                        split_point2 = i 
                ## info1
                for i  in range (0,split_point):
                    info1 = info1 + message[i] 
                ##user_number
                for i in range (split_point + 1,split_point2):
                    user_number = user_number + message[i]
                ## date of creation
                for i in range (split_point2 + 1,len(message)):
                    creation_date = creation_date + message[i]

                print(info1)
                print(user_number)
                print(creation_date)
                                
            except Exception as e :
                print("[generate_token] generate_token() error:",e)
            return info1,user_number,creation_date

        def class_register_qr_code(self,user_number):
            image = ""
            try:
                
                creation_point = datetime.now()
                date = str(creation_point.year)+"-"+str(creation_point.month)+"-"+str(creation_point.day)
                time = creation_point.strftime("%H:%M:%S")
                payload_image="http://localhost:4200/registercheck"
                qr = qrcode.QRCode(
                        version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_H,
                        box_size=10,
                        border=4,
                    )
                qr.add_data(payload_image)
                qr.make(fit=True)
                image = qr.make_image(fill_color="black", back_color="white").convert('RGB')
                make = find_all("log.json","resources/RCQR/")
                if make == 1:
                    array_of_qr = []
                    with open("resources/RCQR/log.json") as outfile:
                        data = json.loads(outfile.read())
                        print(data)
                        array  = data["qr"]
                        for  i in array :
                            array_of_qr.append(i)
                        qr_new_object = {
                                "date":date,
                                "time":time,
                                "user_number":user_number,
                                "pay_load":payload_image
                            }
                        array_of_qr.append(qr_new_object)
                        with open("resources/RCQR/log.json","w") as infile:
                            file_object = {
                                "qr":array_of_qr
                                }
                            json.dump(file_object,infile)
                elif make == 0 : 
                    array_of_qr = []
                    qr_new_object = {
                                "date":date,
                                "time":time,
                                "user_number":user_number,
                                "pay_load":payload_image
                            }
                    array_of_qr.append(qr_new_object)
                    with open("resources/RCQR/log.json","w") as infile:
                        file_object = {
                                    "qr":array_of_qr
                                }
                        json.dump(file_object,infile) 
            except Exception as e:
                print("[class_register_qr_code] class_register_qr_code() error:",e)
            return image,qr

        def read_qr_code(self,user_number):
            im = cv.imread(f'{user_number}.png')
            det = cv.QRCodeDetector()
            retval, points, straight_qrcode = det.detectAndDecode(im)
            print(retval)
            print(points)
            print(straight_qrcode)

        def emailing_services(self,reciver_email,name,user_number,type,token = "",verification_password="",verificationNumber="",password =""):
            try:
                
                
                email_address  ="dummyjackson8@gmail.com"
                email_password  ="dummy101@1"
                email_recieve = reciver_email  
                
                if type == "signup":
                    msg = EmailMessage()
                    msg['Subject'] = 'Welcome to Salus'
                    msg['From'] = email_address
                    msg['To']= email_recieve
                    msg.add_alternative(f"""
                        <!DOCTYPE html>
                        <html>
                            <body>
                                <h1 style ="color:#96c8cc;">Account Made</h1> 
                                <h2 style ="color:#96c8cc;">Thank you {name}</h2>
                                <p>Welcome to Salus we happy to provide u a new way to get onto your school grounds to with safety and secure tracking while maintaining you safety on school gounds and notifying you of issues on school grounds</p>
                                <p>Please  feel safe under Salus</p>
                                <p> We care about your well being </p>
                                <p>Yours sincerly</p>
                                <p>The Salus Team</p>
                            </body>
                        </html>
                        """,subtype= "html")
                    files = ["saluswithname.jpg"]
                    for images in files:
                        with open(f"{images}","rb") as image :
                            file_data = image.read()
                            file_type = imghdr.what(image.name)
                            file_name= image.name
                        msg.add_attachment(file_data,maintype="image",subtype=file_type,filename =file_name)
                elif type == "pg_signup":
                        msg = EmailMessage()
                        msg['Subject'] = 'Welcome to Salus'
                        msg['From'] = email_address
                        msg['To']= email_recieve
                        msg.set_content ('Welcome to Salus we happy to provide you a new way to get onto your school grounds to with safety and secure tracking while maintaining you safety on school gounds and notifying you of issues on school grounds')
                        msg.add_alternative(f"""
                            <!DOCTYPE html>
                            <html>
                                <body>
                                    <h1 style ="color:#96c8cc;">Account Made</h1> 
                                    <h2 style ="color:#96c8cc;">Thank you Parent or Gaudian of {name}</h2>
                                    <p>Your child has signed up for an account with Salus they will be in good hands</p>
                                    <p>Welcome to Salus we happy to provide u a new way to get onto your school grounds to with safety and secure tracking while maintaining you safety on school gounds and notifying you of issues on school grounds</p>
                                    <p>Please  feel safe under Salus</p>
                                    <p> We care about your well being </p>
                                    <p>Yours sincerly</p>
                                    <p>The Salus team</p>
                                </body>
                            </html>
                            """,subtype= "html")
                        files = ["saluswithname.jpg"]
                        for images in files:
                            with open(f"{images}","rb") as image :
                                file_data = image.read()
                                file_type = imghdr.what(image.name)
                                file_name= image.name
                            msg.add_attachment(file_data,maintype="image",subtype=file_type,filename =file_name)
                elif type == "message":
                        msg = EmailMessage()
                        msg['Subject'] = 'Salus has recieved your Messsage'
                        msg['From'] = email_address
                        msg['To']= email_recieve
                        msg.set_content ('Welcome to Salus we have recived your message and we promptly get back to you as soon as we have either read or fixed any issues you may have incountered .We thank you for you patrionage ')
                        msg.add_alternative(f"""
                            <!DOCTYPE html>
                            <html>
                                <body>
                                    <h1 style ="color:#96c8cc;">Message Recieved</h1> 
                                    <h2 style ="color:#96c8cc;">Thank you {name}</h2>
                                    <p>Welcome to Salus we have recived your message and we promptly get back to you as soon as we have either read or fixed any issues you may have incountered </p>
                                    <pWe thank you for you patrionage</p>
                                    <p>Please  feel safe under Salus</p>
                                    <p>We care about your well being </p>
                                    <p>Yours sincerly</p>
                                    <p>The Salus team</p>
                                </body>
                            </html>
                            """,subtype= "html")
                        files = ["saluswithname.jpg"]
                        for images in files:
                            with open(f"{images}","rb") as image :
                                file_data = image.read()
                                file_type = imghdr.what(image.name)
                                file_name= image.name
                            msg.add_attachment(file_data,maintype="image",subtype=file_type,filename =file_name)
                
                elif type == "forgot_password":
                    print("forgot passowrd")
                    msg = EmailMessage()
                    msg['Subject'] = 'Forgot Your Password '
                    msg['From'] = email_address
                    msg['To']= email_recieve
                    msg.set_content ( f'A sign in attempt requires further verification because we did not recognize your device. To complete the sign in, enter the verification code on the unrecognized device. Here is your verification code :{verification_password}')
                    msg.add_alternative(f"""
                        <!DOCTYPE html>
                        <html>
                            <body>
                                <h1 style ="color:#96c8cc;">Forgot your password</h1> 
                                <h2 style ="color:#96c8cc;">Hello {name}</h2>
                                <p>A sign in attempt requires further verification because we did not recognize your device. To complete the sign in, enter the verification code on the unrecognized device.</p>
                                <p>Here is your verification code :</p>
                                <h1 style ="color:#96c8cc;">{verificationNumber}</h1>
                                <p>Yours sincerly</p>
                                <p>The Salus team</p>
                            </body>
                        </html>
                        """,subtype= "html")
                    files = ["saluswithname.jpg"]
                    for images in files:
                        with open(f"{images}","rb") as image :
                            file_data = image.read()
                            file_type = imghdr.what(image.name)
                            file_name= image.name
                        msg.add_attachment(file_data,maintype="image",subtype=file_type,filename =file_name)
                elif type == "forgot_password_send":
                    print("forgot passowrd send")
                    msg = EmailMessage()
                    msg['Subject'] = 'Forgot Your Password '
                    msg['From'] = email_address
                    msg['To']= email_recieve
                    msg.set_content ( f'A sign in attempt requires further verification because we did not recognize your device. To complete the sign in, enter the verification code on the unrecognized device. Here is your verification code :{verification_password}')
                    msg.add_alternative(f"""
                        <!DOCTYPE html>
                        <html>
                            <body>
                                <h1 style ="color:#96c8cc;">Forgot your password</h1> 
                                <h2 style ="color:#96c8cc;">Hello {name}</h2>
                                <p>A sign in attempt that requires further verification has identified a forgotten passsword</p>
                                <p>We recieved your request and have verified you as the holder for the account assigned to :{email_recieve}.</p>
                                <h1 style ="color:#96c8cc;">Your account password :{password}</h1>
                                <p>Disclaimer: We are not liable for any misconduct if this email is not meant for you please send it to email.</p>
                                <p>Yours sincerly</p>
                                <p>The Salus team</p>
                            </body>
                        </html>
                        """,subtype= "html")
                    files = ["saluswithname.jpg"]
                    for images in files:
                        with open(f"{images}","rb") as image :
                            file_data = image.read()
                            file_type = imghdr.what(image.name)
                            file_name= image.name
                        msg.add_attachment(file_data,maintype="image",subtype=file_type,filename =file_name)
                elif type == "change_password" : 
                    print("change_password")
                    msg = EmailMessage()
                    msg['Subject'] = 'Change Your Password '
                    msg['From'] = email_address
                    msg['To']= email_recieve
                    msg.set_content ( 'You wish to change your password')
                    msg.add_alternative(f"""
                        <!DOCTYPE html>
                        <html>
                            <body>
                                <h1 style ="color:#96c8cc;">Account Made</h1> 
                                <h2 style ="color:#96c8cc;">Thank you {name}</h2>
                                <p>Welcome to flow we happy to provide u a new way to bring ease to you doctor appointment making system</p>
                                <p>We care about your well being </p>
                                <p>Yours sincerly</p>
                                <p>The Salus Team</p>
                            </body>
                        </html>
                        """,subtype= "html")
                    files = ["Screenshot 2021-07-11 220843.png","download.jpg"]
                    for images in files:
                        with open(f"C:/Users/farai/OneDrive/Documents/personal work/startup/Flow/resources/{images}","rb") as image :
                            file_data = image.read()
                            file_type = imghdr.what(image.name)
                            file_name= image.name
                        msg.add_attachment(file_data,maintype="image",subtype=file_type,filename =file_name)
                with smtplib.SMTP_SSL("smtp.gmail.com" ,465) as smtp:
                    smtp.login(email_address,email_password)

                    smtp.send_message(msg)
                    print("Email has been sent")    
                    return True    
            except Exception as e :
                print("[email_service] emailingServices() error:",e)
        def log_breach(self,breach_type,quadrant,user_number,breach_number):
            try:
                creation_point = datetime.now()
                date = str(creation_point.year)+"-"+str(creation_point.month)+"-"+str(creation_point.day)
                log_payload  = {
                    "creation_date":f"{date}",
                    "breach_number":f"{breach_number}",
                    "user_number":f"{user_number}",
                    "quadrant":f"{quadrant}",
                    "breach_type":f"{breach_type}"
                }
                make = find_all("log.json","resources/BL/")
                if make == 1:
                    array_of_qr = []
                    with open("resources/BL/log.json") as outfile:
                        data = json.loads(outfile.read())
                        print(data)
                        array  = data["breaches"]
                        for  i in array :
                            array_of_qr.append(i)
                        array_of_qr.append(log_payload)
                        with open("resources/BL/log.json","w") as infile:
                            file_object = {
                                "breaches":array_of_qr
                                }
                            json.dump(file_object,infile)
                elif make == 0 : 
                    array_of_qr = []
                    array_of_qr.append(log_payload)
                    with open("resources/BL/log.json","w") as infile:
                        file_object = {
                                    "breaches":array_of_qr
                                }
                        json.dump(file_object,infile) 
            except Exception as e :
                print("[log_breach] log_breach() error:",e)


        def breach_alram_email_service(self ,type_alram):
            try:
                email_address  ="dummyjackson8@gmail.com"
                email_password  ="dummy101@1"      
                email_recieve = "findo.93.ss@gmail.com"
               

                msg = EmailMessage()
                msg['Subject'] = 'Welcome to Salus'
                msg['From'] = email_address
                msg['To']= email_recieve
                
                msg.add_alternative(f"""
                        <!DOCTYPE html>
                        <html>
                            <body>
                                <h1 style ="color:#96c8cc;">Security Breach</h1> 
                                <h2 style ="color:#96c8cc;">{type_alram}</h2>
                                <p>There has been a breach.</p>
                                <p>This email has been sent to inform you that a breach of the type above has occured on shool campus with has be idetified as a danger to persons of this facility</p>
                                <p>Please use the link the below to go to the response page</p>
                                <p>http://localhost:4200/breachresponse</p>
                                <p>Please  feel safe under Salus</p>
                                <p> We care about your well being </p>
                                <p>Yours sincerly</p>
                                <p>The Salus team</p>
                            </body>
                        </html>
                        """,subtype= "html")                    
                files = ["saluswithname.jpg"]
                for images in files:
                    with open(f"{images}","rb") as image :
                        file_data = image.read()
                        file_type = imghdr.what(image.name)
                        file_name= image.name
                        msg.add_attachment(file_data,maintype="image",subtype=file_type,filename =file_name) 
                with smtplib.SMTP_SSL("smtp.gmail.com" ,465) as smtp:
                    smtp.login(email_address,email_password)
                    smtp.send_message(msg)
                    print("Email has been sent")    
                return True   
            except Exception as  e :
                print("[breach_alram_email_service] breach_alram_email_service() error:",e)
        def vistor_emailing_services(self,reciver_email,name,visitor_number):
            try :
                creation_point = datetime.now()
                date = str(creation_point.year)+"-"+str(creation_point.month)+"-"+str(creation_point.day)
                make = find_all("log.json","resources/OGQR/")
                if make == 1:
                    array_of_qr = []
                    with open("resources/OGQR/log.json") as outfile:
                        data = json.loads(outfile.read())
                        array  = data["qr"]
                        for  i in array :
                            array_of_qr.append(i)
                        qr_new_object = {
                                "date":date,
                                "name":name,
                                "visitor_number":visitor_number
                            }
                        array_of_qr.append(qr_new_object)
                        with open("resources/OGQR/log.json","w") as infile:
                            file_object = {
                                    "qr":array_of_qr
                                }
                            json.dump(file_object,infile)
                elif make == 0 : 
                    array_of_qr = []
                    qr_new_object = {
                                "date":date,
                                "name":name,
                                "visitor_number":visitor_number
                            }
                    array_of_qr.append(qr_new_object)
                    with open("resources/OGQR/log.json","w") as infile:
                        file_object = {
                                    "qr":array_of_qr
                                }
                        json.dump(file_object,infile)


                email_address  ="dummyjackson8@gmail.com"
                email_password  ="dummy101@1"
                email_recieve = reciver_email

                msg = EmailMessage()
                msg['Subject'] = 'Welcome to Salus'
                msg['From'] = email_address
                msg['To']= email_recieve
                msg.set_content ('Welcome to Salus we happy to provide you a new way to get onto your school grounds to with safety and secure tracking while maintaining you safety on school gounds and notifying you of issues on school grounds')
                msg.add_alternative(f"""
                        <!DOCTYPE html>
                        <html>
                            <body>
                                <h1 style ="color:#96c8cc;">Account Made</h1> 
                                <h2 style ="color:#96c8cc;">Thank you {name}</h2>
                                <p>Welcome to Salus we happy to provide u a new way to get onto your school grounds to with safety and secure tracking while maintaining you safety on school gounds and notifying you of issues on school grounds</p>
                                <p>Your visitor number :{visitor_number}</p>
                                <p>Please user it to be able to login into the visitors portal </p>
                                <p>Please  feel safe under Salus</p>
                                <p> We care about your well being </p>
                                <p>Yours sincerly</p>
                                <p>The Salus team</p>
                            </body>
                        </html>
                        """,subtype= "html")
                files = ["ongrounds.png"]
                for images in files:
                    with open(f"QRcodes/{images}","rb") as image :
                        file_data = image.read()
                        file_type = imghdr.what(image.name)
                        file_name= image.name
                        msg.add_attachment(file_data,maintype="image",subtype=file_type,filename =file_name)
                    os.remove(f"QRcodes/ongrounds.png")
                with smtplib.SMTP_SSL("smtp.gmail.com" ,465) as smtp:
                    smtp.login(email_address,email_password)
                    smtp.send_message(msg)
                    print("Email has been sent")    
            except Exception as e :
                print("[vistor_emailing_services] vistor_emailing_services() error:",e)

        def emailing_service_grounds_qr(self,reciver_email,name,token):
            try:
                email_address  ="dummyjackson8@gmail.com"
                email_password  ="dummy101@1"
                email_recieve = reciver_email
                creation_point = datetime.now() 
                date = str(creation_point.year)+"-"+str(creation_point.month)+"-"+str(creation_point.day)
                token.save(f"resources/OGQR/temp/{date}.png")

                msg = EmailMessage()
                msg['Subject'] = 'QR Token '
                msg['From'] = email_address
                msg['To']= email_recieve
                msg.set_content ( f'You have been issed a Token to enter grounds {name}  you may enter school grounds as soon as your QR code has been scanned ')
                msg.add_alternative(f"""
                        <!DOCTYPE html>
                        <html>
                            <body>
                                <h1 style ="color:#96c8cc;">School Grounds Enter link Token</h1> 
                                <h2 style ="color:#96c8cc;">{name}</h2>
                                <p>Please provide personel who wish to enter onto school gorunds the attached QR code </p>
                                <p>If the personal look suspicous please verify by asking for the users personal QR code  if there is a failuire to provide this please contact authorities</p>
                                <p>Yours sincerly</p>
                                <p>The Salus team</p>
                            </body>
                        </html>
                        """,subtype= "html")
                files = [f"{date}.png"]
                for images in files:
                    with open(f"resources/OGQR/temp/{images}","rb") as image :
                        file_data = image.read()
                        file_type = imghdr.what(image.name)
                        file_name= image.name
                        msg.add_attachment(file_data,maintype="image",subtype=file_type,filename =file_name)
                    os.remove(f"resources/OGQR/temp/{date}.png")
                with smtplib.SMTP_SSL("smtp.gmail.com" ,465) as smtp:
                    smtp.login(email_address,email_password)
                    smtp.send_message(msg)
                    print("Email has been sent")   
                return True   
            except Exception as e :
                print("[emailing_service_grounds_qr] emailing_service_grounds_qr() error:",e)

        def emailing_service_class_register(self,reciver_email,name,token):
            try:
                email_address  ="dummyjackson8@gmail.com"
                email_password  ="dummy101@1"
                email_recieve = reciver_email
                creation_point = datetime.now() 
                date = str(creation_point.year)+"-"+str(creation_point.month)+"-"+str(creation_point.day)
                token.save(f"resources/RCQR/temp/{date}.png")

                msg = EmailMessage()
                msg['Subject'] = 'QR Token '
                msg['From'] = email_address
                msg['To']= email_recieve
                msg.add_alternative(f"""
                        <!DOCTYPE html>
                        <html>
                            <body>
                                <h1 style ="color:#96c8cc;">Class Register link Token</h1> 
                                <h2 style ="color:#96c8cc;">{name}</h2>
                                <p>Please provide students who wish to do class register the attached QR code </p>
                                <p>If the personal look suspicous please verify by asking for the users personal QR code  if there is a failuire to provide this please contact authorities</p>
                                <p>Yours sincerly</p>
                                <p>The Salus team</p>
                            </body>
                        </html>
                        """,subtype= "html")
                files = [f"{date}.png"]
                for images in files:
                    with open(f"resources/RCQR/temp/{images}","rb") as image :
                        file_data = image.read()
                        file_type = imghdr.what(image.name)
                        file_name= image.name
                        msg.add_attachment(file_data,maintype="image",subtype=file_type,filename =file_name)
                    os.remove(f"resources/RCQR/temp/{date}.png")
                with smtplib.SMTP_SSL("smtp.gmail.com" ,465) as smtp:
                    smtp.login(email_address,email_password)
                    smtp.send_message(msg)
                    print("Email has been sent")   
                return True   
            except Exception as e :
                print("[emailing_service_class_register] emailing_service_class_register() error:",e)


        def emailing_message_response(self,reciver_email,name,message):
            try:
                email_address  ="dummyjackson8@gmail.com"
                email_password  ="dummy101@1"
                email_recieve = reciver_email
                creation_point = datetime.now() 
                date = str(creation_point.year)+"-"+str(creation_point.month)+"-"+str(creation_point.day)
                msg = EmailMessage()
                msg['Subject'] = 'Response to your message'
                msg['From'] = email_address
                msg['To']= email_recieve
                msg.add_alternative(f"""
                        <!DOCTYPE html>
                        <html>
                            <body>
                                <h1 style ="color:#96c8cc;">Thank You</h1> 
                                <h2 style ="color:#96c8cc;">{name}</h2>
                                <p>{message}</p>
                                <p>Yours sincerly</p>
                                <p>The Salus team</p>
                            </body>
                        </html>
                        """,subtype= "html")
                files = ["saluswithname.jpg"]
                for images in files:
                    with open(f"{images}","rb") as image :
                        file_data = image.read()
                        file_type = imghdr.what(image.name)
                        file_name= image.name
                        msg.add_attachment(file_data,maintype="image",subtype=file_type,filename =file_name)
                with smtplib.SMTP_SSL("smtp.gmail.com" ,465) as smtp:
                    smtp.login(email_address,email_password)
                    smtp.send_message(msg)
                    print("Email has been sent")   
                return True   
            except Exception as e :
                print("[emailing_service_class_register] emailing_service_class_register() error:",e)

        def activity_report(self):
            try:
                breaches_number = 0 
                ongorund_qr = 0
                register_class = 0
                vistor_number =0
                with open("resources/OGQR/log.json") as outfile:
                    data = json.loads(outfile.read())
                    print(data)
                    array  = data ["qr"]
                    if array != []:
                        ongorund_qr = len(array)
                    else:
                        ongorund_qr = 0
         
                with open("resources/RCQR/log.json") as outfile:
                    data = json.loads(outfile.read())
                    print(data)
                    array  = data ["breaches"]
                    if array != []:
                        register_class = len(array)
                    else:
                        register_class = 0
           
                with open("resources/BL/log.json") as outfile:
                    data = json.loads(outfile.read())
                    print(data)
                    array  = data ["breaches"]
                    if array != []:
                        breaches_number = len(array)
                    else:
                        breaches_number = 0

                return breaches_number,ongorund_qr,register_class
            except Exception as e :
                print("[activity_report] activity_report() error:",e)

        def random_number_creation(self):
            number = ""
            try:
                temp_num = 0
               
                for i in range(0,4):
                    temp_num = random.randint(1,10)
                    number = number + str(temp_num)
                print("done")
            except Exception as e:
                print("[random_number_creation] random_number_creation() error:",e)
            return number 