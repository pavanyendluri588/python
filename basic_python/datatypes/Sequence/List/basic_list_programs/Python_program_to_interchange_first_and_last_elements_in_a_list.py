list1=[x for x in range(0,11)] #creationg the list 0 to 10 numbers
print("Before interchangeing the first and last digit in list1:",list1)
list1[0],list1[-1]=list1[-1],list1[0] #interchangeing the first and last digit og list1
print("After interchangeing the first and last digit in list1:",list1)
"""
output:
Before interchangeing the first and last digit in list1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
After interchangeing the first and last digit in list1: [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
"""
