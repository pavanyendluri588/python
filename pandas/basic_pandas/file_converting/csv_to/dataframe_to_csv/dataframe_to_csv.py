#importing pandas libary as pd
import pandas as pd

#createing a dictonary
dict={'name':['pavan','my_wife','my_childern','my_friends','my_enemies'],
     'age':[19,15,1,20,20],
     'gender':['male','female','male_or_female','male_or_female','male_or_female'],
     'phone number':[3423943298,101001292,472983472398,432788,4878274872]}

#createing a dataframe from dictonary
df=pd.DataFrame(dict)
print("dataframe without specifing index:\n",df)

#crateing dataframe with index
df1=pd.DataFrame(dict,index=['a','b','c','d','e'])
print("dataframe with specifing index:\n",df1)

#converting datafeame to csv
df1.to_csv("dataframe_to_csv_converted.csv")
csv_file = df1.to_csv()



