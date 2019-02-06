# import the pandas library
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
'h'],columns=['one', 'two', 'three'])
print df

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print df
print df['one'].isnull()
print df['one'].notnull()
print df['one'].sum()
"""When summing data, NA will be treated as Zero
If the data are all NA, then the result will be NA"""
print ("NaN replaced with '0':")
print df.fillna(0)
print df.dropna()

print"\n"
df = pd.DataFrame({'one':[10,2000,30,40,50,2000],
'two':[1000,0,30,40,50,60]})
print df
print df.replace({1000:10,2000:60})
print df[1:2]['one'].replace({NaN:10})
#print df[1:2]['one'].fillna(0)
#df=df.set_value('b','one',10)



#Find out the percentage of missing values in each column in the given dataset.
import pandas as pd
df = pd.read_csv('https://query.data.world/s/Hfu_PsEuD1Z_yJHmGaxWTxvkz7W_b0')
#print(round())#Round off percentage values to 2 decimial places. 
print(round(df.isnull().sum() * 100 / len(df),2))

#Remove the rows having greater than 5 missing values and then print the percentage of missing values in each column.
import pandas as pd
df = pd.read_csv('https://query.data.world/s/Hfu_PsEuD1Z_yJHmGaxWTxvkz7W_b0')
df=df.dropna(thresh=5)
print(round(df.isnull().sum() * 100 / len(df),2))