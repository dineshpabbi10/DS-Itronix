import numpy as np 
a = np.array([[1,2,3],[3,4,5],[5,6,7]]) 

print 'First array:' 
print a 
print '\n'  
b = np.array([[5,6,7],[7,8,9],[10,11,12]]) 

print 'Second array:' 
print b 
print '\n'  
# both the arrays are of same dimensions 

print 'Joining the two arrays along axis 0:' 
print np.concatenate((a,b)) 
print '\n'  

print 'Joining the two arrays along axis 1:' 
print np.concatenate((a,b),axis = 1)
