#Dunder Method
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
	
	def __add__(self,other):
		return self.salary + other.salary

	def __repr__(self):
		return 'Employee({}, {}, {})'.format(self.fname,self.lname,self.salary)

	def __str__(self):
		return 'The Name of Employee is {}'.format(self.fname)

robin = Employee('Robin','Mahajan',54000) 
rajat = Employee('Rajat','Aggarwal',100)
print(robin+rajat)

print(robin)
print(str(robin))
print(repr(robin))

"""
print(7+5)  :  12
print('7'+'5') : 75 

a=7
print(a.__add__(5))

here __add__ is a dunder method : 

"""
