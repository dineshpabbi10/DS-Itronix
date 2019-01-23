import numpy as np 
x = np.linspace(10,20,5) 
print x
x = np.linspace(10,20,3) 
print x

x = np.linspace(1,2,5, retstep = True) 
print x 
# retstep here is 0.25
#(array([1.  , 1.25, 1.5 , 1.75, 2.  ]), 0.25)

