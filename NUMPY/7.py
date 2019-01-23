import numpy as np 
student = np.dtype([('name','s20'), ('age', 'i1'), ('marks', 'f4')]) 
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student) 
print a
print a[0]
print a[0,1]
