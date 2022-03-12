import pandas as pd
import numpy as np
from openpyxl.workbook import Workbook
"""
dataframe append function
append() used for adding the rows of other DataFrame to the end of the given dataframe,it will return a new dataframe object.
The new columns and the new cells are inserted into the original DataFrame that are populated with NaN value. 
It returns the appended DataFrame as an output.
SYNTAX:
given_DataFrame_name.append(other, ignore_index=False, verify_integrity=False, sort=None)

parameters of appeend:
1.other
2.ignore_index
3.verify_integrity
4.sort
"""
df1=pd.DataFrame({"x":[1,2,3,4],"y":['a','b','c','d'],"z":['1a','2b','3c','4d']})
print("df1:\n",df1)
df2=pd.DataFrame({"x":[5,6,7,8],"y"
:['e','f','g','h'],"z":['5e','6f','7g','8g']})
print("df2:\n",df2)
df3=pd.DataFrame({"x1":[15,26,37,48],"y1":['ae','bf','cg','dh'],"z1":['1a5e','2b6f','3c7g','4d8g']})
print("df3:\n",df3)
print("==============================================================================================")
print("columns index are same")
df4=df1.append(df2)
print("df4 is the output of df2 is append to df1(df2 is added to df1):\n",df4)
print("=========================")
print("verify_integrity:If it is true, it raises ValueError on creating an index with duplicates.")
#print("ValueError: Indexes have overlapping values: Int64Index([0, 1, 2, 3], dtype='int64')")
print("=========================")
print("index:")
df5=df1.append(df2,ignore_index=True)
print("df5is the output of df2 is append to df1(df2 is added to df1) and ignore_index=True:\n",df5)
print("=========================")
print("sort:")
df11=pd.DataFrame({"11":[11,22,33,44],"33":[9,8,7,6],"22":['a','b','c','d']})
df22=pd.DataFrame({"11":[55,66,77,88],"33":[5,4,3,2],"22":['h','g','f','e']})
df6=df11.append(df22,sort=True,ignore_index=True)
exel_file=pd.ExcelWriter('output.xlsx')
df6.to_excel(exel_file)
exel_file.save()
print("df6 is the output of df22 is append to df11(df22 is added to df11) and ignore_index=True and sort=True:\n",df6)
print("=================================================================================================")
print("=================================================================================================")
print("=================================================================================================")
print("columns index is different:")
df41=df1.append(df3)
print("df41 is the output of df3 is append to df1(df3 is added to df1):\n",df41)
"""
output:
df41 is the output of df3 is append to df1(df3 is added to df1):
      x    y    z    x1   y1    z1
0  1.0    a   1a   NaN  NaN   NaN
1  2.0    b   2b   NaN  NaN   NaN
2  3.0    c   3c   NaN  NaN   NaN
3  4.0    d   4d   NaN  NaN   NaN
0  NaN  NaN  NaN  15.0   ae  1a5e
1  NaN  NaN  NaN  26.0   bf  2b6f
2  NaN  NaN  NaN  37.0   cg  3c7g
3  NaN  NaN  NaN  48.0   dh  4d8g
"""
df51=df1.append(df3,ignore_index=True)
print("df51 is the output of df3 is append to df1(df3 is added to df1) and ignore_index=True:\n",df51)

"""
output:
     x    y    z    x1   y1    z1
0  1.0    a   1a   NaN  NaN   NaN
1  2.0    b   2b   NaN  NaN   NaN
2  3.0    c   3c   NaN  NaN   NaN
3  4.0    d   4d   NaN  NaN   NaN
4  NaN  NaN  NaN  15.0   ae  1a5e
5  NaN  NaN  NaN  26.0   bf  2b6f
6  NaN  NaN  NaN  37.0   cg  3c7g
7  NaN  NaN  NaN  48.0   dh  4d8g
"""
df111=pd.DataFrame({"11":[11,22,33,44],"33":[9,8,7,6],"22":['a','b','c','d']})
df222=pd.DataFrame({"1111111111111":[55,66,77,88],"713":[5,4,3,2],"012":['h','g','f','e']})
df61=df111.append(df222,sort=True,ignore_index=True)
print("df612 is the output of df222 is append to df111(df222 is added to df111) and ignore_index=True and sort=True:\n",df61)
"""
output:

note:
sorting is working based  on the first digit of column 
"""

