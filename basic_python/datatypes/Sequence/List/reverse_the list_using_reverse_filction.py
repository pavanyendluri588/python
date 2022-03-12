"""
reverse() parameter
The reverse() method doesn't take any arguments.

Return Value from reverse()
The reverse() method doesn't return any value. It updates the existing list.
"""
lit=[1,2,3,4,4,5,"pavan","ram","chandar"]
print("lit:",lit)
lit.reverse() #this function will reverse the List
print("after using the reverse() to lit:",lit)
print("=============================================================================")
#Reverse a List Using Slicing Operator
# Operating System List
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)

# Reversing a list
# Syntax: reversed_list = systems[start:stop:step]
reversed_list = systems[::-1]


# updated list
print('Updated List:', reversed_list)
#Accessing Elements in Reversed Order
# Operating System List
systems = ['Windows', 'macOS', 'Linux']

# Printing Elements in Reversed Order
for o in reversed(systems):
    print(o)
#output:
"""
Linux
macOS
Windows
"""
