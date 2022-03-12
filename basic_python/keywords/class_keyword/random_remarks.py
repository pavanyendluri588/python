class details:
    name="pavan"
    age=29
    ph_no=9110564858
    atm_no=2222333344445555
d1=details()
print("d1.name:",d1.name,"\nd1.ph_no:",d1.ph_no,"\nd1.age:",d1.age,"\nd1.atm_no:",d1.atm_no)
d1.age=150
print("d1.name:",d1.name,"\nd1.ph_no:",d1.ph_no,"\nd1.age:",d1.age,"\nd1.atm_no:",d1.atm_no)

class  example:
    pass
#createing the object name emp1 of class example
emp1=example()
emp1.name="pavan"
emp1.age=20
emp1.ph_no=9110564858
print("emp1.name:",emp1.name)
print("emp1.age:",emp1.age)
print("emp1.ph_no:",emp1.ph_no)
print(emp1)
class Details_1:
    
    def __init__(self,first_name,middle_name,last_name,age,ph_no):
        self.f_n=first_name
        self.m_n=middle_name
        self.l_n=last_name
        self.a=age
        self.p_n=ph_no
        print(self.f_n)
        print()
    def fun_1(self,name,age1):
        print("this is fun_1 ==============================================")
        print("name:",name)
        print("age:",age1)
        print("name of the student:",name)
        print("age of the student",age1)
        print("end of fun_1 ===============================================")
obj_1=basic_constructor("yendluri","pavan","ramchandar",19,9110564858)
obj_1.fun_1("pavan",19)
