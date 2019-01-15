#Class Methods As Alternative Constructor
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

robin = Employee('Robin','Mahajan',54000) 
rajat = Employee('Rajat','Sharma',54000)

akshay = Employee.from_str("Akshay-Arora-67000")
print (akshay.fname)
print (akshay.lname)
print (akshay.salary)





