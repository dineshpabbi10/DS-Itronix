# convert list to ndarray 
import numpy as np 

x = [1,2,3] 
a = np.asarray(x) 
print a

print "-------------------"
# dtype is set 
x = [1,2,3]
a = np.asarray(x, dtype = float) 
print a

print "-------------------"
# ndarray from list of tuples 
x = (1,2,3) 
a = np.asarray(x) 
print a

print "-------------------"
# ndarray from list of tuples 
x = [(1,2,3),(4,5)] 
a = np.asarray(x) 
print a
