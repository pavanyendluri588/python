import pandas as pd
import numpy as np
print("series to_frame():")
print("The Pandas Series.to_frame() function is used to convert the series object to the DataFrame.")
s=pd.Series([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print("s:\n",s)
print("========================================================")
print("parameters of to_frame:")
print("1.name:name: Refers to the object. Its Default value is None. If it has one value, the passed name will be substituted for the series name.")
s_to_frame=s.to_frame()
s_to_frame_name=s.to_frame(name='num')
print("s_to_frame:\n",s_to_frame)
print("s_to_frame_name:\n",s_to_frame_name)