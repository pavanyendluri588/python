class parent:
    """
    person details
    """
    def __init__(self,first_name,middle_name,last_name,age,gender):
        self.first_name=first_name
        self.middle_name=middle_name
        self.last_name=last_name
        self.age=age
        self.gender=gender

class child1(parent):

    """
    bank account details

    this child3 class will give the information about bank account details information
    """
    def __init__(self,first_name,middle_name,last_name,age,gender,bank_username,bank_password):
        parent.__init__(self,first_name,middle_name,last_name,age,gender)
        self.username=bank_username
        self.password=bank_password
        print("this is child1 constructor")
    def view(self):
        """
        this is the view function of child1 class
        """
        print("=========================================")
        print("first_name:",self.first_name)
        print("middle_name:",self.middle_name)
        print("last_name:",self.last_name)
        print("age:",self.age)
        print("gender:",self.gender)
        print("============")
        print("bank_username:",self.username)
        print("bank_password",self.password)
        print("============")
class child2(parent):
    """
    adhar details

    this child3 class will give the information about Adhar information
    """
    def __init__(self,first_name,middle_name,last_name,age,gender):
        parent.__init__(self,first_name,middle_name,last_name,age,gender)
    def view(self,adhar_name,adhar_number):
        """
        this is the view function of child2 class
        """
        print("================================================")
        print("this is child2 class")
        print("first_name:",self.first_name)
        print("middle_name:",self.middle_name)
        print("last_name:",self.last_name)
        print("age:",self.age)
        print("gender:",self.gender)
        print("==========")
        print("adhar_name:",adhar_name)
        print("adhar_number",adhar_number)
        print("==========")

class child3(parent):
    """
    btech information

    this child3 class will give the information about btech information
    """
    def __init__(self,first_name,middle_name,last_name,age,gender):
        parent.__init__(self,first_name,middle_name,last_name,age,gender)
        print("this is child3 class constructor")
    def view(self,btech_collage_name,btech_marks):
        """
        this is the view function of child3 class
        """
        print("================================================")
        print("this is child3 class")
        print("first_name:",self.first_name)
        print("middle_name:",self.middle_name)
        print("last_name:",self.last_name)
        print("age:",self.age)
        print("gender:",self.gender)
        print("==========")
        print("btech_collage_name:",btech_collage_name)
        print("btech_marks:",btech_marks)
        print("==========")

obj1=parent("yendluri","pavan","ram chandar",19,"male")
print("====================================================")
print("parent object is completed")
print("====================================================")
obj2=child1("yendluri","pavan","ram chandar",19,"male","PAVANYENLDLURI@UNION","jdnfHSBH@^*&")
obj2.view()
print("====================================================")
print("child1 object is completed")
print("====================================================")
obj3=child2("yendluri","pavan","ram chandar",19,"male")
obj3.view("yendluri pavan ram chandar","1234 5678 9012 3456")
print("====================================================")
print("child2 object is completed")
print("====================================================")
obj4=child3("yendluri","pavan","ram chandar",19,"male")
obj4.view("LOVELY PROFESSIONAL UNIVERSITY",9.1)
print("====================================================")
print("child3 object is completed")
print("====================================================")
