import pandas as pd
import numpy as np
data=pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns=['col2','col1'])
print data
pd.DataFrame(data).to_csv("output.csv")
