#Inheritance
class Employee:
	increment=1.5
	no_of_employees=0
	def __init__(self,fname,lname,salary):
		self.fname=fname
		self.lname=lname
		self.salary=salary
		Employee.no_of_employees +=1
	
	def increase(self): 
		self.salary=int(self.salary * self.increment)

	@classmethod
	def change_increment(cls,amount): 
		cls.increment=amount
	
	@classmethod
	def from_str(cls,emp_string):
		fname,lname,salary=emp_string.split("-")
		return cls(fname,lname,salary)

	@staticmethod
	def isopen(day):
		if day=="sunday":
			return False
		else:
			return True


class Programmer(Employee):
	def __init__(self,fname,lname,salary,proglang,exp):
		#self.fname=fname
		#self.lname=lname
		#self.salary=salary
		super().__init__(fname,lname,salary)
		self.proglang=proglang
		self.exp=exp
#instead of self.fname=fname, self.lname=lname, self.salary=salary , Kindly use super().__init__(fname,lname,salary), Super will automatic get all the member os init function

	def increase(self): 
		self.salary=int(self.salary * (self.increment+0.2))

akshay=Programmer('Akshay','Arora',76000,'Python','7 Years') 
print(akshay.fname)
print(akshay.exp)



