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

class tools :
        def id_number_genrator(self):
            id_number = uuid.uuid1()
            return id_number

        def emailing_services(self,reciver_email,name,type,verification_password=""):
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
                
                elif type == "forgot_passoword":
                    print("forgot passowrd")
                    msg = EmailMessage()
                    msg['Subject'] = 'Forgot Your Password '
                    msg['From'] = email_address
                    msg['To']= email_recieve
                    msg.set_content ( 'Welcome to flow we happy to provide u a new way to bring ease to you doctor appointment making system')
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
                print("[email_service] emailingServices() joining error:",e)