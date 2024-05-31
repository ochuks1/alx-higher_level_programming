#!/usr/bin/python3

"""
Script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument (safe from SQL injection)
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username, password, dbname, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=dbname)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
