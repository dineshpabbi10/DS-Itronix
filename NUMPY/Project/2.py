import numpy as np
a = np.genfromtxt('data.csv', delimiter=',',dtype=str)
print(a)
print(a[0][2])
print (len(a))
print (a.shape)
m=np.where(a[...,4]=='Male')
f=np.where(a[...,4]=='Female')

male=a[m]
female=a[f]
np.savetxt("male.csv",male,fmt='%s',delimiter=",")
