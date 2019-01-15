#!/usr/bin/env python
# coding: utf-8

# # DBMS Connectivity using python

# In[3]:


#Libraries are imported here.
import MySQLdb


# In[6]:


db=MySQLdb.connect(host='localhost',user='kunalverma',passwd='12345')


# In[7]:


mycursor=db.cursor()
mycursor.execute("CREATE DATABASE Sudent")


# In[9]:


db=MySQLdb.connect(host='localhost',user='kunalverma',passwd='12345', db='Sudent')
mycursor=db.cursor()
mycursor.execute("Create table studentdetails(FirstName varchar(20),LastName varchar(20))")


# In[15]:


db=MySQLdb.connect(host='localhost',user='kunalverma',passwd='12345', db='Sudent')
mycursor=db.cursor()

mycursor.execute("Insert into studentdetails values('Parul','Verma')")
db.commit()


# In[16]:


db=MySQLdb.connect(host='localhost',user='kunalverma',passwd='12345', db='Sudent')
mycursor=db.cursor()

mycursor.execute("select * from studentdetails")

mydata=mycursor.fetchall()

print(mydata)

for x in mydata:
    print(x[0])  #print 0th column of table


# In[17]:


db=MySQLdb.connect(host='localhost',user='kunalverma',passwd='12345', db='Sudent')
mycursor=db.cursor()

mycursor.execute("update studentdetails set FirstName='kunal' where FirstName='Kunal'")
db.commit()
mydata=mycursor.fetchall()

print(mydata)

for x in mydata:
    print(x[0])  #print 0th column of table


# In[21]:


db=MySQLdb.connect(host='localhost',user='kunalverma',passwd='12345', db='Sudent')
mycursor=db.cursor()

mycursor.execute("delete from studentdetails where FirstName='kunal'")
mydata=mycursor.fetchall()
db.commit()
mycursor.execute("select * from studentdetails")
mydata=mycursor.fetchall()
print(mydata)

for x in mydata:
    print(x[0])  #print 0th column of table


# In[27]:


l=['A','B','C']
it=iter(l)
try:
    while True:
        print(next(it))vb
except StopIteration:
    print("")


# # Assignment - Login Module using dbms in python

# In[ ]:


import MySQLdb
import random
from twilio.rest import Client


# #### Creating Database

# In[44]:


db=MySQLdb.connect(host="localhost",user="kunalverma",passwd="12345")

mycursor=db.cursor()
mycursor.execute('Create Database LoginModule')


# #### Creating table logindetails.

# In[47]:


db=MySQLdb.connect(host="localhost",user="kunalverma",passwd="12345",db="LoginModule")

mycursor=db.cursor()
mycursor.execute("create table logindetails(Name varchar(50),Email varchar(50),Password varchar(100),Phone varchar(15),City varchar(20))")
db.commit()


# #### Inserting Details into database

# In[1]:


def insertdata(name,email,passwd,phone,city):
    db=MySQLdb.connect(host="localhost",user="kunalverma",passwd="12345",db="LoginModule")
    mycursor=db.cursor()
    sql="Select * from logindetails where Email=%s"
    values=email
    mycursor.execute(sql,[values])
    details=mycursor.fetchall()
    if not details:
        sql="Insert into logindetails values(%s,%s,%s,%s,%s)"
        values=(name,email,passwd,phone,city)
        mycursor.execute(sql,values)
        db.commit()
        print("Sign Up SuccesFull")
    else:
        print("Email is already Registered")
    


# #### OTP Generation

# In[2]:


def sendotp():
    a=random.randint(1000,9999)
    otp="Your Otp is "+str(a)
    print(a)
    account_sid = 'AC2b08c61d97f3d464d4aac842d88d3233'
    auth_token = 'c6ad75fd7a1dc89e50c0df942d140958'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
              body=otp,
              from_='+14403067092',
              to='+918699973170',
        )

    print("OTP Sent")
    return a


# #### Login Module of the application

# In[3]:


def login():
    email=input("Enter Email :")
    passwd=input("Enter Password: ")
    
    #opening connection again : 
    db=MySQLdb.connect(host="localhost",user="kunalverma",passwd="12345",db="LoginModule")
    mycursor=db.cursor()
    sql="Select * from logindetails where Email=%s and Password=%s"
    values=(email,passwd)
    mycursor.execute(sql,values)
    details=mycursor.fetchall()
    if not details:
        print("Invalid Username or Password ")
    else:
        otp=sendotp()
        print("OTP is "+str(otp))
        verifyotp=int(input("Please Enter OTP sent to registered Phone"))
        i=3
        while i>=1:
            if verifyotp == otp:
                print("Login SuccessFull")
                headerd=["Name","Email","Passwd","Phone","City"]
                for x in details:
                    for j in range(5):
                        print(headerd[j]+" = "+details[0][j],end=" ")
                break
            else:
                i-=1
                print("Invalid OTP")
                verifyotp=int(input("Please Enter OTP sent to registered Phone"))
        if i==0:
            print("Otp Authentication Failed! Login Denied")
            
    print()   
    return 0


# #### Sign Up Module of the Application

# In[4]:


def signup():
    
    name=input("Enter Name     : ")
    if not name:
        print("Please Enter Valid Name ")
        while not name:
            name=input("Enter Name     : ")
   
    email=input("Enter Email   : ")
    if not email:
        print("Please Enter Valid Email")
        while not email:
            email=input("Enter Email   : ")

    passwd=input("Enter Passwd : ")
    if not passwd:
        print("Please Enter Valid Password")
        while not passwd:
            passwd=input("Enter Passwd : ")
            
    phone=input("Enter Phone   : ")
    if not phone:
        print("Please Enter the Phone")
        while not phone:
            phone=input("Enter Phone   : ")
            
    city=input("Enter City     : ")
    if not city:
        print("Please Enter City")
        while not city:
            city=input("Enter City     : ")
    
    ## Calling Insert method to insert data into the database 
    
    insertdata(name,email,passwd,phone,city)
    


# #### Forget Password Module

# In[29]:


def forgetpass():
    email=input("Enter Email   : ")
    if not email:
        print("Please Enter Valid Email")
        while not email:
            email=input("Enter Email   : ")
            
    phone=input("Enter Phone   : ")
    if not phone:
        print("Please Enter the Phone")
        while not phone:
            phone=input("Enter Phone   : ")
            
    ##Opening Connection
    db=MySQLdb.connect(host="localhost",user="kunalverma",passwd="12345",db="LoginModule")
    mycursor=db.cursor()
    sql="Select * from logindetails where Email=%s and Phone=%s"
    values=(email,phone)
    mycursor.execute(sql,values)
    details=mycursor.fetchall()

    if not details:
         print("No user Details Found!!")

    else:
        otp=sendotp()
        verifyotp=int(input("Please Enter the Otp Sent to Registered Phone Number"))
        i=2
        while i>1:
            if otp != verifyotp:
                i-=1
                print("Invalid OTP")
                verifyotp=int(input("Please Enter the Otp Sent to Registered Phone Number"))
            elif otp==verifyotp:
                passwd=input("Enter new Password ")
                sql="Update logindetails set Password=%s where Email=%s"
               # values=(email,passwd)
                mycursor.execute(sql,[passwd,email])
                db.commit()
                print("Password Changed Successfully")
                break;
        if i==0:
            print("Authentcation Failed ! Exiting")
    
    print()
            
    return 0


# In[32]:


while True:
    print("Please Enter your Choice".center(120,"-"))
    print("1. Login ")
    print("2. Signup ")
    print("3. Forget ")
    print("4. Exit")

    choice=input(">>")
    if choice == "1":
        login()
    elif choice == "2":
        signup()
    elif choice == "3":
        forgetpass()
    elif choice =="4":
        print("Exiting Application")
        exit(1)
        break
    else:
        print("Invalid Choice !")

