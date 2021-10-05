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

        def purge_qr_codes(self):
            try:
                files =[] 
                for directory ,subdirectories,filenames in os.walk("QRcodes"):
                    for filename in filenames:
                        files.append(filename)
                for i in range (0,len(files)):
                    os.remove("QRcodes/"+files[i])
            except Exception as e :
                print("[purge_qr_codes] purge_qr_codes() error:",e)
                return 0
            return 1
            

        def generate_token(self,name,user_number):
            try:
                
                creation_point = datetime.now()
                payload_image= f"{name},{user_number};{creation_point}"
               
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
                image.save(f"QRcodes/{user_number}.png")
                path  = f"QRcodes/{user_number}.png"
    
            except Exception as e :
                print("[generate_token] generate_token() error:",e)
            return image, qr ,path 

        def genrate_grounds_qr(self):
                try:
                     
                    creation_point = datetime.now()
                    payload_image= "http://localhost:4200/registercheck"
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
                    msg.set_content ('Welcome to Salus we happy to provide you a new way to get onto your school grounds to with safety and secure tracking while maintaining you safety on school gounds and notifying you of issues on school grounds')
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
                                <p>Disclaimer: we are not liable for any misconduct if this email is not meant for you please send it to email.</p>
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


        def breach_alram_email_service(self ,type_alram,message,sender):
            try:
                email_address  ="dummyjackson8@gmail.com"
                email_password  ="dummy101@1"
                # email_recieve = ""
                # if type_alarm == " ":
                # elif type_alarm == " ":
                # elif type_alarm == " ":
                # elif type_alarm == " ":
                # elif type_alarm == " ":
                    
                email_recieve = reciver_email 
               

                msg = EmailMessage()
                msg['Subject'] = 'Welcome to Salus'
                msg['From'] = email_address
                msg['To']= email_recieve
                msg.set_content ('Welcome to Salus we happy to provide u a new way to get onto your school grounds to with safety and secure tracking while maintaining you safety on school gounds and notifying you of issues on school grounds')
                msg.add_alternative(f"""
                        <!DOCTYPE html>
                        <html>
                            <body>
                                <h1 style ="color:#96c8cc;">Security Breach</h1> 
                                <h2 style ="color:#96c8cc;">{type_alram}</h2>
                                <p>There has been a breach.</p>
                                <p>This email has been sent to inform you that a breach of the type above has occured on shool campus with has be idetified as a danger to persons of this facility</p>
                                <p>Response</p>
                                <p>Yours sincerly</p>
                                <p>The Salus team</p>
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

        def emailing_service_grounds_qr(self,reciver_email,name,token):
            try:
                email_address  ="dummyjackson8@gmail.com"
                email_password  ="dummy101@1"
                email_recieve = reciver_email
                creation_point = datetime.now()   
                token.save(f"QRcodes/ongrounds.png")

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
                return True   
            except Exception as e :
                print("[emailing_service_grounds_qr] emailing_service_grounds_qr() error:",e)

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