import numpy as np
"""
split is used for 
Split an array into multiple sub-arrays as views into ary.

parameters:
array:
indices_or_selections:int or id array
                     case1:(int)it will devide the array into n(int) equal parts
                     clse2:theis  will divide array like down[2,3]
                           arr[:2]
                           arr[2,3]
                           arr[3:]
                           if the index is iiut of range means it will create empty array
axis:
"""
arr1=np.array([1,2,3,4,5,6,7,8])
"""
arr1_split=np.split(arr1)
TypeError: _split_dispatcher() missing 1 required positional argument: 'indices_or_sections'
"""
arr1_split=np.split(arr1,4)#this will devide array into 4 equal parts
print(arr1)
print(arr1_split)
print(np.split(arr1,4))
print(arr1)
print("==========================================================================")
#level-2
x=np.arange(50)

"""
split1=np.split(x,4)
raise ValueError(
ValueError: array split does not result in an equal division
"""
split1=np.split(x,5)
print(split1,"\n\n")
split2=np.split(x,[1,2,3,4,5,6])
print(split2,"\n\n")
split3=np.split(x,[2,3])
print(split3,"\n\n")
print(x[2:3])
print("=================================================================")
#level-3
x=np.array([[1,2,3,4,5,6],[6,7,8,9,10,11]])
split1=np.split(x,2)
print(split1,"\n\n")
x=np.array([[1,2,3,4,5,6],[6,7,8,9,10,11]])
#split1=np.split(x,3)
print(split1,"\n\n")
x=np.array([[1,2,3,4,5,6],[6,7,8,9,10,11]])
split1=np.split(x,1)
print(split1,"\n\n")
split2=np.split(x,[1,2,3,4,5,6])
print(split2,"\n\n")
split3=np.split(x,[2,3])
print(split3,"\n\n")
print(x[2:3])
