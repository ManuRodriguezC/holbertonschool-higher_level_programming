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
    and print elemests join cities and state
    """
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        password=argv[2],
        database=argv[3],
        port=3306
    )

    cur = db.cursor()

    com = "SELECT c.id, c.name, s.name FROM cities c LEFT JOIN \
            states s ON c.state_id = s.id ORDER BY c.id ASC"

    cur.execute(com)
    for elemets in cur:
        print(elemets)

    db.close()


if __name__ == '__main__':
    date()
