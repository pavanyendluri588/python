# create a list
prime_numbers = [2, 3, 5, 7, 9, 11]
print('Before removing List: ', prime_numbers)
# remove 9 from the list
prime_numbers.remove(9)


# Updated prime_numbers List
print('Updated List: ', prime_numbers)

# Output: Updated List:  [2, 3, 5, 7, 11]
"""
remove() Parameters
The remove() method takes a single element as an argument and removes it from the list.
If the element doesn't exist, it throws ValueError: list.remove(x): x not in list exception.
"""
# animals list
animals = ['cat', 'dog', 'rabbit', 'guinea pig']

# 'rabbit' is removed
animals.remove('rabbit')

# Updated animals List
print('Updated animals list: ', animals)

#If a list contains duplicate elements, the remove() method only removes the first matching element.
# animals list
animals = ['cat', 'dog', 'dog', 'guinea pig', 'dog']

# 'dog' is removed
animals.remove('dog')


# Updated animals list
print('Updated animals list: ', animals)
