
import MySQLdb
import sys

USER_NAME = "root"
USER_PASS = "password"
USER_DB = "coursedb"


db=MySQLdb.connect(user=USER_NAME,
                   passwd=USER_PASS,
                   db=USER_DB)

cur =db.cursor()

SQL_QUERY = "INSERT INTO coursedb.courses (id, name, duration,tutor) VALUES (%s, %s ,%s, %s)"%(1010,"'js'",40,"'murthy'")

cur.execute(SQL_QUERY)

db.commit()
