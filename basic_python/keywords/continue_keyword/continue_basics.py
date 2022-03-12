#break keyword in break loop
for i in range(0,10):
    if i==3:
        continue
    print(i)
print("==========================================================")
#break keyword  in while loop
x=0
while x<1000:
   x+=1
   if x==100:
       continue
   print(x)
