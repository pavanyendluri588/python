import numpy as np


"""
hsplit
splitting array into multiple sub arrays  horizontally

parameters:
arr
indices_or_sections

for above two paraneters refer file
D:\INT_213_Python\numpy\numpy_split.py
"""

arr1=np.array([1,2,3,4,5,6,7,8])
"""
arr1_split=np.split(arr1)
TypeError: _split_dispatcher() missing 1 required positional argument: 'indices_or_sections'
"""
arr1_hsplit=np.hsplit(arr1,4)#this will devide array into 4 equal parts
print(arr1)
print(arr1_hsplit)
print(np.split(arr1,4))
print(arr1)
print("==========================================================================")
print("level-2")
x=np.arange(50)
print("x:\n",x)

"""
split1=np.split(x,4)
raise ValueError(
ValueError: array split does not result in an equal division
"""
split1=np.hsplit(x,5)
print(split1,"\n\n")
split2=np.hsplit(x,[1,2,3,4,5,6])
print(split2,"\n\n")
split3=np.hsplit(x,[2,3])
print(split3,"\n\n")
print(x[2:3])
print("=================================================================")
#level-3
x=np.array([[1,2,3,4,5,6],[6,7,8,9,10,11]])
print("x:\n",x)
print("==================")
split1=np.hsplit(x,2)
print(split1)
print("======================================================================\n\n\n")
x=np.array([[1,2,3,4,5,6],[6,7,8,9,10,11]])
print("x:\n",x)
print("==================")
#split1=np.split(x,3)
print(split1)
print("======================================================================\n\n\n")
x=np.array([[1,2,3,4,5,6],[6,7,8,9,10,11]])
print("x:\n",x)
print("==================")
split1=np.hsplit(x,1)
print(split1)
print("======================================================================\n\n\n")
split2=np.hsplit(x,[1,2,3,4,5,6])
print("x:\n",x)
print("==================")
print(split2)
print("======================================================================\n\n\n")
split3=np.hsplit(x,[2,3])
print("x:\n",x)
print("==================")
print(split3)
print(x[0,1:3])
"""
0 dimension number
1st index upto 3rd index
"""
print(x[1,2:3])
"""
print(x[2,2:3])
error:
print(x[2,2:3])
IndexError: index 2 is out of bounds for axis 0 with size 2
"""

