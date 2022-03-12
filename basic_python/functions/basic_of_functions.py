#function syntax
def function_name():
     x=5 
     y=10
     print("the value of x:",x,"the value of y:",y)
     sum=x+y
     return  sum
function_name()
z=function_name()
print(z)

#printing the sum of two numbers using the return statement:
def function():
      global x #declaration of global variable  insibe the  function
      x=154
      y=100
      print("the value of x:",x,"the value of y :",y)
      return 
function()
print("the function without return statement expersion will print:",function())

def function1(x,y):
      print("the value of x:",x,"the value of y:",y)
      c=x+y
      print(type(x))
      print(type(y))
      return c
a=float(input("enter number1:"))
b=float(input("enter number2:"))
print("the sum of the two numbers:",function1(a,b))
