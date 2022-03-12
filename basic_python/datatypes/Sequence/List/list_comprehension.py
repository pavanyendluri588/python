#iterating a string through for loop and adding the letters to a list
list_itteration=[] #empty list
for x in "human":
    list_itteration.append(x)
print("list_itteration:",list_itteration    )
"""
output:
list_itteration: ['h', 'u', 'm', 'a', 'n']
"""
#creating 0,30 numbers in a list_itteration1
list_itteration1=[x for x in  range(0,31)]
print("list_itteration1:",list_itteration1)
"""
output:
list_itteration: ['h', 'u', 'm', 'a', 'n']
list_itteration1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
"""

#if with list comprehension
list_if_with_list_comprehension=[x for x in range(1,100) if x%2==0]  #taking even numbers to lsit
print("list_if_with_list_comprehension:",list_if_with_list_comprehension)
"""
output:
list_if_with_list_comprehension: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
"""

#nested if with list comprehension
list_nested_if_with_list_comprehension=[x for x in range(0,100) if x%2==0 if x%5==0]  #takinf  list 2 and five tabels into list
print("list_nested_if_with_list_comprehension:",list_nested_if_with_list_comprehension)
"""
output:
list_nested_if_with_list_comprehension: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
"""
