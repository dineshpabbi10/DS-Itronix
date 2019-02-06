# import the pandas library
import pandas as pd
df1 = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Piyush', 'Gautam', 'Garry', 'Abhishek', 'Ankit'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
df2 = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Saurabh', 'Akshay', 'Rajat', 'Ankush', 'Sam'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
print "\nData Frame 1\n",df1
print "\nData Frame 2\n",df2
print "\n",pd.merge(df1,df2,on='id')
print "\n",pd.merge(df1,df2,on=['id','subject_id'])
print "\n",pd.merge(df1,df2, on='subject_id', how='left')
print "\n",pd.merge(df1,df2, on='subject_id', how='right')
print "\n",pd.merge(df1,df2, on='subject_id', how='outer')
print "\n",pd.merge(df1,df2, on='subject_id', how='inner')
