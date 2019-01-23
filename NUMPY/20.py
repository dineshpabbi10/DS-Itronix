import numpy as np 
a = np.array([[1,2,3],[3,4,5],[4,5,6]]) 

print 'Our array is:' 
print a 
print '\n'  

# this returns array of items in the second column 
print 'The items in the second column are:'  
print a[...,1] 
print '\n'  

# Now we will slice all items from the second row 
print 'The items in the second row are:' 
print a[1,...] 
print '\n'  

# Now we will slice all items from column 1 onwards 
print 'The items column 1 onwards are:' 
print a[...,1:]
