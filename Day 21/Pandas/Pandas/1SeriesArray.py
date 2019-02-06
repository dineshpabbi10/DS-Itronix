"""import the pandas library and aliasing as pd : 
Author : Karan Arora :  iTronix Solutions

A Series is a one-dimensional object that can hold any data type such as integers, floats and strings.

pandas.Series( data, index, dtype, copy) 
1:data
data takes various forms like ndarray, list, constants
2:index
Index values must be unique and hashable, same length as data. Default np.arrange(n) if no index is passed.
3:dtype
dtype is for data type. If None, data type will be inferred\
4:copy
Copy data. Default False"""

import pandas as pd
import numpy as np

print "Program 1"
s = pd.Series()
print s

print "------------------------------------"
print "Program 2 : Create a Series from ndarray"
data = np.array(['a','b','c','d'])
print data
s = pd.Series(data)
print s
"""Here, data can be many different things:
        a Python dict
        an ndarray
        a scalar value (like 5)

If data is an ndarray, index must be the same length as data. If no index is passed, one will be created having values [0, ..., len(data) - 1].
"""
print "------------------------------------"
print "Program 3 : Create a Series from ndarray with Index"
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print s
print s[101]

print "------------------------------------"
print "Program 3 : Create a Random Series from ndarray with Index"
s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print s
print s[2]
print s['b']
print s.index

dates = pd.date_range('16/04/2018', periods=8)
print dates
