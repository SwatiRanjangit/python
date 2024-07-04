import mysql.connector

cursor = ''
cur = ''
con = ''

try:
    con = mysql.connector.connect(user='root',password='123456789',database='crudop',host='localhost',port=3306)
    cursor = con.cursor()
    cursor.execute("create table emp(id int(5) primary key, name varchar(20), sal int, address varchar(20))")
    print("Table is created")
    sql = "INSERT INTO emp(id ,name ,sal , address) values(%s,%s,%s,%s)"
    records = [(101,"swati",4500000,"delhi"),(102,"tiya",100000,"mp"),(103,"teesa",23000,"up")]
    cursor.executemany(sql,records)
    con.commit()
    print("Record inserted successfully")
    cursor.execute("SELECT * from emp")
    emp_data = cursor.fetchall()
    for e in emp_data:
        print(e)
    print()


except Exception as e:
    if con == True:
        con.rollback()
        print("There is problem with sql ", e)
    else:
        print("connection failed", e)
finally:
    if cursor:
        print("finally block")
        cursor.close()
    if con:
        con.close()
