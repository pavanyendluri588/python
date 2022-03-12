str="this is pavan ram chandar"
print("checking the length of str string",len(str))
print()
print("checking the str is which type of data type:",type(str))
print("checking is pavan is not present in string str",'pavan' not in str)
print("checking the string str containg a pavan or not:",'pavan' in str)
print("checking the string str ")


#multi line string 
multi_line_string_double_quotes="""this is pavan ram chanmdar
from lovely professional university
my reg.no:12003141 
this is pythgon multiline string """
#or single quotes
multi_line_string_single_quotes='''this is pavan ram chanmdar
from lovely professional university
my reg.no:12003141 
this is pythgon multiline string'''
#checking what is the difference between multi_line_string_double_quotes and multi_line_string_single_quotes
if (multi_line_string_double_quotes==multi_line_string_single_quotes):
    print("multi_line_string_single_quotes is equal to multi_line_string_double_quotes")
else:
    print("multi_line_string_single_quotes is not  equal to multi_line_string_double_quotes")


#strings are arrys
sa="pavan"
print("sa[0]=",sa[0])
#changing sa[0] to r
#sa[0]='r'
#print("after changing :sa=",sa)


#lppos in strings
for x in "pavan":
    print(x)

#the slice operator [] in string
string1="pavan ram chandar"
print("string1:",string1)
print("length of string1:",len(string1))
x=len(string1)
for b in range(0,x):
    print("""string1[" """,b,""" "]=""",string1[b])
print("string1[:]=",string1[:])
print("string1[0:]=",string1[0:])
print("string1[:0]=",string1[:0])
print("string1[5:10]=",string1[5:10])
print("string1[5:]=",string1[5:])
print("string1[:5]=",string1[:5])
#for b in range(x,0,-1):
#negetive indexing
#reversing string
for y in range(-1,-len(string1),-1):
     print("""string1[" """,y,""" "]=""",string1[y])
       
print("REVERSING THE STRING:\nstring1[::-1]:",string1[::-1])
