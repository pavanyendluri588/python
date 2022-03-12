import pandas as pd
import numpy as np
import os
print("applyfunction:apply function allows user to pass a function and apply it every single column in the pandas series.")

"""
parameters of apply function:
1.fun
2.axis
3.braodcast
4.raw
5.reduce
6.result_type
7.args
8.**kwds
"""
data1={"flightname":["delhi airlines","andhra pradesh airlines","telangana airlines","tamil nadu airlines","panjab airlines","up airlines","lpu airlines"],"flight_No:":[423,23342,324,543,756,678,687],"passangers_capacity":[100,200,300,400,500,600,700],"filling_percentage":[79,68,57,45,34,23,78],"duration":["2h 4m","11h 55m","4h 56m","8h 45m","6h 9m","3h 5m","1h 7m",]}

df=pd.DataFrame(data1)
df1=pd.DataFrame([{"flightname":["delhi airlines","andhra pradesh airlines","telangana airlines","tamil nadu airlines","panjab airlines","up airlines","lpu airlines"],"flight_No:":[423,23342,324,543,756,678,687],"passangers_capacity":[100,200,300,400,500,600,700],"filling_percentage":[79,68,57,45,34,23,78],"duration":["2h4m","11h 55m","4h 56m","8h 45m","6h 9m","3h 5m","1h 7m",]}])
data2=pd.read_csv('D:\python\pandas\DataFrame\dataframe_functions\apply_testing_data.csv')
print("data2:\n",data2)
print(df.head())
b=data1.duration[0]
print("b:\n",b)