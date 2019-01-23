# this is one dimensional array 
import numpy as np 
a = np.arange(24) 
print a.ndim
  
print "1 Dimension:",a
print "-----------------"

# now reshape it 
b = a.reshape(4,3,2) 
print b
print b[0][0][0] # This i my 3D Array
b = a.reshape(6,4) 
print b 
# b is having three dimensions
