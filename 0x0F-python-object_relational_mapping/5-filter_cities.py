#!/usr/bin/python3

"""
This script takes in the name of a state as an argument and lists all cities of that state,
using the database `hbtn_0e_4_usa`.

Usage: ./5-filter_cities.py <mysql username> <mysql password> <database name> <state name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username, password, dbname, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=dbname)
    cursor = db.cursor()
    query = "SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC"
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    cities = [row[0] for row in rows]
    print(", ".join(cities))
    cursor.close()
    db.close()
