for x in range(7):
	print("x:",x)
#iterating string
x="python"
print("type of x :",type(x))
for j in x:
	print(j)
#iterating the list
x=[1,2,3,4,5,6,7,8,9]
print("type of x :",type(x))
a=0
for z in x:
	print("x[a] :",x[a])
	a=a+1
	print("z:",z)
#iterating the tuple
x={1,2,3,4,5,6,7,8,9,10}
print("type of x :",type(x))
for z in x:
	print("z:",z)
#iterating the tuple
x=(1,2,3,4,5,6,7,8,9,10)
print("type of x :",type(x))
for z in x:
	print("z:",z)
#iterating the tuple
x={1:"pavan",2:"my_wife",3:"rama",4:"prudhvi",5:"venkat"}
print("type of x :",type(x))
for y,z in x.items():
	print("z:",y,z)