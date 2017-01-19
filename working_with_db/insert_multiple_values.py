
import MySQLdb
import sys

USER_NAME = "root"
USER_PASS = "password"
USER_DB = "coursedb"

data = list()

data.append(('SCALA', 80, 'Murthy'))
data.append(('AJS', 80, 'Murthy'))

print "dataset", data
#
# for i in range(1020,1030):
#     data.append((i,'Java',40,'murthy'))

db = MySQLdb.connect(user=USER_NAME,
                   passwd=USER_PASS,
                   db=USER_DB)

cur =db.cursor()

SQL_QUERY = "INSERT INTO coursedb.courses (name, duration,tutor) VALUES (%s ,%s, %s)"

cur.executemany(SQL_QUERY,
                data)

db.commit()

db.close()
