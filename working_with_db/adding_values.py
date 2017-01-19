
import MySQLdb
import sys

USER_NAME = "root"
USER_PASS = "password"
USER_DB = "coursedb"


db=MySQLdb.connect(user=USER_NAME,
                   passwd=USER_PASS,
                   db=USER_DB)

cur =db.cursor()

SQL_QUERY = "INSERT INTO coursedb.courses (id, name, duration,tutor) VALUES (%s, %s ,%s, %s)"

values = (2001, 'Java', 40, 'delete from courses')

cur.execute(SQL_QUERY,
            values)

db.commit()
