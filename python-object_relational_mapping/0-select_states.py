#!/usr/bin/python3
import MySQLdb


db = MySQLdb.connect(
    user='root',
    password='majo0308',
    database='hbtn_0e_0_usa',
)

cur = db.cursor()

cur.execute("SHOW DATABASES")
cur.execute("USE hbtn_0e_0_usa")
cur.execute("SELECT * FROM states")

for elemets in cur:
    print(elemets)