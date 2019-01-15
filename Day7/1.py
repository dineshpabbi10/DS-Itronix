class Employee:
	pass

robin = Employee()  # Here Robin and Rajat are 2 objects
rajat = Employee()

robin.fname="Robin"
robin.lname="Mahajan"
robin.salary=45000

rajat.fname="Rajat"
rajat.lname="Sharma"
rajat.salary=45000

print(robin,rajat)
print(robin.fname,rajat.fname)

