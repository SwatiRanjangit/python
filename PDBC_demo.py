#               PDBC (Python Database Connectivity) for MS -SQL
#=======================================================================================

# MS-SQL CRUD(create, read, update, delete) OPEARTATIONS
from pyodbc import *



# READ DATA FROM DATABASE:
# def read(con):
#     print("Reading data from the database: ")
#     cur = con.cursor()
#     emp_data = cur.execute("SELECT * FROM table_name")
#     print(list(emp_data))
#     cur.execute("SELECT * FROM table_name")
#     for row in cur:
#           print(row)
      # print()

# read(con) to call read method

# INSERT DATA INTO DATABASE:

# def create(con):
#     print("Inserting data into database: ")
#     cur = con.cursor()
#     cur.execute("INSERT INTO emp(id,name,sal) values(?,?,?);",(2,"durga",10000))
#     con.commit()
#     read(con) # read so that to check that data inserted or not

# create(con)

# UPDATE DATA INTO DATABASE:

# def update_val(con):
#     print("updating data into database: ")
#     cur = con.cursor()
#     cur.execute("UPDATE emp SET name=?, sal=? WHERE id=?",("swati",30000, 2))
#     con.commit()
#     read(con) # read so that to check that data updated or not

# update_val(con)


# def delete_rec(con):
#     print("Deleting data from database: ")
#     cur = con.cursor()
#     cur.delete("DELETE FROM emp WHERE id=2")
#     con.commit()
#     read(con) # read so that to check that data inserted or not

# delete_rec(con)

# con = connect("Driver={driver_name}; server= server_name;database= database_name",) use to connect python to the database server
# read(con)
# create(con)
# update_val(con)
# delete_rec(con)
# con.close()
