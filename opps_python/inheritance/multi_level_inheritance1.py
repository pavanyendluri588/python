class parent:
    def __init__(self,first_name,middle_name,last_name,age):
        self.first_name=first_name
        self.middle_name=middle_name
        self.last_name=last_name
        self.age=age
        print("this is parent constructor:")
    def view(self):
        print("parent class")
        print("first_name:",self.first_name)
        print("middle_name:",self.middle_name)
        print("last_name:",self.last_name)
        print("age:",self.age)
class layer1(parent):
    def __init__(self,first_name,middle_name,last_name,age,phone_number):
        parent.__init__(self,first_name,middle_name,last_name,age)
        self.phone_number=phone_number
        print("this is layer1 constructor:")
    def view(self,atm_number):
        print("============================================")
        print("layer1 class")
        print("first_name:",self.first_name)
        print("middle_name:",self.middle_name)
        print("last_name:",self.last_name)
        print("age:",self.age)
        print("phone_number:",self.phone_number)
        print("atm_number:",atm_number)
class layer2(layer1):
    def __init__(self,first_name,middle_name,last_name,age,phone_number):
        layer1.__init__(self,first_name,middle_name,last_name,age,phone_number)
        self.phone_number=phone_number
        self.pan_number="pan_number"
        self.voter_id="voter_id"
        print("this is layer2 constructor:")
    def view(self,tenth_marks):
        print("============================================")
        print("layer2 class")
        print("first_name:",self.first_name)
        print("middle_name:",self.middle_name)
        print("last_name:",self.last_name)
        print("age:",self.age)
        print("phone_number:",self.phone_number)
        print("pan_number:",self.pan_number)
        print("voter_id:",self.voter_id)
        print("tenth_marks:",tenth_marks)
        #print("btech_marks:",btech_marks)
obj=parent("yendluri","pavan","ram chandar",10)
obj.view()
print("============================================")
print("parent obj is completed")
print("============================================")
obj1=layer1("yendluri","pavan","ram chandar",20,9949978983)
obj1.view(3434323432)
print("============================================")
print("layer1 obj is completed")
print("============================================")
obj2=layer2("yendluri","pavan","ram chandar",30,9110564858)
obj2.view(9.2)
print("============================================")
print("layer2 obj is completed")
print("============================================")
