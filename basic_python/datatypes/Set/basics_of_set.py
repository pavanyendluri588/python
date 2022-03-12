set={"Monday","Tuesday","Wednesday","Thusday","Friday","Saturday"}
print("set:",set)
print("type(set):",type(set))
count=0
for x in set:
  print("set[%d]:%s"%(count,x))
  count+=1

#empty curly brakets will create dictionary
set1={}
print("set1={} type(set1)",type(set1))

#to create empty set we use ste() function
#set2=set()
#print("set2=set() type(set2)",type(set2))

#adding items to set using 2 methods
#1.add() function add function will take only one attribute  error:TypeError: set.add() takes exactly one argument 
#2.update() function
#add() function
set111={"monday","tuesday","wednesday"}
print("before updating set111:",set111)
set111.add("thesday")
print("after updating set111:",set111)

#update() function
print("before updateing set111:",set111)
set111.update(["friday","saturday"])
print("after updateing set111:",set111)


#removeing from the list we have 2 methods
#1.discord
#2.remove
#discard:
set222={"pavan","prudhvi","rama","venkat","raviteja","ammu","prassana","varalakshmi","chilakala","pedhasubarao"}
print("before discarding set222:",set222)
set222.discard("chilakala")
print("after discarding set222:",set222)

#remove:
print("before discarding set222:",set222)
set222.remove("pedhasubarao")
print("after discarding set222:",set222)

#pop() function is used to remove an item feom a set .actually pop will remove the last item but in unordered,
#we can't determine which element will be poped from the set
count=1
for x in range(0,len(set222)):
    set222.pop()
    print("pop[%d]=%s"%(count,set222))
    count+=1

#python provides clear() finction to cleat all the items in the set
set333={"pavan","prudhvi","rama","venkat","raviteja","ammu","prassana","varalakshmi","chilakala","pedhasubarao"}
print("before using clear finction set333:",set333)
set333.clear()
print("after using clear function set333:",set333)

#difference between discord and remove.
#discard this will not give error if the item is not present on the set
#remove this will give a error if the item is not present on the set
set11={"Monday","Tuesday","Wednesday","Thusday","Friday","Saturday"}
set11.discard("sunday")
print("discard will not give any error")
#set11.remove("sunday")
print("""remove function will give this error set11.remove("sunday")  KeyError: 'sunday' """)