import mysql.connector
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="payel",
  password="payel1987"
)

print(mydb)





mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE PaySystem")





mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

# mycursor.execute("CREATE TABLE PaySystem.employee (name VARCHAR(255), department VARCHAR(255), pay int)")
# print("database data")
# mycursor.execute("USE PaySystem")
# mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)

mycursor.execute("select * from PaySystem.employee")


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

# mycursor.execute("Create database EmployeeSystem")
# mycursor.execute("Create table employeedata  (id int primary key auto_increment, name varchar(50), year_join  date)")
# mycursor.execute("Show tables")
# for x in mycursor:
#   print(x)

sql = "INSERT INTO employeedata(name, year_join)  values(%s,%s)"
val = [('John','2020-01-12'),('Peter', '2020-01-01')]
mycursor.executemany(sql,val)
mydb.commit

mycursor.execute("Select * from employeedata")

myresult = mycursor.fetchall()
for x in myresult:
  print(x)

sql = ( "Select * from employeedata where name = 'John' ")
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

sql = ("Select * from employee order by pay desc limit 5 offset 2")
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

sql = ("update employee set department = 'Admn' where department = 'Bill'")
mycursor.execute(sql)
mydb.commit()
sql = ("select * from employee limit 5 ")
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)



