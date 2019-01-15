import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="Python"
)
mycursor = mydb.cursor()
sql = "DELETE FROM student WHERE name = 'karan'"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
