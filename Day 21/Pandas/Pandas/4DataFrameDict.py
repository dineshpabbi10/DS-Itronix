#DataFrame from Dict of ndarrays / Lists
import pandas as pd
data = {'Name':['Ayush', 'Priya', 'Kapil', 'Rohit'],'Age':[28,21,29,42]}
df = pd.DataFrame(data)

print "<<<------------------------------>>>"
df = pd.DataFrame(data,	 index=['rank1','rank2','rank3','rank4'])
print df

#Create a DataFrame from List of Dicts
print "<<<------------------------------>>>"
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print df
#Note : Observe, NaN (Not a Number) is appended in missing areas.

df = pd.DataFrame(data, index=['first', 'second'])
print df

#With two column indices, values same as dictionary keys
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])

#With two column indices with one index with other name
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
print df1
print df2

#Create a DataFrame from Dict of Series
print "\nDataFrame from Dict of Series"
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print df 

print "\nColumn Selection"
print df ['one']

