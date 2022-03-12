class details:
    def __init__(self,name,age,ph_no):
        self.name_1 = name
        self.age_1 = age
        self.ph_no_1=ph_no
    def display(myself):
        #        print("name of preson:",myself.name)   # AttributeError: 'details' object has no attribute 'name'
        print("name of preson:",myself.name_1)
        print("age of the person:",myself.age_1)
        print("phone number of preson:",myself.ph_no_1)
obj_1=details("Pavan",19,9110564858)
obj_1.display()
