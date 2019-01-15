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
	def change_increment(cls,amount): #It takes class as a argument instead of self(instance)
		cls.increment=amount

robin = Employee('Robin','Mahajan',54000) 
rajat = Employee('Rajat','Sharma',54000)

print(robin.salary)
Employee.change_increment(3)
robin.increase()
print(robin.salary)







