#!/usr/bin/env python
# coding: utf-8

# # Random Module

# ### random.random()-> returns any float between 0-1
# ### random.randrange(a), random.randrange(a,b), random.randrange(a,b,mutiple)
# ### random.choice(list[])-> returns random element
# ### random.uniform(a,b)
# ### random.shuffle(list[])
# 
# 

# In[12]:


import random

print(random.random())
print(random.randrange(1000))
print(random.randrange(1000,10000))
print(random.randrange(1000,10000,13))
print(random.choice([1,2,3,4,5,6]))
print(random.uniform(10,20))
l=[1,2,3,4,5,6]
random.shuffle(l)
print(l)


# # Operating System Module

# In[17]:


import os
os.system("mkdir tempDir")
os.system("cd tempDir")   ## not working yet in ubuntu
os.system("mkdir newDir")

"""
Executing a shell command
os.system()    

Get the users environment 
os.environ()   

#Returns the current working directory.
os.getcwd()   

Return the real group id of the current process.
os.getgid()       

Return the current process’s user id.
os.getuid()    

Returns the real process ID of the current process.
os.getpid()     

Set the current numeric umask and return the previous umask.
os.umask(mask)   

Return information identifying the current operating system.
os.uname()     

Change the root directory of the current process to path.
os.chroot(path)   

Return a list of the entries in the directory given by path.
os.listdir(path) 

Create a directory named path with numeric mode mode.
os.mkdir(path)    

Recursive directory creation function.
os.makedirs(path)  

Remove (delete) the file path.
os.remove(path)    

Remove directories recursively.
os.removedirs(path) 

Rename the file or directory src to dst.
os.rename(src, dst)  

Remove (delete) the directory path.
os.rmdir(path)

"""
### cmd basic commands can be executed using os library


# # Maths Module

# In[18]:


import math
print(math.ceil(-145.67))
print(math.ceil(145.17))
print(math.floor(-145.67))
print(math.floor(145.67))
print(max(1,2,3,4,5))
print(min(12,3,4,5))
print(math.pow(5,4))
print(math.sqrt(49))


# In[19]:


a=12
b=45
print ("a is %d and b is %d"%(a,b))


# # String Operations.

# In[29]:


a="hello mr. johny"
print(a.capitalize())
print(a.upper())
print(a.lower())
print(a.center(80,"-")) ## To decorate the String 

b='1234'
c='1234.5'

print(b.isdigit())
print(b.isdigit())


s="This is a string"
print(s.count('i'))

d="this is a string"
print(s.replace(' is'," was"))

f="This is a String"
print(f.swapcase())


# # List Operation
# 
# #### del list[index]
# #### list.append()
# #### cmp(list1,lis2)
# #### list.index(element)
# #### list.insert(index,value)
# #### list.count(element)
# #### len(list)
# #### max(list) ->  return max element
# #### list.remove(element)
# #### list.reverse()
# #### list.sort()
# 
# #### a=list(tupple) ->  conver tupple into list  Mutable
# #### b=tupple(list) ->  convert list into tupple Immutabe
# 
# #### 
# 

# In[29]:


myList=[1,2,3,4,5,6,7]
newList=[1,2,3,4,5,6,7]
del myList[4]
print(myList)

myList.append(8)
print(myList)

#print(cmp(myList,newList)) only in python2

print(myList.index(2))

myList.insert(4,5)
print(myList)

print(myList.count(2))
print(len(myList))

print(max(myList))
print(min(myList))

myList.remove(8)
print(myList)

myList.reverse()
print(myList)

myList.sort()
print(myList)

tup=tuple(myList)
print(tup)

l=list(tup)
print(l)

