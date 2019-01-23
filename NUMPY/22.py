import numpy as np 

x = np.array([[1,2,3], [4,5,6], [7,8,9]]) 
print x
y = x[[0,1,2], [0,1,2]] 
#The selection includes elements at (0,0), (1,1) and (2,0) from the first array.
print "Diagonal Elements\n"
print y

#Output :[1 5 9] : Print Diagonal Elements
