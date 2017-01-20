
import MySQLdb
import sys
import MySQLdb.cursors

USER_NAME = "root"
USER_PASS = "password"
USER_DB = "coursedb"


db=MySQLdb.connect(user=USER_NAME,
                   passwd=USER_PASS,
                   db=USER_DB,
                   cursorclass=MySQLdb.cursors.DictCursor)

cur = db.cursor()

SQL_QUERY = "SELECT * FROM coursedb.courses"

cur.execute(SQL_QUERY)

for row in cur:
    print row

db.close()
