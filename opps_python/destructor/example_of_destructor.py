# Python program to illustrate destructor

class A:
    def __init__(self,bb):
        """
        A class  documentation
        """
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        print("this is  class A constructor")
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        self.b = bb

class B:
    def __init__(self):
        """
        B class constructor
        """
        print("ccbccbccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbbcbbcbbcbbcbbcbcbcbcbcbbccbcbc")
        print("starting of B constructor")
        print("before A ")
        self.a = A(self)
        print("after A")
        print("end od the constructor")
        print("ccbccbccbccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")

    def __del__(self):
        print("bdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbddbdbdbdbbd")
        print("destructor of class B")
        print("die")
        print("bdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbddbdbdbdbbd")

def fun():
    b = B()

fun()
