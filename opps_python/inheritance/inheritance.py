
class parent:
    def __init__(self,fname,fage):
        self.name=fname
        self.age=fage
    def view(self):
        print("name:",self.name,"\nage:",self.age)
class child(parent):
    def __init__(self,fname,fage,flast_name):
        parent.__init__(self,fname,fage)
        self.last_name=flast_name
    def view(self):
        print("name:",self.name,"\nage:",self.age,"\nlast_name",self.last_name)
obj=child("pavan",23,"yendluri")
obj.view()
obj.parent.view()
