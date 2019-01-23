import numpy as np 
x = np.zeros((2,5,2), dtype = np.int) 
print x

print "---------------"
# custom type 
x = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'f4')])  
print x

print "---------------"
# array of five ones. Default dtype is float 
x = np.ones(5) 
print x

print "---------------"
import numpy as np 
x = np.ones([2,2], dtype = int) 
print x
