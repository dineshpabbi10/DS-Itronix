import numpy as np  
a = np.array([[30,17,15],[19,90,16],[69,53,21]]) 

print 'Our array is:' 
print a 
print '\n'

print 'Applying sort() function:' 
print np.sort(a) 
print '\n' 
print np.sort(a,axis=1)
print np.sort(a,axis=0)

  
# Order parameter in sort function 
dt = np.dtype([('name', 'S10'),('age', int)]) 
a = np.array([("Karan",21),("Arpit",25),("Ashish", 17), ("Sam",27),("Robin",22)], dtype = dt) 

print 'Our array is:' 
print a 
print '\n'  

print 'Order by name:' 
print np.sort(a, order = 'name')

print 'Order by age:' 
print np.sort(a, order = 'age')
