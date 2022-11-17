#!/usr/bin/python3
"""
This module conect to the sql with python,
open the hbtn databases and print all elemts
"""
import MySQLdb
from sys import argv


def date():
    """
    This funtion connect to the basedata
    and print specific elemets
    """
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        password=argv[2],
        database=argv[3],
        port=3306
    )

    cur = db.cursor()

    search = "SELECT id, name FROM states WHERE name = '{}' ORDER BY id ASC".format(argv[4])
    cur.execute(search)
    for elemets in cur:
        print(elemets)

    db.close()


if __name__ == "__main__":
    date()
