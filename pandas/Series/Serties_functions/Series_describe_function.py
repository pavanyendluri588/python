import pandas as pd
import numpy as np 
print("================================================================")
print("pandas Series describe()")

print("series.describe Returns : Summary statistics of the Series")
print("=================================================================")
print("parameters of describe finction:")
print("1.percentiles\n2.include\n3.exclude\n4.datetime_is_numeric")
s=pd.Series([1,None,3,4,5,None,7,8,None])
index_=[9,8,7,6,5,4,3,2,1]
s1=pd.Series(['p','a','n','d','a','s'])
s.index=index_
print("s:\n",s)
"""
parameters of describe finction:
1.percentiles
2.include
3.exclude
4.datetime_is_numeric

"""
print("s.describe():\n",s.describe())
"""
output:
.describe():
 count    6.000000
mean     4.666667
std      2.581989
min      1.000000
25%      3.250000
50%      4.500000
75%      6.500000
max      8.000000
dtype: float64
"""
print("describe for categorical values:")
print("s1:\n",s1)
print("s1.describe():\n",s1.describe())


