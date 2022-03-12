import pandas as pd
df=pd.DataFrame([['P','a','n','d','a','s','d','a','t','a','f','r','a','m','e'],['e','m','a','r','f','a','t','a','d','s','a','d','n','a','d'],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen']])
print(df)
df11=df.copy()
"""
output:
  0  1  2  3  4  5  6  7  8  9  10 11 12 13 14
0  P  a  n  d  a  s  d  a  t  a  f  r  a  m  e
1  P  a  n  d  a  s  d  a  t  a  f  r  a  m  e

"""
print("========================================================================")
print("DataFrame attributes:")
print("T\narry\nat\nattr\nsaxes\ndtype\ndtypes\nflag\nhasnameiat\niloc\nindex\nloc\name\nnbytes\nndim\nshape\nsize\nvalues")

print("-------------------->>working of DataFrame attributes:")
print("-->important attributes")
print("===============================================================================")
print("data:")

print("===============================================================================")
print("index:")

print("===============================================================================")
print("columns:The column labels of the DataFrame.")
print("===============================================================================")
print("dtype:Return the dtypes in the DataFrame.")
#print("dtype of df DataFrame:\n",df.dtype)
print("===============================================================================")
print("copy:")
df_copy_False=''
print("copy")
df_copy_True=''
print("===============================================================================")
print("empty:Indicator whether DataFrame is empty.")
print("===============================================================================")
print("ftypes:")
#df.ftypes

print("===============================================================================")
print("iloc:")

print("===============================================================================")
print("loc:")

print("===============================================================================")
print("size:")
print("size of DataFrame",df.size)
print("===============================================================================")
print("ndim:Return 1 if Series. Otherwise return 2 if DataFrame.")
print("ndim od df DtaFrame:\n",df11.ndim)
"""
output:
ndim od df DtaFrame:
 2
"""
print("===============================================================================")
print("style:")
print("style of df DataFrame:\n",df.style)
"""
output:
style of df DataFrame:
 <pandas.io.formats.style.Styler object at 0x0000029EE498BEB0>
"""
print("===============================================================================")
print("values:return the dataframe in the form of numpy representation")
print("values of df DataFrame:\n",df.values)
"""
output:
values of df DataFrame:
 [['P' 'a' 'n' 'd' 'a' 's' 'd' 'a' 't' 'a' 'f' 'r' 'a' 'm' 'e']
 ['e' 'm' 'a' 'r' 'f' 'a' 't' 'a' 'd' 's' 'a' 'd' 'n' 'a' 'd']
 [1 2 3 4 5 6 7 8 9 10 11 12 13 14 15]
 ['one' 'two' 'three' 'four' 'five' 'six' 'seven' 'eight' 'nine' 'ten'
  'eleven' 'twelve' 'thirteen' 'fourteen' 'fifteen']]
"""
print("===============================================================================")
print("-->>remaining attributes")
print("===============================================================================")
print("T:Transpose index and coloumns")
#transpose=df.T
#or 
transpose=df.transpose()
print("before transposeing:\n",df)
print("after transpose of df:\n",transpose)
print("===============================================================================")
print("at:Access a single value for a row/column label pair.")
#DataFrame_name.at[columnname,rowindex]
print("using at getting the value 2ndrow 3 column:",df.at[3,3])
print("using at getting the value 2ndrow 3 column:",df.at[2,5])
print("===============================================================================")
print("axes:")
print("the axes of df DataFrame:\n",df.axes)
"""
output:
the axes of df DataFrame:
 [RangeIndex(start=0, stop=4, step=1), RangeIndex(start=0, stop=15, step=1)]
first ramge index about columns
second range index about rows
"""
print("===============================================================================")
print("blocks:")

print("===============================================================================")
print("ix")
print("===============================================================================")
print("iat")
print("===============================================================================")


print("===============================================================================")


print("===============================================================================")


print("===============================================================================")


print("=======================================================================")
