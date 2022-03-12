from abc import ABC, abstractmethod
class Absclass(ABC):
    def print(self,x):
        print("Passed value: ", x)
    #@abstractmethod
    def task(self):
        print("We are inside Absclass task")
 
class test_class(Absclass):
    def task(self):
        print("We are inside test_class task")
 
class example_class(Absclass):
    def task(self):
        print("We are inside example_class task")
#createu=ing obj file cor obstract class
Absclass_obj=Absclass()
"""
ERROR:
before removing abstractmethod 
Absclass_obj=Absclass()
TypeError: Can't instantiate abstract class Absclass with abstract method task
after removeing abstractclass
output:
Passed value:  1000
We are inside test_class task
Passed value:  100
We are inside example_class task
Passed value:  200
test_obj is instance of Absclass?  True
example_obj is instance of Absclass?  True

"""
Absclass_obj.print(1000)
#object of test_class created
test_obj = test_class()
test_obj.task()
test_obj.print(100)
 
#object of example_class created
example_obj = example_class()
example_obj.task()
example_obj.print(200)
 
print("test_obj is instance of Absclass? ", isinstance(test_obj, Absclass))
print("example_obj is instance of Absclass? ", isinstance(example_obj, Absclass))
