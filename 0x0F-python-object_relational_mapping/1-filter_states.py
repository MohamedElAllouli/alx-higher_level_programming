#!/usr/bin/python3
"""Lists states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    connex = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = connex.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_r = cur.fetchall()
    for r in query_r:
        if r[1].startswith("N"):
            print(r)
    cur.close()
    connex.close()
