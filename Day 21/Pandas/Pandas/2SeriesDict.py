#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
data = {'x' : 10., 'y' : 11., 'z' : 12.}
s = pd.Series(data)
print s

data = {'a1' : 10, 'a2' : 11, 'a3' : 12}
s = pd.Series(data)
print s["a1":"a2"]

data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data,index=['b','c','d','a'])
print s
"""Index order is persisted and the missing element is filled with NaN (Not a Number)."""

s = pd.Series(5, index=[0, 1, 2, 3])
print s

s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print s

#retrieve the first element
print s[0]
print s[:3]
#retrieve the last three element
print s[-3:]
#retrieve multiple elements
print s[['a','c','d']]

#retrieve non exist elements
#print s['f']

