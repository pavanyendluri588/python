import numpy as np
a_d_1=np.array([1,2,3,4,5,6,7,8,9,10])
a_d_2=np.array([[1,2,3,4,5,6,7,8],[11,22,33,44,55,66,77,88]])
print("1-D array:\n",a_d_1)
print("2-D array:\n",a_d_2)
expression=(a_d_1)>=5
d1_extract=np.extract(expression,a_d_1)
print("d1_extract:\n",d1_extract)
expression1=(a_d_2)>=5
d1_extract=np.extract(expression1,a_d_2)
print("d1_extract:\n",d1_extract)