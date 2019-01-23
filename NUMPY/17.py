# obtain iterator object from list 
import numpy as np 
list = range(5) 
it = iter(list)  

# use iterator to create ndarray 
x = np.fromiter(it, dtype = float) 
print x
