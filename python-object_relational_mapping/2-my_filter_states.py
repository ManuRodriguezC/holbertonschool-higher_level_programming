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

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    for elemets in cur:
        if argv[4] == elemets[1]:
            print("({}, '{}')".format(elemets[0], elemets[1]))

    db.close()


if __name__ == "__main__":
    date()
