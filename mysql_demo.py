import mysql.connector
try:
    con = mysql.connector.connect(user='root',password='123456789',database='pythonDB',host='localhost',port=3306)
    if con.is_connected():
        print("Connected Successfully")
        # print("Database created Successfully")
        # print("Table created Successfully")
        # print("Record inserted Successfully")
        # print("deleted Successfully")
        print("data updated Successfully")
except:
    print("Not connected")

# CREATE DATABASE:
# sql = "CREATE DATABASE pythonDB"
# cur = con.cursor()
# cur.execute(sql)
# cur.close()
# con.close()

# CREATE TABLE :
# sql1 = "create table emp(id int, name varchar(20), sal int, address varchar(20))"
# cur = con.cursor()
# cur.execute(sql1)
# cur.close()
# con.close()

# INSERT DATA:
# sql1 = "INSERT INTO emp(id ,name ,sal , address) values(101, 'swati', 300000, 'Patna')"
# cur = con.cursor()
# cur.execute(sql1)
# con.commit()
# cur.close()
# con.close()


# sql1 = "INSERT INTO emp(id ,name ,sal , address) values(101, 'swati', 300000, 'Patna'),(102, 'RIYA', 200000, 'Patna')"
# cur = con.cursor()
# cur.execute(sql1)
# con.commit()
# cur.close()
# con.close()

# DELETE DATA:
# sql1 = "DELETE FROM emp where id= 102"
# cur = con.cursor()
# cur.execute(sql1)
# con.commit()
# cur.close()
# con.close()

# UPDATE DATA:
# sql1 = "UPDATE emp set name='harish', sal= 230000, address='delhi' where id= 101"
# cur = con.cursor()
# cur.execute(sql1)
# con.commit()
# cur.close()
# con.close()

# READ DATA:
sql1 = "SELECT * FROM emp"
cur = con.cursor()
cur.execute(sql1)
emp_data = cur.fetchall()
# print(emp_data)

for e in emp_data:
    print(e)
print()

cur.close()
con.close()