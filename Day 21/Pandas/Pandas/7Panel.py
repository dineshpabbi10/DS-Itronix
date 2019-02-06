"""A panel is a 3D container of data. The term Panel data is derived from econometrics and is partially responsible for the name pandas : pan(el)da(ta)s.

The names for the 3 axes are intended to give some semantic meaning to describing operations involving panel data. They are :

    items : axis 0, each item corresponds to a DataFrame contained inside.

    major_axis : axis 1, it is the index (rows) of each of the DataFrames.

    minor_axis : axis 2, it is the columns of each of the DataFrames.

pandas.Panel()

A Panel can be created using the following constructor :
pandas.Panel(data, items, major_axis, minor_axis, dtype, copy)
"""
import pandas as pd
import numpy as np
a=pd.DataFrame(np.random.randn(4, 3))
b=pd.DataFrame(np.random.randn(4, 2))

print "\nData Frame1 :\n",a
print "\nData Frame2 :\n",b

print "\n3D Panel Data from Data Frame :\n"
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print p['Item1']
print p['Item2']

print "\nAnother Method\n"
data1 = {'Item1' : a, 'Item2' : b}
p1 = pd.Panel(data1)
print p1
print p['Item1']
print p['Item2']
print p[:]
print "\nPrinting All Column 1\n",p.minor_xs(1)
print "\nPrinting All Row 1\n",p.major_xs(1)

