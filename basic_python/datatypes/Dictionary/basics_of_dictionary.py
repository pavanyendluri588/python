dict={}  #empty dictionary
print("type(dict)",type(dict))
dict1={"Name":"pavan"} #Name is key  :pavan is value
print("dict1:",dict1)

#adding values to dict===================================================================
print("before updating dict:",dict)
dict["name"],dict["age"],dict["collage"],dict["list"]="pavan",19,"LPU",[1,2,3,4,5,6,7,8,9]
print("after updating the dict:",dict)
print("""type(dict["list"]):""",type(dict["list"]))  #key muct be single value and it should be unique in dict ,value must be like list,string,tuple,int,etc
#updating the existing values in dict====================================================
print("before updateing the dict:",dict)
dict["age"]=20
print("after updateing the dict:",dict)
#deleting the keyword in the list========================================================
del dict["name"]
print("dict:",dict)
#deleting the dictionary=================
del dict
print("dict:",dict)
"""
print("dict:",dicts)
NameError: name 'dicts' is not defined
"""
#for deleting the elements the dict
#pop()
#popitem()
#clear()
#iterating the dictinary
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}
Employee1= {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}
for x in Employee:
    print(x,":",Employee[x]) #it will print the keywords in dict
for x in Employee.values():
    print(x)
for x in Employee.items():
    print(x)
for x,y in Employee.items():
    print(x,y)
#converting the dict to string
s=str(Employee)
print(s,type(s))

