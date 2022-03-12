"""
reference:
https://www.javatpoint.com/pandas-dataframe-assign
"""
import pandas as pd
import numpy as np
print("===================================================================================")
"""
assign:Dataframe.assign() method assign new columns to a DataFrame
"""
print("===================================================================================")
df=pd.DataFrame({"table_2":[2,4,6,8,10,12,14,16,18,20],"table_3":[3,6,9,12,15,18,21,24,27,30],"table_4":[4,8,12,16,20,24,28,32,36,40],"table_5":[5,10,15,20,25,30,35,40,45,50]},index=[1,2,3,4,5,6,7,8,9,10])
#,columns=['table_2','table_3','table_4','table_5']
print("df:\n",df)
print("===================================================================================")
df_assign=df.assign(name=['one','two','three','four','five','six','seven','eight','nine','ten'],x=5)
print("df_assign=df.assign(name=['one','two','three','four','five','six','seven','eight','nine','ten'],x=5):\n",df_assign)
print("after df_assign the orginal df DataFrame:\n",df)
print("===================================================================================")
print("mathametical operation in assin function:")
df_assign_numeric=df.assign(table_10=df['table_2']*df['table_5'])
print("df_assign_numeric=df.assign(table_10=df['table_2']*df['table_5']):\n",df_assign_numeric)

"""
output:
df:
     table_2  table_3  table_4  table_5
1         2        3        4        5
2         4        6        8       10
3         6        9       12       15
4         8       12       16       20
5        10       15       20       25
6        12       18       24       30
7        14       21       28       35
8        16       24       32       40
9        18       27       36       45
10       20       30       40       50

df_assign=df.assign(name=['one','two','three','four','five','six','seven','eight','nine','ten'],x=5):
     table_2  table_3  table_4  table_5   name  x
1         2        3        4        5    one  5
2         4        6        8       10    two  5
3         6        9       12       15  three  5
4         8       12       16       20   four  5
5        10       15       20       25   five  5
6        12       18       24       30    six  5
7        14       21       28       35  seven  5
8        16       24       32       40  eight  5
9        18       27       36       45   nine  5
10       20       30       40       50    ten  5
after df_assign the orginal df DataFrame:
     table_2  table_3  table_4  table_5
1         2        3        4        5
2         4        6        8       10
3         6        9       12       15
4         8       12       16       20
5        10       15       20       25
6        12       18       24       30
7        14       21       28       35
8        16       24       32       40
9        18       27       36       45
10       20       30       40       50
mathametical operation in assin function:
df_assign_numeric=df.assign(table_10=df['table_2']*df['table_5']):
     table_2  table_3  table_4  table_5  table_10
1         2        3        4        5        10
2         4        6        8       10        40
3         6        9       12       15        90
4         8       12       16       20       160
5        10       15       20       25       250
6        12       18       24       30       360
7        14       21       28       35       490
8        16       24       32       40       640
9        18       27       36       45       810
10       20       30       40       50      1000
"""





































