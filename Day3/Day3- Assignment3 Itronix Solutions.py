#!/usr/bin/env python
# coding: utf-8

# # Functions

# In[3]:


def sum (a,b):
    return a+b
print(sum(5,6))


# # Send email using Python

# In[2]:


import smtplib
serveranyvariable = smtplib.SMTP('smtp.gmail.com',587)
serveranyvariable.starttls()
serveranyvariable.login("swiftsnoop@gmail.com","XXXXXXXXXX")
msg="Test Email using python"
serveranyvariable.sendmail("swiftsnoop@gmail.com","vkunal1996@gmail.com",msg)
serveranyvariable.quit()


# # Send email with subject and attachment using python

# In[9]:


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


serverVariable=smtplib.SMTP('smtp.gmail.com',587)
serverVariable.starttls()
serverVariable.login("swiftsnoop@gmail.com","XXXXXXXXX")
body="Hi this is a sample email Sender Module for Testing\nRegards\nKunal Verma"
subject="Test Email using Python"

msg=MIMEMultipart()
msg['From']= "swiftnoop@gmail.com"
msg['To']= "vkunal1996@gmail.com"
msg['Subject']=subject

msg.attach(MIMEText(body,'plain'))


filename = "testimage.jpg"
attachment = open("/home/kunalverma/Itronix Solutions/testimage.jpg", "rb") 

# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 
  
# To change the payload into encoded form 
p.set_payload((attachment).read()) 
  
# encode into base64 
encoders.encode_base64(p) 
   
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
  
# attach the instance 'p' to instance 'msg' 
msg.attach(p) 


text=msg.as_string()

serverVariable.sendmail("swiftsnoop@gmail.com","vkunal1996@gmail.com",text)

serverVariable.quit()

print("Email Sent")


# # Send Message using twilio in python

# In[12]:


from twilio.rest import Client

import random
# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC2b08c61d97f3d464d4aac842d88d3233'
auth_token = 'c6ad75fd7a1dc89e50c0df942d140958'
client = Client(account_sid, auth_token)

call = client.calls.create(
         from_='+14403067092',
         to='+918699973170',
         url="http://demo.twilio.com/docs/voice.xml"
     )

print(call.sid)

# Send OTP to phone
a=random.randint(1000,9999)
otp="Your Otp is "+str(a)
message = client.messages.create(
         body=otp,
         from_='+14403067092',
         to='+918699973170',
     )

print(message.sid)

"""Send ho gya pr aya ni hje tak..on the way... ponch jayega 2-3 salan tak"""


# # Signup -> Login-> ask for OTP -> Check OTP -> Login succesfull

# In[6]:


from twilio.rest import Client
import random
""" Sign up Module """

username=input("Please Enter the username ")
password=input("Please Enter the Password ")

print("Account has been Created Succesfully")
approval=input("Do you Wish to login?(y/n)")

"""Login Module"""

if approval is 'n':
    exit()
elif approval is 'y':
    loginusername=input("Please Enter the username ")
    loginpassword=input("Please Enter the Password ")
    if loginpassword == password and loginusername == username:
       
    
        """Otp Generation"""
        
        
        a=random.randint(1000,9999)
        print("OTP is ",a)
        otp="Dear "+loginusername+" Your Otp is "+str(a)
        
        
        
        """Sending Otp to registered Mobile"""
        
        
        account_sid = 'AC191c4af117808f7e138459b90d28fd6e'
        auth_token = '4e83b66b9b3f88d1743e536cd955b321'
        client = Client(account_sid, auth_token)
        message = client.messages.create(
                 body=otp,
                 from_='+19842070224',
                 to='+917696478008',
             )

        print("OTP Sent to the Registered Contact Number")
        
        
        
        """Verification Module """
        
        
        
        enterOTP=int(input("Please Enter the OTP "))
        while True:
            if enterOTP == a:
                print("Login SuccessFull")
                print("Exiting Application")
                break
            else:
                print("Invalid OTP")
                enterOTP=int(input("Please Enter the OTP "))

            
            
    else:
        print("Invalid Username or Password. Exiting Application")
        exit()

        

