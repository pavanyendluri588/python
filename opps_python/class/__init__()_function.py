"""
NOTE:The __init__() function is called automatically every time the class is being used to create a new object.
All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
"""

class computer_details:
    university_name="lovely professional university"  #university_nameis called property of a class
    def __init__(self,name,processor,hhd,cost,ram):
        self.name = name
        self.processor=processor
        self.hhd=hhd
        self.cost=cost
        self.ram=ram
    def display(self):                        #display  is called as methods of the class
        print("========================================================")
        #print("university_name:",university_name) #error:NameError: name 'university_name' is not defined
        print("university_name:",university_name) #this will print the university_name
        print("Name of the laptop:",self.name)
        print("Processor model:",self.processor)
        print("Storage space:",self.hhd)
        print("Cost of laptop:",self.cost)
        print("Ram in laptop",self.ram)

#===========================
"""
laptop_name=input("Enter laptop name:")
laptop_processor=input("Enter the laptop processor model number:")
laptop_hhd=input("Enter the laptop storage space:")
laptop_cost=input("Enter the laptop cost:")
laptop_ram=input("Enter the laptop ram storage space:")
#creating the object
student1=computer_details(laptop_name,laptop_processor,laptop_hhd,laptop_cost,laptop_ram)
student1.display()
"""
student2=computer_details("lenovo","i7 10gen","512 gb ssd",42000,"12_gb_ram")
#accessing the property of class name computer_details
print("this is the property of the class:",student2.university_name)
#accessing the methods of the class computer_details
student2.display()

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
