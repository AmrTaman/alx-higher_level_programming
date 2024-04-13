#!/usr/bin/python3

"""
you turn the lights in then you get them back off
"""

import sys
import MySQLdb


if __name__ == "__main__":
    args = (sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=args[0],
            passwd=args[1],
            db=args[2]
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '{}'"
                " ORDER BY id ASC".format(args[3]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
