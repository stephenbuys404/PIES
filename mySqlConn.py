#mysql
#mysql-connector
#mysql-connector-python

import mysql.connector
import MySQLdb

#db=mysql.connector.connect(host= localhost ,user= root ,passwd=  )

db=mysql.connector.connect(host= localhost ,user= root ,passwd= ,database= testdatabase )

mycursor=db.cursor()

#mycursor.execute( CREATE DATABASE testdatabase )

#mycursor.execute( CREATE TABLE Person(name VARCHAR(60),age smallint UNSIGNED,personID int PRIMARY KEY AUTO_INCREMENT) )

#mycursor.execute( DESCRIBE Person )
#for x in mycursor:
#    print(x)

#mycursor.execute( DELETE FROM Person WHERE age>3; )
#db.commit()

#mycursor.execute( INSERT INTO Person(name,age) VALUES (%s,%s) ,( James ,12))
#db.commit()

mycursor.execute( SELECT * FROM Person )
for x in mycursor:
    print(x)