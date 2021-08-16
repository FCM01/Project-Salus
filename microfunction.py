import random
import string
import smtplib
import os
import json
import imghdr
from email.message import EmailMessage
from datetime import datetime
import uuid

class tools :
        def id_number_genrator(self):
            id_number = uuid.uuid1()
            return id_number

        def emailing_services(self,reciver_email,name,type,verification_password=""):
            try:
                
                email_address  ="dummyjackson8@gmail.com"
                email_password  ="dummy101@1"
                email_recieve = reciver_email

                if type == "appointment":
                    msg = EmailMessage()
                    msg['Subject'] = 'Appointment Made With Doctor'
                    msg['From'] = email_address
                    msg['To']= email_recieve
                    msg.set_content ( 'You have set up an appointment with Dr.Megan Timm practise we will get back to you ass soon as possible Number: 011 893 2100')
                    msg.add_alternative(f"""
                        <!DOCTYPE html>
                        <html>
                            <body>
                                <h1 style ="color:#96c8cc;">Appointment Made</h1> 
                                <h2 style ="color:#96c8cc;">Thank you {name}</h2>
                                <p>You have set up an appointment with Dr.Megan Timm's practise we will get back to you as soon as possible with a time slot for you to come Number: 011 893 2100</p>
                                <zbr>
                                <p>Address</p>
                                <p>27 gannet street </p>
                                <p>GSermiston</p>    
                                <p>1428</p> 
                                <p>South Africa</p>  
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
                
                elif type == "signup":
                    msg = EmailMessage()
                    msg['Subject'] = 'Welcome to FLOW2'
                    msg['From'] = email_address
                    msg['To']= email_recieve
                    msg.set_content ( 'Welcome to flow we happy to provide u a new way to bring ease to you doctor appointment making system')
                    msg.add_alternative(f"""
                        <!DOCTYPE html>
                        <html>
                            <body>
                                <h1 style ="color:#96c8cc;">Account Made</h1> 
                                <h2 style ="color:#96c8cc;">Thank you {name}</h2>
                                <p>Welcome to flow we happy to provide u a new way to bring ease to you doctor appointment making system</p>
                                <p>Please proceed to provide your medical information</p>
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
                                <p>The FLOW2 team</p>
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
                    msg.set_content ( 'Welcome to flow we happy to provide u a new way to bring ease to you doctor appointment making system')
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