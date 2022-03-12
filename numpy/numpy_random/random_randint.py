from numpy import random
"""
syntax:
random.randint(low, high=None, size=None, dtype=int)
=======================================================
parameters:
low:the value should be greater or equal thean n
high:(int,None)the value should not greater than (n-1)
size:the size of the array
dtype:data type of  the array
"""
a=random.randint(5,size=(2,5))
print(a)

b=random.randint(3,size=(3,5),high=10)# here value greater than or equal to 3 and highest value is  less than 10
print(b)
c=random.randint(30,size=(3,5),high=50,dtype="int8")# here the low is 30 and high is (50-1)
print(c)