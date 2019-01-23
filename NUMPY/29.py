import numpy as np 
a = np.arange(12).reshape(3,4) 

print 'The original array is:' 
print a  
print '\n' 

print 'The transposed array is:' 
print np.transpose(a)
print a.T  # Same Result
