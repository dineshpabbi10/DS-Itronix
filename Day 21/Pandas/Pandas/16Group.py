#import the pandas library
import pandas as pd
import numpy as np
ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings','kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

print df
grouped = df.groupby('Year')
for name,group in grouped:
    print name
    print group
print "\n2014 Data\n",grouped.get_group(2014)

grouped = df.groupby('Year')
print grouped['Points'].agg(np.mean)
print grouped['Points'].agg(np.sum)
print grouped['Points'].agg(np.average)
