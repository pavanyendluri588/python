#this will gibe the dimensions od the array
import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8]])
print(a)
print(a.ndim)
print("=======================")
b=np.arange(24)
print(b)
print(b.ndim)
#reshaping
b.reshape(2,4,3)#this will not reshape array
b=b.reshape(2,4,3)#this will reshape the attay
print(b)
print(b.shape)
print(b.ndim)