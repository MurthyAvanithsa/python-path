
import MySQLdb
import sys

USER_NAME = "root"
USER_PASS = "password"
USER_DB = "coursedb"


db = MySQLdb.connect(user=USER_NAME,
                   passwd=USER_PASS,
                   db=USER_DB)

cur = db.cursor()

SQL_QUERY = "DELETE FROM coursedb.courses where id=%s"%(2006)

print cur.execute(SQL_QUERY)

db.commit()

db.close()

