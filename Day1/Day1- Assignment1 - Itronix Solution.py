#!/usr/bin/env python
# coding: utf-8

# # Check if the number is +ve or not

# In[3]:


num=int(input("Please Enter the Number "))
if(num>0):
    print(num," is a positive number")
elif(num<0):
    print(num," is a negative number")
else:
    print(num," is neutral")


# # Greatest Numbers between two numbers.

# In[5]:


a=int(input(" Please Enter first Number "))
b=int(input(" Please Enter Second Number "))
if a>b:
    print(a," is greater than ",b)
else:
    print(b," is greater than ",a)


# # Greatest Between three Numbers.

# In[10]:


a=int(input("Please Enter first Number "))
b=int(input("Please Enter Second Number "))
c=int(input("Please Enter third Number "))
if a>b:
    if a>c:
        print(a," is greatest")
    else:
        print(c, "is greatest")
elif b>c:
    if b>a:
        print(b," is greatest")
    else:
        print(a, "is greatest")
elif c>a:
    if c>b:
        print(c," is greatest")
    else:
        print(b, "is greatest")


# # Check if number is Even or Odd.

# In[12]:


num=int(input("Please Enter the Number"))
if num % 2 ==0:
    print(num," is Even Number")
else:
    print(num," is Odd Number")


# # Check if number is Even or Odd (No Modulo Operator)

# In[15]:


num=int(input("Please Enter the Number"))
if num & 1 ==0:
    print(num," is Even Number")
else:
    print(num," is Odd Number")


# # Check if number is even or odd only if number >6

# In[19]:


num=int(input("Please Enter the Number"))
if num<6:
    print("Invalid Number")
else:
    if num & 1 ==0:
        print(num," is Even Number")
    else:
        print(num," is Odd Number")

