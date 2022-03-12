#inner class:
"""
the class created in the  another class is called inner class.
ItIf an object is created using child class means inner class then the object can also be used by parent class or root class.
A parent class can have one or more inner class but generally inner classes are avoided.

We can make our code even more object oriented by using inner class.
A single object of the class can hold multiple sub-objects. We can use multiple sub-objects to give a good structure to our program.
"""
class parent_class:
    """

    """
    def __init__(self):
        """

        """
        self.first_name="yendluri"
        self.middle_name="pavan"
        self.last_name="ram chandar"
    def display(abcd):
        """

        """
        print("first name:",abcd.first_name)
        print("middle name:",abcd.middle_name)
        print("last_name:",abcd.last_name)
    class inner_class:
        """

        """
        def __init__(inner_self):
            """

            """
            inner_self.atm_no=1234567890121234
            inner_self.pan_no="1q2w3e4r4f5g6h"
            inner_self.adhar_no=78945612
            inner_self.add="bhavanipuram"
        def display_abcd(abcd1):
            """

            """
            print("======================================================")
            print("display_abcd1:atm_no=",abcd1.atm_no)
            print("display_abcd1:pan_no=",abcd1.pan_no)
            print("display_abcd1:adhar_number=",abcd1.adhar_no)
            print("display_abcd1:address= ",abcd1.add)
            """
            error:NameError: name 'inner_self' is not defined
            print("display_inner_self:atm_no=",inner_self.atm_no)
            print("display_inner_self:pan_no=",inner_self.pan_no)
            print("display_inner_self:adhar_number=",inner_self.adhar_no)
            print("display_inner_self:address= ",inner_self.add)
            """
        def display_sub_abcd(abcd1):
            """

            """
            abcd1.atm_no="1234 4321 3456 4567"
            abcd1.pan_no="hwsb82y8ye3e3ey1y"
            abcd1.adhar_no=346347326432782377
            abcd1.add="vijayawada"
            print("======================================================")
            print("display_sub_abcd1:atm_no=",abcd1.atm_no)
            print("display_sub_abcd1:pan_no=",abcd1.pan_no)
            print("display_sub_abcd1:adhar_number=",abcd1.adhar_no)
            print("display_sub_abcd1:address= ",abcd1.add)
        def display_sub_of_constructor(inner_self):
            """

            """
            print("=======================================================")
            print("display_inner_self:atm_no=",inner_self.atm_no)
            print("display_inner_self:pan_no=",inner_self.pan_no)
            print("display_inner_self:adhar_number=",inner_self.adhar_no)
            print("display_inner_self:address= ",inner_self.add)
        def p(self):
            print("first name:",self.first_name)
            print("middle name:",self.middle_name)
            print("last_name:",self.last_name)



parent_obj=parent_class()
parent_obj.display()
inner_obj=parent_obj.inner_class()
inner_obj.display_abcd()
inner_obj.display_sub_abcd()
inner_obj.display_sub_of_constructor()
inner_obj.p()
