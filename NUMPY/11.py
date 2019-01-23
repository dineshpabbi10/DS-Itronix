# dtype of array is int8 (1 byte) 
import numpy as np 
x = np.array([1,2,3,4,5], dtype = np.int8) 
print x.itemsize
print "------------------"
x = np.array([1,2,3,4,5], dtype = np.float32) 
print x.itemsize
