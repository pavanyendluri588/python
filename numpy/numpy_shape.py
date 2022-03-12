import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8]])
print(a)
print(type(a))
print(np.shape(a))
#reshaping the array a
a.shape=(4,2)
b=a.reshape(4,2)
print(a)
print("========================")
print(b)