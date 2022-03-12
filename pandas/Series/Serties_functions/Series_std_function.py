"""
Refernce:

"""
import pandas as pd
import numpy as np
data=[[1,0.1,1],[2,0.2,2],[3,0.3,9],[4,0.4,16],[5,0.5,25],[6,0.6,36]]
df=pd.DataFrame(data,columns=['int','float','power'])

print("==========================================================================")
print("pandas Series.std() function applications")
print("std() is a function for calculating the standard deviation of the given set of numbers, DataFrame, column, and rows.")
print("The standard deviation is normalized by N-1 by default and can be changed using the ddof argument.")
print("=============")
#std:standerd deviation
#std Formula:
print("the std function of df DataFrame:\n",df.std())
print("parameters of std function:")
print("axis\nskipna\nlevel\nddof\nnumeric_only")
"""
parameters of std function:
1.axis
2.skipna
3.level
4.ddof
5.numeric_only
"""
print("========================================================================")
print("working with std finction")
print("axis:")
#df.std(axis=True)=df.std(axis=1)
#df.std(axis=False)=df.std(axis=0)
print("axis=True of df DataFrame:\n",df.std(axis='index'))
print("axis=False of df DataFrame:\n",df.std(axis='columns'))
"""
output:

"""
print("============")
print("skipna:")
#df.std(skipna=True)=df.std(skipna=1)
#df.std(skipna=False)=df.std(skipna=0)
print("skipna=True of df DataFrame:\n",df.std(skipna=1))
print("skipna=False of df DataFrame:\n",df.std(skipna=False))

print("============")
print("level:")
print("============")
print("ddof:")
print("============")
print("numeric_only:")

