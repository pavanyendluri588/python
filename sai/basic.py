#sum of digits of the number
"""
rev,sum,it=0,0,0
num1=int(input("Enter the number:"))
len_num1=len("num1")
print("lenth of num1",len_num1)
while it<=len_num1:
    rev=num1%10
    num1=num1//10
    sum=sum+rev
    it+=1
print("sum of digits  is ",sum)
"""
#factroial
fac=1
num2=int(input("Enter the number:"))
#len_num2=len("num2")
#print("lenth of number:",len_num2)
while num2>=3:
    fac=fac*num2
    num2-=1
print("factorial:",fac)
    

