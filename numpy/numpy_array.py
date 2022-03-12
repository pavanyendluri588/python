import numpy as np
a=[1,2,3,4,5,6]
#single dimensional
b=np.array(a)
print(b)
print(type(b))
#multidimensional
c=np.array([[1,2,3,4],[2,3,4,5]])
print(c)
print(type(c))
#dtype  this will specify the datatype
d=np.array([5+6j,4j+8],dtype=complex)
print(d)
print(type(d))
#order
order1=np.array([1,2,3,4,5],order="C")
print(order1)
print(type(order1))
for x in range(0,len(order1)):
	#these all hase same memory location
	print(id(order1[x]),"x=",x)