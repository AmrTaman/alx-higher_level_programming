#!/usr/bin/python3

"""
saddsasdasdasd
"""

import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=args[0],
        passwd=args[1],
        db=args[2]
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY"
                " name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
