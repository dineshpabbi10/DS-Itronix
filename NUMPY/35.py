import numpy as np 
a = np.array([[1,2,3],[3,4,5],[4,5,6]]) 

print 'Our array is:' 
print a 
print '\n'  

print 'Applying mean() function:' 
print np.mean(a) 
print '\n'  

print 'Applying mean() function along axis 0:' 
print np.mean(a, axis = 0) 
print '\n'  

print 'Applying mean() function along axis 1:' 
print np.mean(a, axis = 1)
