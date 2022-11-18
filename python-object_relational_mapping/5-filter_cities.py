#!/usr/bin/python3
"""
This module conect to the sql with python,
open the hbtn databases and print all elemts
"""
import MySQLdb
from sys import argv


def date():
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        password=argv[2],
        database=argv[3],
        port=3306
    )

    cur = db.cursor()

    com = f"SELECT c.name FROM cities c LEFT JOIN states s ON c.state_id \
            = s.id WHERE s.name = '{argv[4]}' ORDER BY c.id ASC"

    cur.execute(com)

    count = 0
    for elemets in cur:
        if count > 0:
            print(", ", end="")
        print(elemets[0], end="")
        count += 1
    print()

    db.close()


if __name__ == '__main__':
    date()
