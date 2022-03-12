"""
he else keyword in a while loop specifies a block of code to be executed when the loop is finished:

Example
Print all numbers from 0 to 5, and print a message when the loop has ended:
x=0
while x<5:  #while loop is executed until this loop is false
	print(x)
	x=x+1
else:
	print("while loop is finished")
"""
x=0
#y=1
while x<10:
	print(x)
	x=x+1
	"""
	print(y)
	y=y+1
	"""
else:
	print("while loop is finished")