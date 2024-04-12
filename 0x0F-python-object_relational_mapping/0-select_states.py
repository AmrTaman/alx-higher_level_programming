#!/usr/bin/python3

"""
this module executes sql through mysqldb class
"""

import MySQLdb
import sys


args = (sys.argv[1], sys.argv[2], sys.argv[3])
db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=args[0],
        passwd=args[1],
        db=args[2]
)
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
db.close()
