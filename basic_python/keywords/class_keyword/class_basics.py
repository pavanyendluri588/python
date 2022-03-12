class maths_basic_operations:  #creating a class with  name maths_basic_operations

    def addition(self,a,b):
        print(f"num1:",a,"\nnum2:",b,"\nAddtion of ",a,"+",b,"=",a+b)
    def subraction(self,a,b):
        print(f"num1:",a,"\nnum2:",b,"\subraction of ",a,"-",b,"=",a-b)
    def multiplication(self,a,b):
        print(f"num1:",a,"\nnum2:",b,"\multiplication of ",a,"*",b,"=",a*b)
    def division(self,a,b):
        print(f"num1:",a,"\nnum2:",b,"\division of ",a,"/",b,"=",a/b)
p1=maths_basic_operations()
p1.addition(5,6)
p1.subraction(7,8)
p1.multiplication(4,4)
p1.division(4,9)
print(maths_basic_operations.__doc__)#
