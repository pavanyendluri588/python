"""
Refernce:

"""
import pandas as pd
import numpy as np
s=pd.Series(['pavan','rama','venkat','prudhvi','raviteja','prassana','priya',np.nan,'anil','dharma','ashok','siva','sudhir'],name='names')
print("=======================================================================")
print("series map():")
print("s Series:\n",s)
print("=======================================================================")
"""
parameters of map:
1.arg:
2.na_action:If ‘ignore’, propagate NaN values, without passing them to the mapping correspondence.
"""
print("======================================================================")
print("working with map function:map accepts a dict or a Series. Values that are not found in the dict are converted to NaN, unless the dict has a default value")
print("s.map({'pavan':'pavanramchandar','prudhvi':'prudhviramchandar'}):\n",s.map({'pavan':'pavanramchandar','prudhvi':'prudhviramchandar'}))
"""
output:
s.map({'pavan':'pavanramchandar','prudhvi':'prudhviramchandar'}):
 0       pavanramchandar
1                   NaN
2                   NaN
3     prudhviramchandar
4                   NaN
5                   NaN
6                   NaN
7                   NaN
8                   NaN
9                   NaN
10                  NaN
11                  NaN
12                  NaN
Name: names, dtype: object
"""
print("=============================")
print("map also accepts a function:")
print("s.map('my name is {}'.format):\n",s.map('my name is {}'.format))
"""
output:
map also accepts a function:
s.map('my name is {}'.format):
 0        my name is pavan
1         my name is rama
2       my name is venkat
3      my name is prudhvi
4     my name is raviteja
5     my name is prassana
6        my name is priya
7          my name is nan
8         my name is anil
9       my name is dharma
10       my name is ashok
11        my name is siva
12      my name is sudhir
Name: names, dtype: object
"""
print("======================================================================")
print("using the parameter na_action:by default na_action is in None means it will pass all nan/Null values also,na_action='ignore' means it will not allow nan/Null values")
print(s.map('my name is {}'.format,na_action='ignore'))
"""
output:
using the parameter na_action:by default na_action is in None means it will pass all nan/Null values also,na_action='ignore' means it will not allow nan/Null values
0        my name is pavan
1         my name is rama
2       my name is venkat
3      my name is prudhvi
4     my name is raviteja
5     my name is prassana
6        my name is priya
7                     NaN
8         my name is anil
9       my name is dharma
10       my name is ashok
11        my name is siva
12      my name is sudhir
Name: names, dtype: object
"""
print("====================================================================")
print("arg parameter in map function:")
