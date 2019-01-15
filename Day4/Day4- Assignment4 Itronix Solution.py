#!/usr/bin/env python
# coding: utf-8

# # File Handling
# 
# 
# ### Open
# ### Close
# ### Read
# ### Write
# 
# ### Modes -> r,w,a,r+,w+,a+, (rb,wb,ab)-> binary files

# In[4]:


fo=open("abc.txt","w")
fo.write("Hello World")
fo.close()

## r-> will find if dile exists
## w-> will create file and open in write mode
## a-> will append existing file

##Modes with + sign can create files if not exists


# In[6]:


def createFile():
    b=input("Enter the File Name")
    fo=open(b,"w")
    fo.write("Hello")
    fo.close()
def readFile():
    c=fo.open(b,"r")
    print(c)


# In[13]:


fo =open("hello.txt","a+")
fo.write("Hello")

fo.seek(0,0)   ## in C we use fseek function to point cursor to starting
a=fo.read()

b=fo.read(10) ## 10 Characters from starting   ## in Python we use fo.seek(postion,whens) whesn-> 0 for start 1 for current 2 for end
print(a)
print(b)

l=fo.tell()  ## return the length of the file ## can be used to read the contents from the end
print(l)
fo.close()


# ## Press 1 for signup
# ## Press 2 for login
# 
# ## signup()-> Name,Email,Pass,Phone No, City -> goes to filename -> filename= email name
# ## login()-> Enter Email id, Enter Password compare with second and third line -> Send OTP -> OTP correct then access granted
# 
# ## FogetPassword()-> Enter Email, Phone number, -> Send OTP -> Change password in the file.

# In[5]:


def signup():
    username=input("Enter the Name ")
    email=input("Enter the Email ")
    password=input("Enter the Password ")
    phone=input("Enter the Phone Number ")
    city=input("Enter the City ")
    
    fo=open(email+".txt","w")
    fo.write(username+"\n"+email+"\n"+password+"\n"+phone+"\n"+city)
    fo.close()
    print("Sign up Succesfull")


# In[8]:


def login():
    import random
    from twilio.rest import Client
    email=input("Enter the Email Address ")
    password=input("Enter the Password ")
    data=[]
    fo=open(email+".txt","r")
    data=fo.readlines()
    ##print(data)
    e=data[1]
    p=data[2]
    e=e[:-1]
    p=p[:-1]
    if e==email and p==password:
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
        code=int(input("Please Enter the OTP"))
        i=1
        while i<=3:
            if code==a:
                print("Login SuccessFul")
                print("Exiting Application")
                break
            else:
                i+=1
                code=int(input("Please Enter the OTP"))
        if i==4:
            print("OTP Authentication Failed. Exiting Application")
    else:
        print("Invalid Username or Password")
    fo.close()


# In[9]:


def forgetpassword():
    import random
    from twilio.rest import Client
    
    email=input("Please Enter the Email ")
    phone=input("Please Enter the Phone Number ")
    
    data=[]
    fo=open(email+".txt","r")
    data=fo.readlines()
    e=data[1]
    ph=data[3]
    e=e[:-1]
    ph=ph[:-1]
    fo.close()
    if e==email and ph==phone:
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
        code=int(input("Please Enter the OTP "))
        i=1
        while i<=3:
            if code==a:
                fo=open(email+".txt","w")
                newpassword=input("Please Enter the new Password ")
                data[2]=newpassword+"\n"
                fo.writelines(data)
                fo.close()
                print("Password Changed Successfully")
                answer=input("Do you want to Login? y/n")
                if answer=="n":
                    break
                elif answer=="y":
                    login()
                    break
            else:
                i+=1
                code=int(input("Please Enter the OTP"))
            if i==4:
                print("Authentication Failed")
    else:
        print("Invalid Username or Password")
    fo.close()
    


# In[6]:


signup()


# In[78]:


login()


# In[11]:


forgetpassword()

