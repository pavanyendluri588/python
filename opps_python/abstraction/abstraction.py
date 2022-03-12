from abc import  ABC,abstractmethod

class absclass(ABC):

	def bank_details(self):
		print("this is bank_details method before abstract method")
	@abstractmethod
	def process(self):
		print("this is process method after abstract method")
	def system_recquirement_check(self):
		print("this is system_recquirement_check method agter the abstract class")
obj1=absclass
obj1.bank_details("pavan")
obj1.process("pavan")
