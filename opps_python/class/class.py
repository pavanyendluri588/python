#creating the class
#class class_name:
#syntax:
#class classname:
#class siite

class employee:
    id=10
    name="pavan"
    
    def input(myself):
        myself.id=input("Enter your id:")
        myself.name=input("Enter your name:")
 
    def display(self):
        print("self.id",self.name)
obj=employee()
obj.display()
print("employee.id=",employee.id)
print("employee.name=",employee.name)

class employee:
    def display(myself,x,y):
        print("x,y",x,y)
obj1=employee()
cs=obj1.display(56,'pavan')
print("cs=",cs)