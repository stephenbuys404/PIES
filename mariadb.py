#mariadb
import sys
import mariadb

try:
    con=mariadb.connect(
    user='root',
    password='mypassword',
    host='localhost',
    port=3306,
    database='companydb'
)
except(mariadb.Error)as ex:
    print(f'{ex}')

cur = con.cursor()
def CreateTable(cur):
    cur.execute('CREATE TABLE employees (name VARCHAR(30), age INTEGER)');

def InsertToTable(cur,con):
    #cur.execute('INSERT INTO employees (name, age) VALUES ('Joel M', 27), ('Mary K', 33),('Bosco C', 45)')
    con.commit()
    con.autocommit = False

def FindData(cur):
    data = cur.execute('SELECT name, age FROM employees')
    for (name, age) in data:
        print('Name:', {name}, 'Age:', {age})

#CreateTable(cur)
#InsertToTable(cur,con)
FindData(cur)
con.close()