class access_modifiers:
    def __init__(self):
        pass
    #public access modifiers
    """
    The members of a class that are declared public are easily accessible from any part of the program.
    All data members and member functions of a class are public by default.
    the members in the class by default is public.
    """
    name="public"
    age=1
    ph_no=9949978983

    #============================================================================
    #protected access modifiers
    """
    The members of a class that are declared protected are only accessible to a class derived from it.
    Data members of a class are declared protected by adding a single underscore ‘_’ symbol before the data member of that class.
    """
    _name="protected"
    _age=1
    _ph_no=9110564858
    def _protected_class_function(name,age,ph_no):
        _name=name
        _age=age
        _ph_no=ph_no
        print("protected_class_function=======================================")
        print(_name,_age,_ph_no)
    _protected_class_function("pavan",19,11111111111111)
    #============================================================================
    #priviate access modifiers
    """
    The members of a class that are declared private are accessible within the class only, private access modifier is the most secure access modifier.
    Data members of a class are declared private by adding a double underscore ‘__’ symbol before the data member of that class.
    """
    __name="priviate"
    __age=2
    __ph_no=9347308435
class b1(access_modifiers): #acces moodifiers in  protected

    _protected_class_function("prudhvi",11,222222222222222222222)
    _protected_class_function("Rama",22,3333333333333333)
#creating object
obj1=access_modifiers()
