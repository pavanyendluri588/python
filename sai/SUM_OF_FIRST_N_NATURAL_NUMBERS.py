"""
sum=0
num=int(input("Enter the number:"))
for i in range(num+1):
    sum=sum+i
print("sum of first ",num," natural numbers is ",sum)
"""
"""
#table
for i in range(1,6):
    for j in range(1,11):
        print(i," * ",j," = ",i*j)
    print("        ")
"""
"""
#stars:
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=(" "))
    print(" ")
"""
num=7
for i in range(7):
    num=num-1
    for j in range(num,0,-1):
       print("*",end=" ")
    print(" ")
