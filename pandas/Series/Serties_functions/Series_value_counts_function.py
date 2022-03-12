import pandas as pd  
import numpy as np  
index_= pd.Index([2, 1, 1, np.nan, 3])
s=pd.Series([3,4,5,6,7])
s.index(index_)
print("s:\n",s)  
index_.value_counts()
print("index_:\n",index_) 