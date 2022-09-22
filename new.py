import mysql.connector
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="payel",
  password="payel1987"
)

print(mydb)

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="payel",
  password="payel1987"
)

# mycursor = mydb.cursor()
#
# mycursor.execute("CREATE DATABASE PaySystems")

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="payel",
  password="payel1987"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

# mycursor.execute("CREATE TABLE PaySystem.employee (name VARCHAR(255), department VARCHAR(255), pay int)")
print("database data")
mycursor.execute("USE PaySystem")
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)

# mycursor.execute("select * from PaySystem.employee")
# mycursor.execute("insert into employee (name, department, pay) values ('Payel Banerjee', 'Bill', '500')")

sql = "INSERT INTO PaySystem.employee (name, department, pay) VALUES (%s, %s, %s)"
val = ("John", "Bill", "500")


for i in range(600,700):
  val = ("John", "Bill", str(i))
  mycursor.execute(sql, val)
mydb.commit()

mycursor.execute("select * from PaySystem.employee")
for x in mycursor:
  print(x)
mycursor.execute("select count(name) as Total_Employee from employee")
for x in mycursor:
  print(x)

mycursor.execute("select sum(pay) from employee")
for x in mycursor:
  print(x)

mycursor.execute("select name, pay from employee where pay = (select max(pay) from employee)")
for x in mycursor:
  print(x)
