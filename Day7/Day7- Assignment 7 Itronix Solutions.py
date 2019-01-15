#!/usr/bin/env python
# coding: utf-8

# # Classes and Objects..

# In[5]:


class Employee:
    pass # works similar to continue in other languages

robin= Employee()
rajat= Employee()
 
print(Employee)
print(robin,rajat)


# In[8]:


## Attributes of the object
robin.fname="Robin"
robin.lname="Mahajan"
robin.age="21"

print(robin.fname, robin.lname)


# In[12]:


#Optimze Classs

class Employeeee:                         ## __init__() is default constructor
    def __init__(self,fname,lname,age): ## Work as Default Constructor
        self.fname=fname                ## Self keyword work as this operator
        self.lname=lname
        self.age=age
robin=Employeeee("Robin","Mahajan","21")
rajat=Employeeee("Rajat","Kumar","22")

print(robin.fname,robin.lname,robin.age)


# In[17]:


class Employeeee:       
    increment=1.5                       ## __init__() is default constructor
    def __init__(self,fname,lname,age,salary): ## Work as Default Constructor
        self.fname=fname                ## Self keyword work as this operator
        self.lname=lname
        self.age=age
        self.salary=salary
    def increase(self):
        pass
robin=Employeeee("Robin","Mahajan","21",1234)
rajat=Employeeee("Rajat","Kumar","22",1234)

print(robin.fname,robin.lname,robin.age)
print(robin.increase())


# In[23]:


class Employeeee:       
    increment=1.5                       ## __init__() is default constructor
    def __init__(self,fname,lname,age,salary): ## Work as Default Constructor
        self.fname=fname                ## Self keyword work as this operator
        self.lname=lname
        self.age=age
        self.salary=salary
    def increase(self):
        #self.salary=int(self.salary * increment)  It will generate Error
        self.salary=int(self.salary * Employeeee.increment) # find the class variable
        self.salary=int(self.salary * self.increment) # find the variable in constructor then find the class variable
        
robin=Employeeee("Robin","Mahajan","21",1234)
rajat=Employeeee("Rajat","Kumar","22",1234)

print(robin.fname,robin.lname,robin.age)
print(robin.increase())
print(robin.salary)
print(robin.__dict__)
robin.dept="Sales"
print(robin.__dict__)
print(Employeeee.__dict__)


# In[25]:


class Employeeee:       
    increment=1.5                       ## __init__() is default constructor
    def __init__(self,fname,lname,age,salary): ## Work as Default Constructor
        self.fname=fname                ## Self keyword work as this operator
        self.lname=lname
        self.age=age
        self.salary=salary
    def increase(self):
        #self.salary=int(self.salary * increment)  It will generate Error
        #self.salary=int(self.salary * Employeeee.increment) # find the class variable
        self.salary=int(self.salary * self.increment) # find the variable in constructor then find the class variable
    @classmethod
    def __increase_amount__(cls,amount):
        cls.increment=amount

robin=Employeeee("Robin","Mahajan","21",1234)
rajat=Employeeee("Rajat","Kumar","22",1234)

robin.increase()
print(robin.salary)
robin.__increase_amount__(3)
robin.increase()
print(robin.salary)


# In[31]:


## USE Class method as an alternative Constructor
class Employeeee:       
    increment=1.5                       ## __init__() is default constructor
    def __init__(self,fname,lname,age,salary): ## Work as Default Constructor
        self.fname=fname                ## Self keyword work as this operator
        self.lname=lname
        self.age=age
        self.salary=salary
    def increase(self):
        #self.salary=int(self.salary * increment)  It will generate Error
        #self.salary=int(self.salary * Employeeee.increment) # find the class variable
        self.salary=int(self.salary * self.increment) # find the variable in constructor then find the class variable
    @classmethod
    def __increase_amount__(cls,amount):
        cls.increment=amount
    @classmethod
    def from_str(cls,details):
        fname,lname,age,salary=details.split("-")
        return cls(fname,lname,age,salary)


akshay=Employeeee.from_str("Akshay-Khanna-21-6700")
print(akshay.fname,akshay.lname,akshay.age,akshay.salary)


# In[33]:


##Static Methods.....

## USE Class method as an alternative Constructor
class Employeeee:       
    increment=1.5                       ## __init__() is default constructor
    def __init__(self,fname,lname,age,salary): ## Work as Default Constructor
        self.fname=fname                ## Self keyword work as this operator
        self.lname=lname
        self.age=age
        self.salary=salary
    def increase(self):
        #self.salary=int(self.salary * increment)  It will generate Error
        #self.salary=int(self.salary * Employeeee.increment) # find the class variable
        self.salary=int(self.salary * self.increment) # find the variable in constructor then find the class variable
    @classmethod
    def __increase_amount__(cls,amount):
        cls.increment=amount
    @classmethod
    def from_str(cls,details):
        fname,lname,age,salary=details.split("-")
        return cls(fname,lname,age,salary)
    @staticmethod
    def isopen(day):
        if day == "sunday":
            return False
        else:
            return True

akshay=Employeeee.from_str("Akshay-Khanna-21-6700")
print(akshay.fname,akshay.lname,akshay.age,akshay.salary)
print(Employeeee.isopen('sunday'))
print(akshay.isopen('monday'))


# ## Inheritance

# In[41]:


##Static Methods.....

## USE Class method as an alternative Constructor
class Employeeee:       
    increment=1.5                       ## __init__() is default constructor
    def __init__(self,fname,lname,age,salary): ## Work as Default Constructor
        self.fname=fname                ## Self keyword work as this operator
        self.lname=lname
        self.age=age
        self.salary=salary
    def increase(self):
        #self.salary=int(self.salary * increment)  It will generate Error
        #self.salary=int(self.salary * Employeeee.increment) # find the class variable
        self.salary=int(self.salary * self.increment) # find the variable in constructor then find the class variable
    @classmethod
    def __increase_amount__(cls,amount):
        cls.increment=amount
    @classmethod
    def from_str(cls,details):
        fname,lname,age,salary=details.split("-")
        return cls(fname,lname,age,salary)
    @staticmethod
    def isopen(day):
        if day == "sunday":
            return False
        else:
            return True
    def __add__(self,other):
        return self.salary + other.salary

class Programmer(Employeeee):
    def __init__(self,fname,lname,age,salary,lang,exp):
        super().__init__(fname,lname,age,salary)
        self.lang=lang
        self.exp=exp

kunal=Programmer("Kunal","Verma","22",50000,"python","2 years")
parul=Programmer("Parul","Verma","22",50000,"python","2 years")
print(kunal.fname,kunal.lang)
print(kunal+parul)


# # Graphics

# In[45]:


from tkinter import *
a= Tk()
a.title("shopping Cart")
#a.geometry("500x500+0+0")
def func1():
    print("Hello")
B1=Button(a,text="Hello",width=15,height=5,fg="blue",bg="yellow",command=func1,relief=GROOVE)
B2=Button(a,text="Hello",width=15,height=5,fg="blue",bg="yellow",command=func1,relief=RIDGE)
B3=Button(a,text="Hello",width=15,height=5,fg="blue",bg="yellow",command=func1,relief=FLAT)
B4=Button(a,text="Hello",width=15,height=5,fg="blue",bg="yellow",command=func1,relief=SUNKEN)
B5=Button(a,text="Hello",width=15,height=5,fg="blue",bg="yellow",command=func1,relief=RAISED)

B1.pack()
B2.pack()
B3.pack()
B4.pack()
B5.pack()
a=mainloop()


# In[46]:


from tkinter import *
a= Tk()
a.title("shopping Cart")
#a.geometry("200*200+0+0")
def func1():
    print("Hello")
B1=Button(a,text="Hello",width=15,height=5,fg="blue",bg="yellow",command=func1,relief=GROOVE)
B2=Button(a,text="Hello",width=15,height=5,fg="blue",bg="yellow",command=func1,relief=RIDGE)
B3=Button(a,text="Hello",width=15,height=5,fg="blue",bg="yellow",command=func1,relief=FLAT)
B4=Button(a,text="Hello",width=15,height=5,fg="blue",bg="yellow",command=func1,relief=SUNKEN)
B5=Button(a,text="Hello",width=15,height=5,fg="blue",bg="yellow",command=func1,relief=RAISED)

B1.pack(side=TOP)
B2.pack(side=TOP)
B3.pack(side=TOP)
B4.pack(side=LEFT)
B5.pack(side=RIGHT)
a=mainloop()


# In[54]:


from tkinter import *
a= Tk()
a.title("shopping Cart")
a.geometry("500x500+0+0")
def func1():
    print("Hello")
B1=Button(a,text="Hello",width=15,height=5,fg="blue",bg="yellow",command=func1,relief=GROOVE)
B2=Button(a,text="Hello",width=15,height=5,fg="blue",bg="red",command=func1,relief=RIDGE)
B3=Button(a,text="Hello",width=15,height=5,fg="blue",bg="yellow",command=func1,relief=FLAT)
B4=Button(a,text="Hello",width=15,height=5,fg="blue",bg="yellow",command=func1,relief=SUNKEN)
B5=Button(a,text="Hello",width=15,height=5,fg="blue",bg="yellow",command=func1,relief=RAISED)

B1.pack(side=TOP,fill=X,padx=10,ipadx=40,ipady=30) # fille whole width with button color, padx is for padding ipad is for internal padding
B2.pack(side=TOP,fill=BOTH,expand=1) # for expanding the button, By defualt expnd is 0
B3.pack(side=TOP)
B4.pack(side=LEFT)
B5.pack(side=RIGHT)
a=mainloop()


# In[61]:


from tkinter import *
from tkinter import messagebox
#import tkMessageBox
a= Tk()
a.title("shopping Cart")
a.geometry("500x500+450+100")
def func1():
    messagebox.showinfo("Say hello"," Hellow World")
B1=Button(a,text="Hello",width=15,height=5,fg="blue",bg="yellow",command=func1,relief=GROOVE)
B2=Button(a,text="Hello",width=15,height=5,fg="blue",bg="red",command=func1,relief=RIDGE)
B3=Button(a,text="Hello",width=15,height=5,fg="blue",bg="yellow",command=func1,relief=FLAT)
B4=Button(a,text="Hello",width=15,height=5,fg="blue",bg="yellow",command=func1,relief=SUNKEN)
B5=Button(a,text="Hello",width=15,height=5,fg="blue",bg="yellow",command=func1,relief=RAISED)

B1.pack(side=TOP,fill=X,padx=10,ipadx=40,ipady=30) # fille whole width with button color, padx is for padding ipad is for internal padding
B2.pack(side=TOP,fill=BOTH,expand=1) # for expanding the button, By defualt expnd is 0
B3.pack(side=TOP)
B4.pack(side=LEFT)
B5.pack(side=RIGHT)
a=mainloop()


# ## GUI in rows and column wise

# In[87]:


from tkinter import *
from tkinter import messagebox
i=0
def newwindow():

    global a
    a1.destroy()
    a= Tk()
    a.title("Page2")
    a.geometry("500x500+450+100")
    B2=Button(a,text="Hello",width=15,height=5,fg="blue",bg="yellow",command=home1,relief=GROOVE)
    B2.pack(side=TOP,fill=X,padx=10,ipadx=40,ipady=30) # fille whole width with button color, padx is for padding ipad is for internal padding
    a.mainloop()

def home1():
    global a1
    global i
    i=i+1
    if i>1:
        a.destroy()
    a1= Tk()
    a1.title("Page1")
    a1.geometry("500x500+450+100")
    B1=Button(a1,text="Hello",width=15,height=5,fg="blue",bg="yellow",command=newwindow,relief=GROOVE)
    B1.pack(side=TOP,fill=X,padx=10,ipadx=40,ipady=30) # fille whole width with button color, padx is for padding ipad is for internal padding
    a1.mainloop()


# In[88]:


home1()


# ### Grid View

# In[29]:


from tkinter import *
from tkinter import messagebox
#import tkMessageBox
a= Tk()
a.title("shopping Cart")
a.geometry("700x500+450+100")
def func1():
    messagebox.showinfo("Say hello"," Hellow World")
B1=Button(a,text="Hello",width=15,height=5,fg="blue",bg="yellow",command=func1,relief=GROOVE)
B2=Button(a,text="Hello",width=15,height=5,fg="blue",bg="red",command=func1,relief=RIDGE)
B3=Button(a,text="Hello",width=15,height=5,fg="blue",bg="yellow",command=func1,relief=FLAT)
B4=Button(a,text="Hello",width=15,height=5,fg="blue",bg="yellow",command=func1,relief=SUNKEN)
B5=Button(a,text="Hello",width=15,height=5,fg="blue",bg="yellow",command=func1,relief=RAISED)
B6=Button(a,text="Hello",width=15,height=5,fg="blue",bg="yellow",command=func1,relief=GROOVE)
B7=Button(a,text="Hello",width=15,height=5,fg="blue",bg="red",command=func1,relief=RIDGE)
B8=Button(a,text="Hello",width=15,height=5,fg="blue",bg="yellow",command=func1,relief=FLAT)
B9=Button(a,text="Hello",width=15,height=5,fg="blue",bg="yellow",command=func1,relief=SUNKEN)
B10=Button(a,text="Hello",width=15,height=5,fg="blue",bg="yellow",command=func1,relief=RAISED)
B11=Button(a,text="Hello",width=15,height=5,fg="blue",bg="yellow",command=func1,relief=GROOVE)
B12=Button(a,text="Hello",width=15,height=5,fg="blue",bg="red",command=func1,relief=RIDGE)
B13=Button(a,text="Hello",width=15,height=5,fg="blue",bg="yellow",command=func1,relief=FLAT)

B1.grid(row=0,column=0,rowspan=2)
B2.grid(row=0,column=1,columnspan=2)
B3.grid(row=0,column=3,rowspan=2)
B4.grid(row=1,column=1)
B5.grid(row=1,column=2)
B6.grid(row=2,column=0)
B7.grid(row=2,column=1)
B8.grid(row=2,column=2)
B9.grid(row=2,column=3)
B10.grid(row=3,column=0)
B11.grid(row=3,column=1)
B12.grid(row=3,column=2)
B13.grid(row=3,column=3)

a=mainloop()


# # Assignment -> Table using GUI grid in python

# In[127]:


from tkinter import *
from tkinter import messagebox

window=Tk()
window.geometry("700x900+300+100")
window.title("Assigment") 

def message():
    messagebox.showinfo("Hello","Under Construction")
    
   

B1=Button(window,text="Hello",width=10,height=15,fg="blue",bg="yellow",command=message,relief=GROOVE)
B2=Button(window,text="Hello",width=54,height=4,fg="blue",bg="yellow",command=message,relief=GROOVE)
B3=Button(window,text="Hello",width=40,height=4,fg="blue",bg="yellow",command=message,relief=GROOVE)
B4=Button(window,text="Hello",width=18,height=5,fg="blue",bg="yellow",command=message,relief=GROOVE)
B5=Button(window,text="Hello",width=18,height=5,fg="blue",bg="yellow",command=message,relief=GROOVE)
B6=Button(window,text="Hello",width=10,height=10,fg="blue",bg="yellow",command=message,relief=GROOVE)
B7=Button(window,text="Hello",width=10,height=7,fg="blue",bg="yellow",command=message,relief=GROOVE)
B8=Button(window,text="Hello",width=18,height=7,fg="blue",bg="yellow",command=message,relief=GROOVE)
B9=Button(window,text="Hello",width=18,height=7,fg="blue",bg="yellow",command=message,relief=GROOVE)
B10=Button(window,text="Hello",width=10,height=3,fg="blue",bg="yellow",command=message,relief=GROOVE)
B11=Button(window,text="Hello",width=10,height=3,fg="blue",bg="yellow",command=message,relief=GROOVE)
B12=Button(window,text="Hello",width=10,height=17,fg="blue",bg="yellow",command=message,relief=GROOVE)
B13=Button(window,text="Hello",width=18,height=5,fg="blue",bg="yellow",command=message,relief=GROOVE)
B14=Button(window,text="Hello",width=18,height=5,fg="blue",bg="yellow",command=message,relief=GROOVE)
B15=Button(window,text="Hello",width=10,height=11,fg="blue",bg="yellow",command=message,relief=GROOVE)
B16=Button(window,text="Hello",width=18,height=5,fg="blue",bg="yellow",command=message,relief=GROOVE)
B17=Button(window,text="Hello",width=18,height=5,fg="blue",bg="yellow",command=message,relief=GROOVE)
B18=Button(window,text="Hello",width=18,height=5,fg="blue",bg="yellow",command=message,relief=GROOVE)
B19=Button(window,text="Hello",width=18,height=5,fg="blue",bg="yellow",command=message,relief=GROOVE)
B20=Button(window,text="Hello",width=10,height=6,fg="blue",bg="yellow",command=message,relief=GROOVE)



B1.grid(row=0,column=0,rowspan=3)
B2.grid(row=0,column=1,columnspan=4)
B3.grid(row=1,column=1,columnspan=2)
B4.grid(row=2,column=1)
B5.grid(row=2,column=2)
B6.grid(row=1,column=3,columnspan=2,rowspan=2)
B7.grid(row=3,column=0,rowspan=2)
B8.grid(row=3,column=1,rowspan=2)
B9.grid(row=3,column=2,rowspan=2)
B10.grid(row=3,column=3,columnspan=2)
B11.grid(row=4,column=3,columnspan=2)
B12.grid(row=5,column=0,rowspan=6)
B13.grid(row=5,column=1,rowspan=1)
B14.grid(row=5,column=2,rowspan=1)
B15.grid(row=5,column=3,columnspan=2,rowspan=3)
B16.grid(row=7,column=1,rowspan=1)
B17.grid(row=7,column=2,rowspan=1)
B18.grid(row=8,column=1,rowspan=2)
B19.grid(row=8,column=2,rowspan=2)
B20.grid(row=8,column=3,columnspan=2,rowspan=3)
window.mainloop()
    
    


# In[ ]:




