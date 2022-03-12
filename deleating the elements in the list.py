l=[1,3,5,7,9,2,1,3,4,5,4,6,8,7,6,7,9]
len=len(l)
l1=1
c=0
for i in range(0,len):
    print("list itertion:",i,"list[",i,"]=",l[i])
    for j in range(1,len):
       if l[i]==l[j]:
           del l1[j]
print(l)
print("==============================================================")
print(l1)
print(c)