import numpy as np
s="hello world i am pavan"
a=np.frombuffer(s,count=4)
print(a)
b=np.frombuffer(s,count=5,offset=2)
print(b)

"""
parameters:
buffer:Any object that exposes buffer interface
dtype:data type of the returned array (default it is float)
count:number of elements should read (default it is -1)
offset:the starting position to read from (default it is 0)
"""