"""
reference:
https://www.youtube.com/watch?v=RCLtgM2LLhs
https://www.javatpoint.com/pandas-dataframe-aggregate
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.aggregate.html
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.agg.html
"""
import pandas as pd
import numpy as np
print("=======================================================================")
print("aggregate means మొత్తం")
print("The main task of DataFrame.aggregate() function is to apply some aggregation to one or more column. Most frequently used aggregations are:\n")

print("sum: It is used to return the sum of the values for the requested axis.")

print("min: It is used to return the minimum of the values for the requested axis.")

print("max: It is used to return the maximum values for the requested axis.")
print("So, I was going through agg() and aggregate() in pandas. And found both to give similar output.Here is the code which gives similar output for both the functions. So, just wanted to understand wat is the difference between both of them.")

print("=======================================================================")
print("parameters of aggregate:")
print("1.fun:")
print("2.axis:")
print("3.*args:")
print("4.**kwargs:")
print("=======================================================================")
df= pd.DataFrame([[25,15,12,19],[47, 24, 17, 29],[12,13,14,15],[23,24,25,26]],columns=['x','y','z','a'])  
print("df:\n",df)
print("df.agg(['sum','max','min']):\n",df.agg(['sum','max','min','std']))
print("""df.agg("x":['sum','max'],'y':['min','std']}),axis=0""",df.agg({'x':['sum','max'],'y':['min','std']},axis=0))
print("""df.agg(['sum','max','min','std'],axis=1)):\n""",df.agg(['sum','max','min','std'],axis=1))
#axis=0 or "index"  : It is an apply function for each column.
#axis=1 or "columns"  : It is an apply function for each row.
print("=======================================================================================")
print("using the function in aggregate()")
	