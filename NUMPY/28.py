import numpy as np 
print 'Invert of 13 where dtype of ndarray is uint8:' 
print np.invert(np.array([13], dtype = np.uint8)) 
print '\n'  
# Comparing binary representation of 13 and 242, we find the inversion of bits 

print 'Binary representation of 13:' 
print np.binary_repr(13, width = 5) 
print '\n'  

print 'Binary representation of 242:' 
print np.binary_repr(242, width = 8)
