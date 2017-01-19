
import MySQLdb
import sys

USER_NAME = "root"
USER_PASS = "password"
USER_DB = "coursedb"


db=MySQLdb.connect(user=USER_NAME,
                   passwd=USER_PASS,
                   db=USER_DB)

cur =db.cursor()

SQL_QUERY = "UPDATE coursedb.courses SET name='%s',duration='%s' WHERE id='%s'"%("nodejs",30,1001);


cur.execute(SQL_QUERY)

print "rows updated", cur.rowcount

db.commit()

