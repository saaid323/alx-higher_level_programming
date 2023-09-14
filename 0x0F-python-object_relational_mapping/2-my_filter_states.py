#!/usr/bin/python3
"""script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3], host='localhost', port=3306)
    cur = db.cursor()
    cur.execute(f"SELECT * FROM states WHERE name={sys.argv[4]} ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
