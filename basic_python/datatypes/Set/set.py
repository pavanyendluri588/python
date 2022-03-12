"""
set is collection  of unnorderd items
every element in a set must be unique
set is immutable
set remove the duplicates.

there is no index attached to the elements of the set, i.e., 
we cannot directly access any element of the set by the index. 
However, we can print them all together, or we can get the list of elements by looping through the set.

"""
#methods of set creation
#m-1
#using the curly brackets and comma seperated
set1={"apple","banana","orange"}
print("set1:",set1)
print("type(set1):",type(set1))
"""
print("set1[0]:",set1[0])
TypeError: 'set' object is not subscriptable
"""
#accessing the set using the loop
for x in set1:
     print(x)
#m-2
#
"""
set2=set("apple","banana","orange")
TypeError: set expected at most 1 argument, got 3
"""
set2=set(["banana","orange","apple","apple"])#set remove duplicates
print("set2:",set2)
print("type(set2):",type(set2))
#accessing the set using the loop
for x in set2:
     print(x)

# Creating a set which have immutable elements  
#set is immutable
set1 = {1,2,3, "JavaTpoint", 20.5, 14}  
print(type(set1)) 
"""
#Creating a set which have mutable element  
set2 = {1,2,3,["Javatpoint",4]}  
print(type(set2))
output:
set2 = {1,2,3,["Javatpoint",4]}
TypeError: unhashable type: 'list'
"""

#createing the empty set
set1=set()
print("set1:",set1)
print("type(set1)",type(set1))

#if ue create the using the curly brackets
set2={}
print("set2:",set2)
print("type(set2)",type(set2))

#adding the items into the set 
#Use add() function to add a single element. Whereas use update() function to add multiple elements to the set.
#add() is faster than update()
#we use the add() and update() to add the elements
set11={1,2,3,4,5}
print("set11:",set11)
#adding the immutable string in set11 using the add() method
set11.add("added single element using the add function")
print("set11:",set11)

set11.update("adding the single element using the update function")
print("set11:",set11)
set11.update({"added multiple element1 using the update function","added multiple element2 using the update function","added multiple element3 using the update function"})
print("set11:",set11)
print("=============================================================================")
print("remove() function")
#removing elements from the set
#we use the 3 methods to remove elements from set
#remove(),discard() and pop() methods to remove eements in set
"""
remove() method 
-->>remove methos remove the element if the element doesnot exist means it will return keyvalue error
remove function is faster than all the deleting functions because this will no check if element is exit in the set or not.
if the element doesnot exist means it will return Keyvalue Error.
"""
prathice_set={"apple","orange","pineapple","banana","grapes"}#set automaticallu remove the duplicate elements
print("before useing the remove function:\nprathice_set:",prathice_set)
prathice_set.remove("apple")#this will remove 
x=prathice_set.remove("banana")
print("prathice_set:",prathice_set)
print("x:",x)


print("====================")
print("discard() function")
"""
#discard() function
this function is samme like remove function but this will not return any error if theitem doesn't exist

"""
prathice_set1={"apple","mango","grapes","pineapple","orange"}#instde the brackets are   empty means it is dictonary
print("beforeusing the discard function\nprathice_set1:",prathice_set1)
prathice_set1.discard("greenapple")
print("""after using prathice_set1.discard("greenapple")--\n>>in set greenpple doesnot exist in set but also  discord does not rise error \nprathice_set1:""",prathice_set1)

print("====================")
print("pop() function")
"""
pop function
if we want to delete a random element from a set and also want to know what is deleted. 
Then use the pop() function.
This method removes a top element from the set but not the random element and returns the removed element. 
"""
prathice_set={"apple","orange","pineapple","banana","grapes"}#set automaticallu remove the duplicate elements
print("before useing the pop function:\nprathice_set:",prathice_set)
x=prathice_set.pop()#this will remove top element or random element and this will return element
print("after useing pop function\nprathice_set:",prathice_set)
print("""removed element is" """,x,""" " """)

print("====================")
print("clear function")
"""
clear() method
-->>clear() method is used to clear all items from set
"""
prathice_set={"apple","orange","pineapple","banana","grapes"}#set automaticallu remove the duplicate elements
print("before useing the remove function:\nprathice_set:",prathice_set)
prathice_set.clear()#this will remove all items from set
print("after useing the clear function\nprathice_set:",prathice_set)
print("========================================================================")
