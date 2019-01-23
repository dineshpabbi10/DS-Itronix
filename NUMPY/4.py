# dtype parameter 
import numpy as np 
a = np.array([1, 2, 3], dtype = complex) 
print a
a = np.array([1, 2, 3], dtype = int) 
print a
a = np.array([1, 2, 3], dtype = float) 
print a

"""Output : [1.+0.j 2.+0.j 3.+0.j]
      	    [1 2 3]
	    [1. 2. 3.]
"""

