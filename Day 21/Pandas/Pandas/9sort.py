import pandas as pd
import numpy as np
data=pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns=['col2','col1'])
print data
a="Data in Ascending Order\n",data.sort_index()   #Asc Order
print a
b="Print Data in Des Order\n",data.sort_index(ascending=False)
print b
c=data.sort_values(by='col1',kind='mergesort')
print c

#kind : {quicksort, mergesort, heapsort}


