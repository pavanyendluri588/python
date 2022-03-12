import pandas as pd
import numpy as np
series=pd.Series(['p','a','n','d','a','s'])
print(series)
"""
output:-
0    p
1    a
2    n
3    d
4    a
5    s
dtype: object
-->series is one dimensional array.
-->The row labels are called 'index'.
we can easily convert the list,tuple,and dictonary  into series by using 'Series' method.
"""
#creating the array by using numpy
numpy1=np.array([1,2,3,4,5,6,7,8])
numpy2=np.array([8,7,6,5,4,3,2,1])
#series1=pd.Series(data=numpy1,name='numpy1')
series1=pd.Series([numpy1,numpy2])
print(series1)
"""
output:-
0    [1, 2, 3, 4, 5, 6, 7, 8]
1    [8, 7, 6, 5, 4, 3, 2, 1]
dtype: object
"""
emptyseries=pd.Series()
print(emptyseries)
"""
output:-
The default dtype for empty Series will be 'object' instead of 'float64' in a future version. Specify a dtype explicitly to silence this warning.
  emptyseries=pd.Series()
Series([], dtype: float64)
"""
print("==============================================================================================")
print("creating a series dict")
dict={1:'x',2:'y',3:'z'}
dict_series=pd.Series(dict)
print(dict_series)
"""

"""
print("===========================================================================")
print("creating the series using scalar")
print("If we take the scalar values, then the index must be provided. The scalar value will be repeated for matching the length of the index.")
scalar_series=pd.Series(4,index=[0,1,2,3,4,5,6,7,8,9])
print(scalar_series)
print("============================================================================")
print("Accessing data from series with Position:")
series_position=pd.Series([0,1,2,3,4,5,6,7,8,9])
print(series_position[1])
print("============================================================================")
print("Series object attributes")
Series=series_position.copy()
print("Series\n",Series)
print("=============================================================================")
print("Series.index:\n",Series.index)
"""
output:
 RangeIndex(start=0, stop=10, step=1)
"""
print("==============================================================================")
print("Series.shape:\n",Series.shape)
"""
output:
(10,)
"""
print("===============================================================================")
print("Series.dtype:\n",Series.dtype)
"""
output:
"""
print("===============================================================================")
print("Series.size:\n",Series.size)
print("or")
print("len(Series)",len(Series))
"""
output:
Series.size:
 10
this will return the size of the data
"""
print("===============================================================================")
print("Series.empty:\n",Series.empty)
"""
output:
Series.empty:
 False
this will return 'True' id the series object isd empty.otherwise returns false
"""
print("===============================================================================")
print("Series.hasnans:\n",Series.hasnans)
"""
output:
Series.hasnans:
 False
this will return 'True' if there is any NaN valuesw.otherwise return False
"""
print("===============================================================================")
print("Series.nbytes:\n",Series.nbytes)
"""
output:
Series.nbytes:
 80
this returms the number of bites in the data
"""
print("===============================================================================")
print("Series.ndim:\n",Series.ndim)
"""
output:
Series.ndim:
 1
this returnd the dimensions of the data
"""
print("===============================================================================")
#print("Series.itemsize:\n",Series.itemsize)
"""
output:
"""
print("===============================================================================")
print("-------------------->>attributes of Series:")
print("-->important attributes")
print("===============================================================================")
print("data:")

print("===============================================================================")
print("index:")
print("===============================================================================")
print("name:")
print("===============================================================================")
print("dtype:")
print("===============================================================================")
print("copy:")
print("===============================================================================")
print("fastpath:")
print("===============================================================================")
print("-->>remaining attributes")
print("===============================================================================")
print("T:Transpose index and coloumns")
print("===============================================================================")
print("at:")
print("===============================================================================")
print("axes:")
print("===============================================================================")print("===============================================================================")
print("blocks:")
print("===============================================================================")print("===============================================================================")


print("===============================================================================")


print("===============================================================================")


print("===============================================================================")


print("===============================================================================")

print("===============================================================================")


print("===============================================================================")


print("===============================================================================")



print("===============================================================================")



print("===============================================================================")