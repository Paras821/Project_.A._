
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "INSERT INTO employees(id,name,age,dept,salary,joined) VALUES (%s, %s, %s, %s, %s, %s)"
val = [
    ('1', 'Alice', '30', 'HR', '50000', '2020-02-15'),
    ('2', 'Bob', '25', 'IT', '60000', '2021-06-10'),
    ('3', 'Charlie', '35', 'Finance', '70000', '2018-11-23'),
    ('4', 'David', '28', 'IT', '55000', '2019-09-30'),
    ('5', 'Eva', '40', 'HR', '80000', '2017-07-01')
    ]

mycursor.executemany(sql,val)

conn.commit()

print(mycursor.rowcount, "Record(s) Inserted")

