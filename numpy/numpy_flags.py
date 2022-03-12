import numpy as np 
a=np.array([[1,2,3,4,5,6],[1,3,5,7,9,11]])
print("a",a)
print("type(a):",type(a))
print("a.np.flags:\n",a.flags)
b=a
print(b)
print("type(b):",type(b))
print("b.flags:\n",b.flags)
