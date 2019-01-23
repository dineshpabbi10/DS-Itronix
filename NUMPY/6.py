# using array-scalar type 
import numpy as np 
dt = np.dtype(np.int32) 
print dt

#int8, int16, int32, int64 can be replaced by equivalent string 'i1', 'i2','i4', etc. 
dt = np.dtype('i1')
print dt 
dt = np.dtype('i2')
print dt 
dt = np.dtype('i4')
print dt 
dt = np.dtype('i8')
print dt 
