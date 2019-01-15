#Note: We can access class variable with class name(Employee) or also with instance name(self) : as we already studied difference b/w both
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


print(Employee.no_of_employees)
robin = Employee('Robin','Mahajan',54000)
print(Employee.no_of_employees)
rajat = Employee('Rajat','Sharma',54000)
print(Employee.no_of_employees)
