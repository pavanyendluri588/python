import numpy as np

"""
zeros_like 
it is used to print the array with argument shape  and elements are replaced by ones
"""
array_1=np.array([[6,7,8,9,10],[2,3,4,5,6],[1,2,3,4,5]])
print("array_1:\n",array_1)
array_1_to_ones=np.ones_like(array_1)
print("array_1_to_ones:\n",array_1_to_ones)