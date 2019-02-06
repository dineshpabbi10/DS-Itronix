import pandas as pd
import numpy as np
d={'Name':pd.Series(['Akshay','Rajat','Robin','Kapil','James','Cyril']),'Age':pd.Series([25,26,29,27,23,21]),'Rating':pd.Series([4.23,2.35,1.56,3.20,4.62,3.99])}
df=pd.DataFrame(d)
print df
#print "Sum of All the Data Frame",df.sum()
#print "Sum of All the Age",df['Age'].sum()
print "Sum of All the Age",df['Age'].mean()
print "Sum of All the Age",df['Age'].std()
print "Sum of All the Age",df['Age'].count()
print "Sum of All the Age",df['Age'].min()
print "Sum of All the Age",df['Age'].max()
print "Sum of All the Age",df['Age'].prod()
print "Sum of All the Age",df['Age'].median()
print "Sum of All the Age",df['Age'].cumsum()
print "Sum of All the Age",df['Age'].cumprod()

#print "\nHead\n",df.head(2)
#print "\nTail\n",df.tail(2)
#print df.shape
#print df.T  #Transpose of Data Frame

