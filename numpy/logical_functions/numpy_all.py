import  numpy as np
"""
syntax:
numpy.all(a, axis=None, out=None, keepdims=<no value>, *, where=<no value>)

parameters:
object
axis
keepdims
where
"""
x=[1,2,3,4,5,6,7,8]
a=np.all(x,axis=0)
print(a)
x1=[[4,3,2,1],[1,2,3,4]]
print(x1)
a1=np.all(x1)
print(a1)
