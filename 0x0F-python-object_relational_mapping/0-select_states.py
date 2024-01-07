#!/usr/bin/python3
import MySQLdb
from MySQLdb import Error
import sys

"""
Connect to a database hbtn_0e_0_usa and
list all states from the database
"""

if __name__ == "__main__":
    connection = None
    cursor = None
    try:
        connection = MySQLdb.connect(
                host="localhost",
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3]
                )
        cursor = connection.cursor()
        cursor.execute("SELECT * from states")
        results = cursor.fetchall()
        for result in results:
            print(result)
        cursor.close()
        connection.close()
    except Error as err:
        print(f"Error: {err}")
