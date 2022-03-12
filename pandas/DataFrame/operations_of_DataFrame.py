import pandas as pd
import numpy as np
"""
create a DataFrame:
We can create a DataFrame using following ways:
1.dict
2.Lists
3.Numpy ndarrrays
4.Series
"""
print("creatinga data frame by using following ways\n1.dict\n2.Lists\n3.Numpy ndarrays\n4.series")
print("==========================================================================================")
print("-->creating a dataframe using 1D list:")
lst=[11,22,33,44,55]
df_list=pd.DataFrame(lst,columns=['Names'])
print("df_list:\n",df_list)
"""
print("===========")
print("-->>creating a DataFrame using 2d list=Using zip() for zipping two lists=")
list1=[1,2,3,4,5]
df_zippedlist=pd.DataFrame(list(zip(lst,list1)),columns =['list','list2'])
print("zipped list:\n",df_zippedlist)
"""
print("===========")
print("-->>creatingh DataFrame using multidimensional list")
multidimensional_list=[[11,22,33,44,55],['one','two','three','four','five']]
df_multidimensional_list=pd.DataFrame(multidimensional_list,columns=['01','02','03','04','05'])
print("df_multidimensional_list:\n",df_multidimensional_list)

multidimensional_list1=[['One',1],['Two',2],['Three',3],['Four',4],['Five',5]]
df_multidimensional_list1=pd.DataFrame(multidimensional_list1,columns=['word','num'])
print("df_multidimensional_list1:\n",df_multidimensional_list1)
print("===========")
print("-->>creating the DataFrame using multidimensional_list,columns,dtype")
multidimensional_list2=[[1,'one',0.1111],[2,'two',0.2222],[3,'three',0.3333],[4,'four',0.4444]]
df_multidimensional_list_columns_dtype=pd.DataFrame(multidimensional_list2,columns=['int_to_float','word','float'],dtype=float)
print("df_multydimensional_list_columns_dtype:\n",df_multidimensional_list_columns_dtype)
print("orginalvalues:")
print(" int_to_float   word   float\n0           1    one  0.1111\n1           2    two  0.2222\n2           3  three  0.3333\n3           4  four   0.4444")
print("===================")
print("-->>Using lists in dictionary to create dataframe")
nme = ["aparna", "pankaj", "sudhir", "Geeku"]
deg = ["MBA", "BCA", "M.Tech", "MBA"]
scr = [90, 40, 80, 98]
# dictionary of lists 
dict = {'name': nme, 'degree': deg, 'score': scr} 
df_dictonary = pd.DataFrame(dict)
print("df_dictonary:\n",df_dictonary)
print("==========================================================================================")
print("-->>columns selection in DataFrame")
multidimensional_list3=[['One',1],['Two',2],['Three',3],['Four',4],['Five',5]]
df_multidimensional_list3=pd.DataFrame(multidimensional_list3,columns=['word','num'])
print("df_multidimensional_list3:\n",df_multidimensional_list3)
print("selecting column <num>:")
num_column=df_multidimensional_list3['num']
print(num_column)
"""
output:
selecting column <num>:
0    1
1    2
2    3
3    4
4    5
Name: num, dtype: int64
"""
print("================")
print("-->>column addition ")

print("===============")
print("-->>coloum deletion")
multidimensional_list4=[[1,'one',0.1111],[2,'two',0.2222],[3,'three',0.3333],[4,'four',0.4444]]
df_multidimensional_list_del=pd.DataFrame(multidimensional_list4,columns=['int','word','float'])
print("df_multydimensional_list_del:\n",df_multidimensional_list_del)
print("deleting the <int> column")
del df_multidimensional_list_del['int']
print(df_multidimensional_list_del)
print("deleting the <word> column")
del df_multidimensional_list_del['word']
print(df_multidimensional_list_del)
print("deleting the <float> column")
del df_multidimensional_list_del['float']
print(df_multidimensional_list_del)
"""
output:
df_multydimensional_list_del:
    int   word   float
0    1    one  0.1111
1    2    two  0.2222
2    3  three  0.3333
3    4   four  0.4444
deleting the <int> column
    word   float
0    one  0.1111
1    two  0.2222
2  three  0.3333
3   four  0.4444
deleting the <word> column
    float
0  0.1111
1  0.2222
2  0.3333
3  0.4444
deleting the <float> column
Empty DataFrame
Columns: []
Index: [0, 1, 2, 3]
==============
if the DataFrame is empty.then it will return:
Empty DataFrame
Columns: []
index:
 the delete or pop function to delete the columns from the DataFrame.

"""
print("===============================================================")
print("row selection using pandas")
#We can select any row by passing the row label to a loc function.
info = {'one' : pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e']),   
   'two' : pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f'])}  
  
df111 = pd.DataFrame(info)  
print("df111:",df111)
print (df111.loc['b'])  
print("===================================================================")
print("slice rows")