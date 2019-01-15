#!/usr/bin/env python
# coding: utf-8

# #    Print N Numbers

# In[19]:


n=int(input("Enter the Number"))
for i in range(1,n+1):
    print(i,end=" ")


# # Sum of N Numbers.

# In[2]:


sum=0
n=int(input("Enter the Number"))
for i in range(1,n+1):
    sum+=i
print("Sum is ",sum)


# # Factorial of Given Number.

# In[3]:


factorial=1
n=int(input("Enter the Number"))
for i in range(n,1,-1):
    factorial*=i
print("Factorial is ",factorial)


# # SUM of the Digits.

# In[11]:


n=int(input("Please Enter the Number"))
sumf=0
temp=0
while n!=0:
    temp=n%10
    sumf+=temp
    n=n//10
print("Sum of the Digits are ",sumf)


# # Reverse of the Digits.

# In[13]:


n=int(input("Please Enter the Number"))
rev=0

while n!=0:
    rev=rev*10+ n%10
    n=n//10
print("Reverse of the Digits are ",rev)


# # Palindrome Checker

# In[16]:


n=int(input("Please Enter the Number"))
rev=0
temp=n
while n!=0:
    rev=rev*10+ n%10
    n=n//10
if rev is temp:
    print("It is a palindrome Number")
else:
    print("It is not a Palindrome Number")


# # Fibonacci Series upto n

# In[21]:


a=0
b=1
c=a+b
n=int(input("Please Enter the Number"))
print(a,end=" ")
print(b,end=" ")
print(c,end=" ")
for i in range(3,n+1):
    a=b
    b=c
    c=a+b
    print(c,end=" ")


# # Patterns

# In[183]:


n=int(input("Please Enter the Number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
#Reverse Pattern
print()
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
print()

k=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(k,end=" ")
        k+=1
    print()
print()

#Pascal's Triangle

r=1
for i in range(n,0,-1):
    print(end=" ")
print("1")
for i in range(n,1,-1):
    for k in range(i,1,-1):
        print(end=" ")
    for j in range(1,r+2):
        print(j,end="")

    for j in range(r,0,-1):
        print(j,end="")
    r+=1
    
    print()
    
print()

r=1
for i in range(n,0,-1):
    print(end=" ")
print("*")
for i in range(n,1,-1):
    for k in range(i,1,-1):
        print(end=" ")
    for j in range(1,r+2):
        print("*",end="")

    for j in range(r,0,-1):
        print("*",end="")
    r+=1
    
    print()
    
print()

#Half diamond
k=1
temp=n
for i in range(1,2*n):
    print("*",end=" ")
print()
for i in range(n,1,-1):
    for j in range(i-1,0,-1):
        print("*",end=" ")
    for j in range(1,2*k):
        print(end=" ")
    for j in range(1,2*k):
        print(end=" ")
    for j in range(i-1,0,-1):
        print("*",end=" ")
    k+=1
    print()

print()
   

k=1
temp=2
for i in range(n,0,-1):
    print(i,end=" ")
for i in range(2,n+1):
    print(i,end=" ")
print()
for i in range(n,1,-1):
    for j in range(i-1,0,-1):
        print(j,end=" ")
    for j in range(1,2*k):
        print(end=" ")
    for j in range(1,2*k):
        print(end=" ")
    for j in range(1,i):
        print(j,end=" ")
    k+=1
    print()

    #Full Diamond
print()

r=1
for i in range(2*n,0,-1):
    print(end=" ")
print("*")
for i in range(n,1,-1):
    for k in range(i,1,-1):
        print(end="  ")
    for j in range(1,r+2):
        print("*",end=" ")

    for j in range(r,0,-1):
        print("*",end=" ")
    r+=1
    
    print()
r=n-1
for i in range(1,n):
    for j in range(1,i+2):
        print(end="  ")
    for j in range((2*r)-1,0,-1):
        print("*",end=" ")
    r-=1
    print()
print()

#Empty Diamond
print()
   

k=1
temp=2
for i in range(n,0,-1):
    print("*",end=" ")
for i in range(2,n+1):
    print("*",end=" ")
print()
for i in range(n,1,-1):
    for j in range(i-1,0,-1):
        print("*",end=" ")
    for j in range(1,2*k):
        print(end=" ")
    for j in range(1,2*k):
        print(end=" ")
    for j in range(1,i):
        print("*",end=" ")
    k+=1
    print()
r=n-2
for i in range(2,n):
    for j in range(1,i+1):
        print("*",end=" ")
    for j in range(2*r,1,-1):
        print(end="  ")
    #for j in range(2*r,0,-1):
     #   print(end=" ")
    r-=1
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(n,0,-1):
    print("*",end=" ")
for i in range(2,n+1):
    print("*",end=" ") 
    
    


# In[ ]:




