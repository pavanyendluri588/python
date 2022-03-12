import numpy as np
"""
syntax:
numpy.random.choice(a, size=None, replace=True, p=None)
parameters:
1) a – 1-D array of numpy having random samples.

2) size – Output shape of random samples of numpy array.

3) replace – Whether the sample is with or without replacement.

4) p – The probability attach with every samples in a. 

Output : Return the numpy array of random samples.
"""

a=np.random.choice([1,2,3,4,5],size=(2,5))
print(a)
b=np.random.choice(10,size=(5,2),replace=True)#replace True means it will allow the replacement
print(b)
c=np.random.choice(10,size=(5,2),replace=False)#replace False means it will not allow the replacement
print(c)