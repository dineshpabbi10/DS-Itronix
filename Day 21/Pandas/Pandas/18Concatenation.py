import pandas as pd
one = pd.DataFrame({
         'Name': ['Akash', 'Abhishek', 'Arpit', 'aayush', 'Ankit'],
         'subject':['sub1','sub2','sub4','sub6','sub5'],
         'Marks':[98,90,87,69,78]},
         index=[1,2,3,4,5])
two = pd.DataFrame({
         'Name': ['Bobby', 'Bhavnish', 'Bhavya', 'Bonny', 'Brett'],
         'subject':['sub2','sub4','sub3','sub6','sub5'],
         'Marks':[89,80,79,97,88]},
         index=[1,2,3,4,5])
print "\n",pd.concat([one,two])
print "\n",pd.concat([one,two],keys=['x','y']) #The index of the resultant is duplicated; each index is repeated.
print "\n",pd.concat([one,two],ignore_index=True)
print "\n",pd.concat([one,two],axis=1)
print "\n",one.append(two)
print "\n",one.append([two,one,two])
print "\n",pd.datetime.now()
print "\n",pd.date_range("11:00", "13:30", freq="30min").time
print "\n",pd.date_range("11:00", "13:30", freq="H").time


Operations on multiple dataframes
Description
Given three data frames containing the number of gold, silver, and bronze Olympic medals won by some countries, determine the total number of medals won by each country. 
Note: All the three data frames don’t have all the same countries. So, ensure you use the ‘fill_value’ argument (set it to zero), to avoid getting NaN values. Also, ensure you sort the final dataframe, according to the total medal count in descending order.
import numpy as np 
import pandas as pd

# Defining the three dataframes indicating the gold, silver, and bronze medal counts
# of different countries
gold = pd.DataFrame({'Country': ['USA', 'France', 'Russia'],
                         'Medals': [15, 13, 9]}
                    )
silver = pd.DataFrame({'Country': ['USA', 'Germany', 'Russia'],
                        'Medals': [29, 20, 16]}
                    )
bronze = pd.DataFrame({'Country': ['France', 'USA', 'UK'],
                        'Medals': [40, 28, 27]}
                    )

data=gold.append([silver,bronze],ignore_index=True).groupby('Country').sum()
c=data.sort_values(by='Medals',ascending=False)
c=pd.DataFrame(c,dtype=float)
print(c)