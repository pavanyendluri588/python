"""
def demo(*args):
    print(args)
Call the function

demo("Humpty", "Dumpty") # call with two arguments
Output:

('Humpty', 'Dumpty')
Call the function again, this time with 6 arguments

demo("Humpty", "Dumpty", "Sat", "On", "A", "Wall") # call with two arguments
Thus, regardless of the number of arguments passed, *args is showing you the result. Doesn’t matter if you pass (“Humpty”, “Dumpty”) or (“Humpty”, “Dumpty”, “Sat”, “On”, “A”, “Wall”). , *args will handle that for you. Note: As mentioned, you can write anything and not just args. Let’s try *whatever.

def demo(*whatever):
    print(whatever)
Call the function

demo("Humpty", "Dumpty", "Sat", "On", "The", "Wall")
Output:

('Humpty', 'Dumpty', 'Sat', 'On', 'The', 'Wall')
And that’s perfectly fine!

Let’s write a function that sums up as many inputs as we want.

def sum(*args):
    c = 0
    for arg in args:
        c+=arg
    return c
Call the function

sum(1,2,3,4,5)
Output:

15
Call again. This time with more arguments.

sum(1,2,3,4,5,6,7,8,9,10)
Output:

55
Doesn’t matter if you sum 1 to 5 or 1 to 10, Python will calculate the result for you irrespective of the number of parameters. This is the beauty of *args.
"""
def function(*names): #*args is used to pass the arguments number is unknown
	print("the names:",names)
function("pavan","rama","ram","my wife","prudhvi","venkat")
def sumofnum(*numbers):
	print("passed numbers:",numbers)
	c=0
	for x in numbers:
		c+=x
	else:
		print("calculation is completed")

	return c
d=sumofnum(1,2,3,4,5,6)
print("the sum of the numbers is ",d)
print("====================================================")
#printing the LETTERS IN THE STRINGS
def seperating(*strings):
	print("passed strings:",strings)
	for x in strings:
		for y in x:
			print(y)
		print("")
	else:
		print("seperation is completed")
seperating("pavan","rama","ram","my wife","prudhvi","venkat")
