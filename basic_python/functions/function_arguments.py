"""
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")
ERROR:
Traceback (most recent call last):
  File "demo_function_args_error.py", line 4, in <module>
    my_function("Emil")
TypeError: my_function() missing 1 required positional argument: 'lname'
"""
#if we don't know no of arguments:
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
#OUTPUT:The youngest child is Linus


#keyword arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child1)
  print("The youngest child is " + child2)
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#setting the default parameter value:
def my_function(child3, child2, child1):
  print("The youngest child is " + child1)
  print("The youngest child is " + child2)
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
#OUTPUT:
#I am from Sweden
#I am from India
#I am from Norway
#I am from Brazil


#passing the list to function:
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
OUTPUT:
#apple
#banana
#cherry