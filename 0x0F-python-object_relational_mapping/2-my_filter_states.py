#!/usr/bin/python3

"""
you turn the lights in then you get them back off
"""

import sys
import MySQLdb


if __name__ == "__main__":
    username, password, database, state_name = sys.argv[1:]
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '{}'"
                " ORDER BY id ASC".format(state_name))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
