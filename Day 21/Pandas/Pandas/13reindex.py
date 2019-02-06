import pandas as pd
import numpy as np
df1 = pd.DataFrame(np.random.randn(10,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(7,3),columns=['col1','col2','col3'])
print "\nData Frame1\n",df1
print "\nData Frame2\n",df2
df1 = df1.reindex_like(df2)
print "\nNew Data Frame\n",df1

#Note : Here, the df1 DataFrame is altered and reindexed like df2. The column names should be matched or else NAN will be added for the entire column label.

df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])
print "\nData Frame1\n",df1
print "\nData Frame2\n",df2
# Padding NAN's
print df2.reindex_like(df1)

# Now Fill the NAN's with preceding Values
print ("Data Frame with Forward Fill:")
print "\nForward Fill\n",df2.reindex_like(df1,method='ffill')
print "\nBackward Fill\n",df2.reindex_like(df1,method='backfill')
print "\nNearest Fill\n",df2.reindex_like(df1,method='nearest')

print ("Data Frame with Forward Fill limiting to 1:")
print df2.reindex_like(df1,method='ffill',limit=2)

print "\nRenaming Rows and Columns\n"
df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
print df1

print ("After renaming the rows and columns:")
print df1.rename(columns={'col1' : 'c1', 'col2' : 'c2'},
index = {0 : 'Apple', 1 : 'Kiwi', 2 : 'Mango'})
