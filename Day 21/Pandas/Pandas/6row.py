import pandas as pd

d = {'one' : pd.Series([11, 21, 31], index=['a', 'b', 'c']), 
     'two' : pd.Series([11, 22, 33, 44], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print df
print df.loc['b']

print "\n-----Selection by integer location-----"
#Rows can be selected by passing integer location to an iloc function.
df = pd.DataFrame(d)
print df.iloc[1]
print "Multiple rows can be selected using  :  operator."
print df[2:4]

print "\n<<-----Addition of Rows----->>"
df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
print "Row1\n",df
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])
print "Row2\n",df2
print "\nAppend"
df = df.append(df2)
print df

print "\nDrop rows with label 0"
df = df.drop(0)

print df
