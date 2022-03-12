class maths_basic_operations:  #creating a class with  name maths_basic_operations
    """This is the doc string on the class.
    """
    def addition(self,a,b):
        """
        This is the docstring of the function in  class
        """
        print(f"num1:",a,"\nnum2:",b,"\n addtion of ",a,"+",b,"=",a+b)
    def subraction(self,a,b):
        """
        This is the docstring of the subraction function in the maths_basic_operations class

        """
        print(f"num1:",a,"\nnum2:",b,"\subraction of ",a,"-",b,"=",a-b)
    def multiplication(self,a,b):
        """
        This is the docstring of the multiplication function in the maths_basic_operations class

        """
        print(f"num1:",a,"\nnum2:",b,"\multiplication of ",a,"*",b,"=",a*b)
    def division(self,a,b):
        """
        This is the docstring of the division function in the maths_basic_operations class

        """
        print(f"num1:",a,"\nnum2:",b,"\division of ",a,"/",b,"=",a/b)
p1=maths_basic_operations()
p1.addition(5,6)
p1.subraction(7,8)
p1.multiplication(4,4)
p1.division(4,9)
"""docstrings

"""
print(maths_basic_operations.__doc__)
print(p1.addition(1,2).__doc__)
help(maths_basic_operations)
print(maths_basic_operations.__get__)
