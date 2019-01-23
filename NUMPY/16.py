import numpy as np 
s = 'Hello World' 
a = np.frombuffer(s, dtype = 'S1') 
print a[0]
