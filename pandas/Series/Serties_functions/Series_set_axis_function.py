"""
Resources:
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.set_axis.html

"""
import pandas as pd
import numpy as np
print("================================================================")
print("python Series set_axis():this function is used for the changing indexes ")

s=pd.Series(['a','b','c','d','e'])
index_=[0,1,2,3,4]
s.index=index_
print("Series s:\n",s)
print("=================================================================")
"""
parameters of set_axis:
1.labels
2.axis
3.inplace
"""
print("parameters of set_axis():")
print("1.labels\n2.axis\n")
print("3.inplace:this is used to decide the changes want to done in orginal series or in now operating series")
print("inplace=0 or inplace='index' :means the operations will work on the rows")
print("inplace=1 or inplace='columns' :means the operations will work on the columns  #but Series does not have columns")
print(s.set_axis([11,22,33,44,55],axis='index'))
"""
output:
================================================================
python Series set_axis():this function is used for the changing indexes
Series s:
 0    a
1    b
2    c
3    d
4    e
dtype: object
=================================================================
parameters of set_axis():
1.labels
2.axis

3.inplace:this is used to decide the changes want to done in orginal series or in now operating series
inplace=0 or inplace='index' :means the operations will work on the rows
inplace=1 or inplace='columns' :means the operations will work on the columns  #but Series does not have columns
11    a
22    b
33    c
44    d
55    e
dtype: object
"""