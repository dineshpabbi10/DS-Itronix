class Employee:
	increment=1.5
	def __init__(self,fname,lname,salary):
		self.fname=fname
		self.lname=lname
		self.salary=salary
	
	def increase(self):
		pass

robin = Employee('Robin','Mahajan',54000) 
rajat = Employee('Rajat','Sharma',54000)

print(robin,rajat)
print(robin.fname,rajat.fname)

robin.increase() #  here self automatically called cz of class
