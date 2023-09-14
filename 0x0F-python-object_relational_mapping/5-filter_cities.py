#!/usr/bin/python3
""" script that takes in the name of a state as an argument and lists all 
cities of that state, using the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3],
            host='localhost',
            port=3306
            )
    cur = db.cursor()
    query = ("SELECT cities.name FROM cities WHERE cities.state_id = "
            "(SELECT states.id FROM states WHERE name=%s) ORDER BY cities.id ASC")
    cur.execute(query, (sys.argv[4],))
    rows = cur.fetchall()
    li = []
    for row in rows:
        li.append(row[0])
    print(", ".join(li))
    cur.close()
    db.close()
