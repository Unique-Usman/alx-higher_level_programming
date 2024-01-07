#!/usr/bin/python3
import MySQLdb
from MySQLdb import Error
import sys

"""
Connect to a database hbtn_0e_0_usa and
list all cities from the database based on
the arguments(state)
"""

if __name__ == "__main__":
    connection = None
    cursor = None
    try:
        connection = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3]
                )
        cursor = connection.cursor()
        cursor.execute("""
                       SELECT distinct(name)
                       FROM cities
                       WHERE state_id IN
                       (SELECT id FROM states WHERE name = %s);
                       """, (sys.argv[4],))
        results = cursor.fetchall()
        out = []
        for result in results:
            out.append(result[0])

        for i, v in enumerate(out):
            if i != len(out) - 1:
                print(v, end=", ")
            else:
                print(v)
        cursor.close()
        connection.close()
    except Error as err:
        print(f"Error: {err}")
