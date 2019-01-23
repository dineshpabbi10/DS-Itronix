import numpy as np 
x = np.arange(9).reshape(3, 3) 

print 'Our array is:' 
print x  

# define a condition 
condition = np.mod(x,2) == 0 

print 'Element-wise value of condition' 
print  condition 

print 'Extract elements using condition' 
print np.extract(condition, x)

#another method
print 'Element-wise value of condition' 
print x[condition]  
