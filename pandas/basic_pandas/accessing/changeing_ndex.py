import pandas as pd
import numpy as np
#createing the dictonary
dict={'name':["pavan1","pavan2","pavan3","pavan4","pavan5"],
     'age':[19,20,21,22,23],
     'phone_number':[19110564858,29110564858,39110564858,49110564858,59110564858]
}
print("dict:\n",dict)
print("dtype(dict)",type(dict))
#checking what are the columns are there in dataframe
print("df.columns",df.columns)
#print the index if teh dataframe
print("df.indexs")
#createing the dataframe using dictonary
df=pd.DataFrame(dict,index=['a','b','c','d','e'])
#printing the dataframe
print("df\n",df)
#checking the type of  columthe dataframe
print("type(df)\n",type(df))

#increaseing the index
df1=pd.DataFrame(df,index=['a','b','c','d','e','f','g','h','i'])
print("df1\n",df1)
#decreaseing  the index
df2=pd.DataFrame(df,index=['a','b','c'])
print("df2\n",df2)

#to check the datatypes of the dataframe
print("df\n",df)
print("df.dtype:\n",df.dtypes)

#while createing the DataFrame specify the datatype og the dataframe
df3=pd.DataFrame(df,columns=['phone_number','age'],dtype=np.int64)
print("df3:\n",df3)