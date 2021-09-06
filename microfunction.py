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

class tools :
        def id_number_genrator(self):
            id_number = uuid.uuid1()
            print(id_number)
            return id_number

        def generate_token(self,profile,user_number):
            image = ""
            print(profile,user_number)
            qr_id = uuid.uuid1()
            try:
                if profile != "" and user_number != "": 
                    name = profile["name"]
                    surname = profile["surname"]
                    creation_point = datetime.now()
                    payload_image= f"NAME:{name}, SURNAME:{surname}, USER NUMBER:{user_number}, CREATED:{creation_point}, QR CODE ID:{qr_id},"
                    # text =qrcode.make(payload)
                    #image creation 
                    qr = qrcode.QRCode(
                        version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_H,
                        box_size=10,
                        border=4,
                    )
                    qr.add_data(payload_image)
                    qr.make(fit=True)
                    image = qr.make_image(fill_color="black", back_color="white").convert('RGB')
                    # image.save(f"QRcodes/{user_number}.png")
                else :
                    print("Missing credentials to create qr code")
            except Exception as e :
                print("[generate_token] generate_token() error:",e)
            return image 

        def class_register_qr_code(self,class_subject,teacher_name,qr_id ):
            image = ""
            qr_id = uuid.uuid1()
            try:
                if class_subject != "" and teacher_name != "" and qr_id !="":
                    creation_point = datetime.now()
                    payload_image= f"CLASS:{class_subject}, TEACHER:{teacher_name}, CREATED:{creation_point}, QR CODE ID:{qr_id},"

                    #image creation 
                    qr = qrcode.QRCode(
                        version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_H,
                        box_size=10,
                        border=4,
                    )
                    qr.add_data(payload_image)
                    qr.make(fit=True)
                    image = qr.make_image(fill_color="black", back_color="white").convert('RGB')
                    # image.save(f"QRcodes/{user_number}.png")
                else :
                    print("Missing credentials to create qr code")
            except Exception as e:
                print("[class_register_qr_code] class_register_qr_code() error:",e)

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
                    msg.set_content ('Welcome to Salus we happy to provide u a new way to get onto your school grounds to with safety and secure tracking while maintaining you safety on school gounds and notifying you of issues on school grounds')
                    msg.add_alternative(f"""
                        <!DOCTYPE html>
                        <html>
                            <body>
                                <h1 style ="color:#96c8cc;">Account Made</h1> 
                                <h2 style ="color:#96c8cc;">Thank you {name}</h2>
                                <p>Welcome to Salus we happy to provide u a new way to get onto your school grounds to with safety and secure tracking while maintaining you safety on school gounds and notifying you of issues on school grounds</p>
                                <p>Please be feel safe under Salus</p>
                                <p> We care about your well being </p>
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
                elif type == "qr_code":
                    print("qr_code")
                    token.save(f"QRcodes/{user_number}.png")
                    msg = EmailMessage()
                    msg['Subject'] = 'QR Token '
                    msg['From'] = email_address
                    msg['To']= email_recieve
                    msg.set_content ( f'You have been issed a Token to enter grounds {name}  you may enter school grounds as soon as your QR code has been scanned ')
                    msg.add_alternative(f"""
                        <!DOCTYPE html>
                        <html>
                            <body>
                                <h1 style ="color:#96c8cc;">School Grounds Token</h1> 
                                <h2 style ="color:#96c8cc;">{name}</h2>
                                <p>You have been issed a Token to enter grounds{name}  you may enter school grounds as soon as your QR code has been scanned </p>
                                <p>Yours sincerly</p>
                                <p>The Salus team</p>
                            </body>
                        </html>
                        """,subtype= "html")
                    files = [f"{user_number}.png"]
                    for images in files:
                        with open(f"QRcodes/{images}","rb") as image :
                            file_data = image.read()
                            file_type = imghdr.what(image.name)
                            file_name= image.name
                        msg.add_attachment(file_data,maintype="image",subtype=file_type,filename =file_name)
                    os.remove(f"QRcodes/{images}")
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
                                <p>Here is your verification code :{verification_password}</p>
                                <p>Yours sincerly</p>
                                <p>The Salus team</p>
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
                                <p> WE care about your well being </p>
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

        def random_number_creation():
            number = ""
            try:
                temp_num = 0
               
                for i in range(0,4):
                    temp_num = random.randint()
                    number = number + str(temp_num)
                print(done)
            except Eception as e:
                print("[random_number_creation] random_number_creation() error:",e)
            return number 