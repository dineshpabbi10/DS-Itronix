import pandas as pd
import numpy as np

s = pd.Series(['Katrina','Raman','Jessica','Albert','1234','Smith'])
print s

print s.str.lower()
print s.str.upper()
print s.str.len()
print s.str.contains('a')
print s.str.replace('a','@')
print s.str.repeat(2)
print s.str.count('a')
print s.str. startswith ('S')
print s.str.endswith('t')
print s.str.find('n')
print s.str.findall('e')
print s.str.swapcase()
print s.str.islower()
print s.str.isupper()
print s.str.isnumeric()


