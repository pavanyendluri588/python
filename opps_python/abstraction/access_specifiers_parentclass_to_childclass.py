class parent:
    #public:
    first_name="yendluri"
    #protected
    _second_name="pavan"
    #private
    __last_name="ram chandar"
    def __init__(self):
        print("this is a parent class constructor")

    def public(self):
        print("this is public function")
    def _protected(self):
        print("this is protected function")
    def __private(self):
        print("this is private function")
    def view(self):
        print("=======================================================")
        print("this is public member :",self.first_name)
        print("this is protected member :",self._second_name)
        print("this private member :",self.__last_name)
        self.public()
        self._protected()
        self.__private()
class child(parent):
    def __init__(self):
        print("this is child class constructor")

    def view(self):
        print("===================================================")
        print("this is public member :",self.first_name)
        print("this is protected member :",self._second_name)
        #print("this private member :",self.__last_name)
        """
        above atribute in print statement is last name is a private access modifier
        error for above print statement :
         print("this private member :",self.__last_name)
         AttributeError: 'child' object has no attribute '_child__last_name'
        """
        self.public()
        self._protected()
        #self.__private()
        """
        above method __private  is a private access modifier
        error for above print statement :
        self.__private()
        AttributeError: 'child' object has no attribute '_child__private'
        """

obj1=parent()

obj1.view()
print("=================================================")
print("obj1 is completed successfully")
print("=================================================")
obj2=child()
obj2.view()
print("=================================================")
print("obj2 is completed successfully")
print("=================================================")
