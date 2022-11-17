#!/usr/bin/python3
"""
This module conect to the sql with python,
open the hbtn databases and print all elemts
"""
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user="root",
        password="majo0308",
        database="hbtn_0e_0_usa",
        port=3306
    )

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    for elemets in cur:
        print(elemets)
