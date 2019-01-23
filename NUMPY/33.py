import numpy as np 
a = np.array([[30,65,70],[80,95,10],[50,90,60]]) 

print 'Our array is:' 
print a 
print '\n'  

print 'Applying median() function:' 
print np.median(a) 
print '\n'  

print 'Applying median() function along axis 0:' 
print np.median(a, axis = 0) 
print '\n'  
 
print 'Applying median() function along axis 1:' 
print np.median(a, axis = 1)
