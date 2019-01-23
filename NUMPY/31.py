import numpy as np 
a = np.arange(12) 

print 'First array:' 
print a 
print '\n'  

print 'Split the array in 3 equal-sized subarrays:' 
b = np.split(a,4) 
print b 
print '\n'  

print 'Split the array at positions indicated in 1-D array:' 
b = np.split(a,[4,7])
print b 
print b[0]
print b[0][0],b[0][1]
