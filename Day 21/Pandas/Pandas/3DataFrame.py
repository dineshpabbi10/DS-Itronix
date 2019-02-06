"""A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns.
Features of DataFrame

    Potentially columns are of different types
    Size : Mutable
    Labeled axes (rows and columns)
    Can Perform Arithmetic operations on rows and columns

A pandas DataFrame can be created using the following constructor :
pandas.DataFrame( data, index, columns, dtype, copy)

Create DataFrame
A pandas DataFrame can be created using various inputs like :
    Lists
    dict
    Series
    Numpy ndarrays
    Another DataFrame

"""
#import the pandas library and aliasing as pd
#Create an Empty DataFrame
import pandas as pd
df = pd.DataFrame()
print df

#Create a DataFrame from Lists
data = [10,20,30,40,50]
df = pd.DataFrame(data)
print df

data = [['Robin',26],['Kevin',25],['Curil',23]]
df = pd.DataFrame(data,columns=['Name','Age'])
print df

data = [['Alex',10,20],['Bob',12,20],['Clarke',13,65]]
df = pd.DataFrame(data,columns=['Name','Age','Marks'],dtype=float)
print df
print df['Name']
