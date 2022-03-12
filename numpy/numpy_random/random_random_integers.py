from numpy import random
"""
syntax:
random.random_integers(low,high=None,size)
parameters:
low:the array elenents lowest elements is n
high:the array elements less than n
size:size of the array
"""
print("=====================================")
a=random.random_integers(5,size=(5,10,10))
print(a)
print(a.shape)
print("=====================================")
b=random.random_integers(5,high=10,size=(5,10,10))
print(b)
print(b.shape)


