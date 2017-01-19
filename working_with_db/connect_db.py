import MySQLdb
import sys

DB_HOST ="localhost"
USER_NAME = "root"
USER_PASS = "password"
USER_DB = "coursedb"

con_obj = None

try:
    con_obj = MySQLdb.connect(host=DB_HOST,
                         user=USER_NAME,
                         passwd=USER_PASS,
                         db=USER_DB)
    print con_obj
except:
    print("Unexpected error:", sys.exc_info()[0])

finally:
    if con_obj:
        con_obj.close()


