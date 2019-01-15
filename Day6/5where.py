import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="Python"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM student where name='karan'")

myresult = mycursor.fetchall()
print (myresult)

for x in myresult:
  print (x[0])
