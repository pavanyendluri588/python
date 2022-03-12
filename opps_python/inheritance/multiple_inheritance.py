class parent1:
    def __init__(self,first_name,middle_name,last_name,age):
        self.first_name=first_name
        self.middle_name=middle_name
        self.last_name=last_name
        self.age=age
        print("this is the parent1 class")
    def view(self):
        print("=============================================")
        print("parent1 class view function")
        print("first_name:",self.first_name)
        print("middle_name:",self.middle_name)
        print("last_name:",self.last_name)
        print("age:",self.age)
class parent2():
    def __init__(self,first_name,middle_name,last_name,age,phone_number):
        #parent.__init__(self,first_name,middle_name,last_name,age)
        self.first_name=first_name
        self.middle_name=middle_name
        self.last_name=last_name
        self.age=age
        self.phone_number=phone_number
        print("this is the parent2 class")
    def view(self,atm_number):
        print("============================================")
        print("parent2 class view function")
        print("first_name:",self.first_name)
        print("middle_name:",self.middle_name)
        print("last_name:",self.last_name)
        print("age:",self.age)
        print("phone_number:",self.phone_number)
        print("atm_number:",atm_number)
class child(parent1,parent2):
    def __init__(self,first_name,middle_name,last_name,age,phone_number):
        parent1.__init__(self,first_name,middle_name,last_name,age)
        parent2.__init__(self,first_name,middle_name,last_name,age,phone_number)

        self.pan_number="pan_number"
        self.voter_id="voter_id"
        print("this is the child class")
    def view(self,inter_marks,btech_marks):
        print("============================================")
        print("child class view function")
        print("first_name:",self.first_name)
        print("middle_name:",self.middle_name)
        print("last_name:",self.last_name)
        print("age:",self.age)
        print("phone_number:",self.phone_number)
        print("pan_number:",self.pan_number)
        print("voter_id:",self.voter_id)
        print("inter_marks:",inter_marks)
        print("btech_marks:",btech_marks)
obj1=parent1("yendluri","pavan","ram chandar",28)
obj1.view()
print("============================================")
print("parent1 class obj is completed")
print("============================================")
obj=parent2("yendluri","pavan","ram chandar",28,9110564858)
#obj.view(3434323432)
print("============================================")
print("parent2  class obj is completed")
print("============================================")
obj2=child("yendluri","pavan","ram chandar",30,9347308435)
obj2.view(7.8,8.9)
print("============================================")
print("child class obj is completed")
print("============================================")
