class Employee:
	increment=1.5 #This is common for all the employee
	def __init__(self,fname,lname,salary):
		self.fname=fname
		self.lname=lname
		self.salary=salary
		
	
	def increase(self): 
		#self.salary=int(self.salary * increment)
		#self.salary=int(self.salary * Employee.increment)
		self.salary=int(self.salary * self.increment) # first it will search in __init__ if not found then search in class.

robin = Employee('Robin','Mahajan',54000) 
rajat = Employee('Rajat','Sharma',54000)

print(robin.salary)
robin.increase()
print(robin.salary)

print(robin.__dict__)

robin.dept="Sales"
print(robin.__dict__)
print(Employee.__dict__)

