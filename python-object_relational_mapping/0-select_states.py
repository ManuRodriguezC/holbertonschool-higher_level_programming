#!/usr/bin/python3
"""
This module conect to the sql with python,
open the hbtn databases and print all elemts
"""


import MySQLdb


db = MySQLdb.connect(
    user='root',
    password='majo0308',
    database='hbtn_0e_0_usa'
)
# asasas
cur = db.cursor()
#asas
cur.execute("SELECT * FROM states")
#asas
for elemets in cur:
    print(elemets)
