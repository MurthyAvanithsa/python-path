
import MySQLdb
import sys

USER_NAME = "root"
USER_PASS = "password"
USER_DB = "coursedb"



SQL_QUERY = "UPDATEs coursedb.courses SET name='%s',duration='%s' WHERE id='%s'"%("METIOR",30,1);

db = None


try:
    db = MySQLdb.connect(user=USER_NAME,
                         passwd=USER_PASS,
                         db=USER_DB)

    cur = db.cursor()
    print "Executing SQL", SQL_QUERY
    cur.execute(SQL_QUERY)
    cur.commit()
    print "rows updated", cur.rowcount

except(MySQLdb.ProgrammingError):
    print "Sql Exception"

except(MySQLdb.OperationalError):
    print "Please check username,password"

finally:
    if db:
        db.close()





