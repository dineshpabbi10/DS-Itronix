#The resultant selection is an ndarray object containing corner elements.
import numpy as np 
x = np.array([[0,1,2,4],[3,4,5,6],[6,7,8,9],[9,10,11,12]]) 
   
print 'Our array is:' 
print x 
print '\n' 

rows = np.array([[0,0],[3,3]])
print rows
cols = np.array([[0,3],[0,3]])
print cols 
y = x[rows,cols] 
   
print 'The corner elements of this array are:' 
print y
