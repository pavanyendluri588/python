class parent:
    def __init__(self):
        print("this is constructor of parent class")
    def __del__(self):
        print("this is destructor of parent class")
    def function(self):
        print("this is function")
obj=parent()
obj.function()
print("==============================================")
print("obj is  parent class object is executed")
print("==============================================")
obj1=parent()
obj1.function()
print("==============================================")
print("obj1 is  parent class object is executed")
print("==============================================")
print("+++++++++++++++++++++++++++++++++++++")
print("+++++++++++++++++++++")
print("program  is ended")
