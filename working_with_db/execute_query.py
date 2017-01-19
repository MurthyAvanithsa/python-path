
import MySQLdb
import sys

USER_NAME = "root"
USER_PASS = "password"
USER_DB = "coursedb"


db = MySQLdb.connect(user=USER_NAME,
                   passwd=USER_PASS,
                   db=USER_DB)

cur = db.cursor()

SQL_QUERY = "SELECT * FROM coursedb.courses"

cur.execute(SQL_QUERY)

row = cur.fetchone()

for col in row:
    print col