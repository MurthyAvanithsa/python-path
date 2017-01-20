
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

# rows = cur.fetchmany(2)
#
# for row in rows:
#     for col in row:
#         print col

res = cur.fetchmany(2)

for row in res:
    print row

db.close()
