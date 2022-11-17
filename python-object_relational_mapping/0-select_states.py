#!/usr/bin/python3
"""
This module conect to the sql with python,
open the hbtn databases and print all elemts
"""


import MySQLdb

def date():   
    db = MySQLdb.connect(
        user='root',
        password='majo0308',
        database='hbtn_0e_0_usa'
    )

    cur = db.cursor()

    cur.execute("USE hbtn_0e_0_usa")
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    for elemets in cur:
        print(elemets)
        
if __name__ == "__main__":
    date()