import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
index = pd.date_range('24/6/2018', periods=10),
columns = ['A', 'B', 'C', 'D'])
print df

print pd.date_range('24/04/2018', periods=5)
print pd.date_range('1/1/2011', periods=5,freq='M')
