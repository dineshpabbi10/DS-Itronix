import pandas as pd
print "<-----Column Addition----->"
d = {'one' : pd.Series([1, 2, 3]),
      'two' : pd.Series([1, 2, 3, 4])}

df = pd.DataFrame(d)

# Adding a new column to an existing DataFrame object with column label by passing new series

print ("Adding a new column by passing as Series:")
df['three']=pd.Series([10,20,30])
print df

print ("Adding a new column using the existing columns in DataFrame:")
df['four']=df['one']+df['three']

print df
print df[['one','two']] #Print Particular Column

print "\n Delete any Particular Column"
# using del function
print ("Deleting the first column using DEL function:")
del df['one']
print df

# using pop function
print ("Deleting another column using POP function:")
df.pop('two')
print df

