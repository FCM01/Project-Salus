import random
import string
import smtplib
import os
import json
import imghdr
from email.message import EmailMessage
from flask_pymongo import PyMongo
from datetime import datetime

class tools :
    def user_account_creation(self,signup_payload):
        try:
            if signup_payload["user_type"]=="Teacher":
                
            elif signup_payload["user_type"]=="Student":
            elif signup_payload["user_type"] =="Vistor":

        except Exception as e:
            print("ERROR:user_account_creation():--->",e)