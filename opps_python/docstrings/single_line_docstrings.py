"""
single line doc strings :
docstrings are used to write a documentation about the class,functions,...etc

Rules for declearing the doc strings"

"""
class details:
      pavan="name"
      """this class is used to to get the details and display the details """
      name="none"
      age="none"
      phone_number="none"
      def input(self,name,age,phone_number):
           """This function is use to get the input""" 
           self.name=name
           self.age=age
           self.phone_number=phone_number
      def display():
           """tthus function is used to display the details"""
           print("name of the student:",self.name)
           print("age  of the student:",self.age)
           print("phone number  of the student:","self.phone_number")
obj1=details()
x=obj1.__doc__
print(x)
y=help(obj1)
print(y)
z=obj1.input.__doc__
print(z)