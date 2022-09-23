import mysql.connector
mydb = mysql.connector.connect(
    host= 'localhost',
    username = 'payel',
    password = 'payel1987',
    database = "Employee"
)
print(mydb)

mycursor = mydb.cursor()
# mycursor.execute("Create database Employee")

mycursor.execute("Show databases")
for x in mycursor:
    print (x)
# mycursor.execute("create table EmployeeIn (EmpID int primary key, Name varchar(100), Department varchar(100))")
# mycursor.execute("create table Salary(EmpID int, Pay  int)")
mycursor.execute("Show tables")
for x in mycursor:
    print (x)

# sql = "Insert into EmployeeIn(EmpID, Name, Department) values (%s,%s,%s)"
# val = [
#   ('1','Peter', 'Admn'),
#   ('2','Amy', 'Software'),
#   ('3','Hannah', 'Data Analyst'),
#   ('4','Michael', 'Payroll'),
#   ('5','Sandy', 'Data Engineer'),
#   ('6','Betty', 'House Keeper'),
#   ('7','Richard', 'Java Developer'),
#   ('8','Susan', 'Manager'),
#   ('9','Vicky', 'Customer Care'),
#   ('10','Ben', 'Receptionist')
#
# ]



# mycursor.executemany(sql, val)
#
# mydb.commit()

mycursor.execute("Select * from EmployeeIn")
myresult = mycursor.fetchall()



for x in myresult:
    print (x)
# mycursor.execute("Alter table Salary add column RevisedDate DATE")
# sql = "Insert into Salary (EmpID,Pay, RevisedDate) values (%s,%s, %s)"
# val = [
#   ('1', '500', '2022-03-01' ),
#   ('2','1000', '2022-09-01'),
#   ('3','700','2022-09-06'),
#   ('4','600','2022-03-01'),
#   ('5','750','2022-07-01'),
#   ('6','400','2022-03-01'),
#   ('7','900','2022-06-01'),
#   ('8','1200','2022-04-01'),
#   ('9','450','2022-03-01'),
#   ('10','400','2022-03-01')
#
#  ]

# mycursor.executemany(sql, val)
#
# mydb.commit()

mycursor.execute("Select * from Salary")
myresult = mycursor.fetchall()
for x in myresult:
    print (x)

# sql = ("Select * from EmployeeIn order by Name")
mycursor.execute("Select * from EmployeeIn order by Name")
myresult = mycursor.fetchall()
for x in myresult:
    print (x)

mycursor.execute("Select distinct(EmpId) from Salary where Pay = (Select max(Pay) from Salary) ")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
mycursor.execute("select Name , Department from EmployeeIn where EmpId = 8 ")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
mycursor.execute("Select sum(pay) from Salary ")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

mycursor.execute("Select distinct(EmpId), pay from salary order by pay desc limit 3")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
mycursor.execute("Delete  from Salary where RevisedDate is NULL")
mydb.commit()

mycursor.execute("Select * from Salary order by RevisedDate desc")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
mycursor.execute("Select EmployeeIn.Name,EmployeeIn.Department, Salary.Pay, Salary.RevisedDate "
                 "from EmployeeIn join Salary on EmployeeIn.EmpId = Salary.EmpId")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# mycursor.execute("create view CompleteData as Select EmployeeIn.Name,EmployeeIn.Department, "
#                  "Salary.Pay, "
#                  "Salary.RevisedDate "
#                  "from EmployeeIn "
#                  "join Salary on EmployeeIn.EmpId = Salary.EmpId ")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)
mycursor.execute("select * from CompleteData")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

mycursor.execute("select name , pay from CompleteData where pay = (select max(pay) from CompleteData) ")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

