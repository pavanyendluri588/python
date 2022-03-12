# importing pandas
import pandas as pd

# creating orginal_dataframe
orginal_dataframe=pd.DataFrame({'Name':['Shobhit','Vaibhav',
								'Vimal','Sourabh'],
						
						'Class':[11,12,10,9],
						'Age':[18,20,21,17]})

# Checking created orginal_dataframe
# copied orginal_dataframe
print("orginal_dataframe:\n",orginal_dataframe)
print("==============================================================================")
print("by default inplace:False")
# without using inplace renaming the column
"""
new_data = orginal_dataframe.rename(columns = {'Name':'FirstName'})

# Copied orginal_dataframe
print("new_data is copyed from orginal_dataframe but first coloum name was changed to Firstname",new_data)

# checking whether orginal_dataframe is modified or not
# Original orginal_dataframe
print("===============================================================================")
print("orginal_dataframe after replaceing first row with Firstnamein the copy :\n",orginal_dataframe)
"""
# putting inplace=False
new_data_2 = orginal_dataframe.rename(columns = {'Name':'FirstName'},inplace = False)

# Copied orginal_dataframe
print("using inplace=False",new_data_2)

print("checking whether orginal_dataframe is modified or not")
print("orginal_dataframe:\n",orginal_dataframe)
print("==============================================================================")
# Putting Inplace=True
#you can keep '1' in place of 'True'
#you can keep '0' in place of 'False'
new_data_3=orginal_dataframe.rename(columns = {'Name':'FirstName'},inplace =1)
#here the operation is done in the orginal_dataframe. so the new_data_3 will return  none 

# Original orginal_dataframe
print("using inplace=True:\n",new_data_3)
print("checking whether orginal_dataframe is modified or not")
print("orginal_dataframe:\n",orginal_dataframe)
"""
output:
orginal_dataframe:
       Name  Class  Age
0  Shobhit     11   18
1  Vaibhav     12   20
2    Vimal     10   21
3  Sourabh      9   17
==============================================================================
by default inplace:False
using inplace=False   FirstName  Class  Age
0   Shobhit     11   18
1   Vaibhav     12   20
2     Vimal     10   21
3   Sourabh      9   17
checking whether orginal_dataframe is modified or not
orginal_dataframe:
       Name  Class  Age
0  Shobhit     11   18
1  Vaibhav     12   20
2    Vimal     10   21
3  Sourabh      9   17
==============================================================================
using inplace=True
: None
checking whether orginal_dataframe is modified or not
orginal_dataframe:
   FirstName  Class  Age
0   Shobhit     11   18
1   Vaibhav     12   20
2     Vimal     10   21
3   Sourabh      9   17
"""
print("======================================================================================")
print("======================================================================================")
print("conclusion about inplace:")
print("by default inplase is False means the operations will not occore in the orginal object")
print("inplace=True means the operation will done on the orginal object")
print("see the above example to understand about inplace")
print("======================================================================================")
print("======================================================================================")