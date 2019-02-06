"""Indexing	Description
.loc()	Label based
.iloc()	Integer based
.ix()	Both Label and Integer based"""

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10,5), index =['a','b','c','d','e','f','g','h','i','j'], columns = ['A','B','C','D','E'])
print df
#select all rows for a specific column
print df.loc[:,'A']
print df.loc[:,'A':'C']
print df.loc[:,['A','C']]

# Select few rows for multiple columns, say list[]
print df.loc[['a','b','f','h'],['A','C']]
print df.loc['a':'h']

# for getting values with a boolean array
print df.loc[['a','b']]>0

# select all rows for a specific column
print df.iloc[:4]
# Integer slicing
print df.iloc[1:5, 2:4]

print "\nSlicing through list of values\n"
print df.iloc[[1, 3, 5], [1, 3]]
print df.iloc[1:3, :]
print df.iloc[:,1:3]

# Integer slicing with ix - Hybrid
print df.ix[:4]
print df.ix[:,'A']

#Note:each operation can be performed on the DataFrame object. 
print df['A']
print df[['A','B']]
#Columns can be selected using the attribute operator '.'
print df.B

#reindex the DataFrame
df_reindexed = df.reindex(index=['a','c','d'], columns=['A', 'C', 'B'])
print df_reindexed


