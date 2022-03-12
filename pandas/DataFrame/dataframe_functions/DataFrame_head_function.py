"""
reference:


"""
import pandas as pd
import numpy as np
print("======================================================================================")
print("""head function:The head() returns the first n rows for the object based on position. If your object has the right type of data in it, it is useful for quick testing. This method is used for returning top n (by default value 5) rows of a data frame or series.""")

print("======================================================================================")
print("parameters of head:")
print("n:It refers to an integer value that returns the 'n' number of rows.")
df=pd.DataFrame({"table_2":[2,4,6,8,10,12,14,16,18,20],"table_3":[3,6,9,12,15,18,21,24,27,30],"table_4":[4,8,12,16,20,24,28,32,36,40],"table_5":[5,10,15,20,25,30,35,40,45,50]},index=[1,2,3,4,5,6,7,8,9,10])
print("df:",df)
df_assign=df.assign(table_6=df['table_2']*df['table_3'],table_8=df['table_2']*df['table_4'],table_10=df['table_2']*df['table_5'],table_12=df['table_3']*df['table_4'],table_15=df['table_3']*df['table_5'],table_20=df['table_4']*df['table_5'])
print("using the head function n default value is 5:\n",df_assign.head())
print("======================================================")
print("changing n value to 9:\n",df_assign.head(9))
"""
output:
======================================================================================
head function:The head() returns the first n rows for the object based on position. If your object has the right type of data in it, it is useful for quick testing. This method is used for returning top n (by default value 5) rows of a data frame or series.
======================================================================================
parameters of head:
n:It refers to an integer value that returns the 'n' number of rows.
df:     table_2  table_3  table_4  table_5
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
using the head function n default value is 5:
    table_2  table_3  table_4  table_5  table_6  table_8  table_10  table_12  table_15  table_20
1        2        3        4        5        6        8        10        12        15        20
2        4        6        8       10       24       32        40        48        60        80
3        6        9       12       15       54       72        90       108       135       180
4        8       12       16       20       96      128       160       192       240       320
5       10       15       20       25      150      200       250       300       375       500
======================================================
changing n value to 9:
    table_2  table_3  table_4  table_5  table_6  table_8  table_10  table_12  table_15  table_20
1        2        3        4        5        6        8        10        12        15        20
2        4        6        8       10       24       32        40        48        60        80
3        6        9       12       15       54       72        90       108       135       180
4        8       12       16       20       96      128       160       192       240       320
5       10       15       20       25      150      200       250       300       375       500
6       12       18       24       30      216      288       360       432       540       720
7       14       21       28       35      294      392       490       588       735       980
8       16       24       32       40      384      512       640       768       960      1280
9       18       27       36       45      486      648       810       972      1215      1620
"""

































