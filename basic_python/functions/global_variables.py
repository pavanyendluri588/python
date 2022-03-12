#outside function every variable is a global variable:
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
#OUTPUT:python is awesome

#if we declare the variable inside the function it is independent to the outside variable
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
#OUTPUT:
#Python is fantastic
#Python is awesome


#if you declare a variable with the global keyword it should be changed in entire program
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#OUTPUT:Python is fantastic
