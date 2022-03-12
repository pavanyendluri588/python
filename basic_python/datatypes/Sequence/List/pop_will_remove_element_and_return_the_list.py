"""
The pop() method removes the item at the given index from the list and returns the removed item.

pop() parameters
The pop() method takes a single argument (index).
The argument passed to the method is optional. If not passed, the default index -1 is passed as an argument (index of the last item).
If the index passed to the method is not in range, it throws IndexError: pop index out of range exception

"""
lit=[1,2,3,4,'pavan','ram','chandar']
print("before useing the pop in lit:",lit)
removed_list=lit.pop(2)
print("removed element fron the list:",removed_list)
print("after removing lit:",lit)
print("=======================================================================")
#pop() without an index, and for negative indices
# programming languages list
languages = ['Python', 'Java', 'C++', 'Ruby', 'C']
print("orginal list of languages:",languages)
# remove and return the last item
print('When index is not passed:')
print('Return Value:', languages.pop())#this will return the last element from the list

print('Updated List:', languages)

# remove and return the last item
print('\nWhen -1 is passed:')
print('Return Value:', languages.pop(-1))

print('Updated List:', languages)

# remove and return the third last item
print('\nWhen -3 is passed:')
print('Return Value:', languages.pop(-3))

print('Updated List:', languages)
