import numpy as np
print("level-1")
a=np.arange(10).reshape(2,5)+10
print("a:\n",a)
search_argmax_0=np.argmax(a,axis=0)
print("search_argmax_0:\n",search_argmax_0)
print("\n==============")
search_argmax_1=np.argmax(a,axis=1)
print("search_argmax_1:\n",search_argmax_1)
print("=================================================\n")
print("level-2")
a1=np.array([[1,2,3,4,5,np.nan,6,7,8,999],[2,np.nan,4,5,6,np.nan,8,9,10,np.nan]])
print("a1:\n",a1)
search_argmax_0_nan=np.argmax(a1,axis=0)
print("search_argmax_0_nan:\n",search_argmax_0_nan)
print("\n==============")
search_argmax_1_nan=np.argmax(a1,axis=1)
print("search_argmax_1_nan:\n",search_argmax_1_nan)
print("=================================================\n")
print(a1[5,1])