class parent:
    def __init__(self,first_name,middle_name,last_name,age):
        self.first_name=first_name
        self.middle_name=middle_name
        self.last_name=last_name
        self.age=age
    def view(self):
        print("parent class")
        print("first_name:",self.first_name)
        print("middle_name:",self.middle_name)
        print("last_name:",self.last_name)
        print("age:",self.age)
class child(parent):
    def __init__(self,first_name,middle_name,last_name,age,phone_number):
        parent.__init__(self,first_name,middle_name,last_name,age)
        self.phone_number=phone_number
    def view(self,atm_number):
        print("============================================")
        print("child class")
        print("first_name:",self.first_name)
        print("middle_name:",self.middle_name)
        print("last_name:",self.last_name)
        print("age:",self.age)
        print("phone_number:",self.phone_number)
        print("atm_number:",atm_number)

obj1=parent("yendluri","pavan","ram chandar",28)
obj1.view()
obj=child("yendluri","pavan","ram chandar",28,9110564858)
obj.view(3434323432)
