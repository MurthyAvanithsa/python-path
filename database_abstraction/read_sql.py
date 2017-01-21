from sqlalchemy import create_engine

#engine = create_engine("postgresql+psycopg2://murthyavanithsa@/murthyavanithsa")

engine = create_engine("mysql://root:password@localhost/coursedb", pool_recycle=3600)


# no need of change
connection = engine.connect()

result = connection.execute("select * from courses")

for row in result:
    print row

connection.close()