import numpy as np 
a = np.arange(10,20) 
print a

s = slice(2,7,2) #Start 2 -> End 7 -> inc 2 
#(start:stop:step) directly to the ndarray object.
print a[s]

#<-------------------------------->
#Same Result
a = np.arange(10,20) 
b = a[2:7:2] 
print b


a = np.arange(10) 
b = a[5] 
print b

a = np.array([[1,2,3],[3,4,5],[4,5,6]]) 
print a  

# slice items starting from index
print 'Now we will slice the array from the index a[1:]' 
print a[1:]
