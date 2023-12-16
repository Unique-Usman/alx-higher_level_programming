#!/usr/bin/python3

import sqlite3

# learning sqlite3
conn = sqlite3.connect("customer.db")

# create a cursor
c = conn.cursor()

# create a table

c.execute("""CREATE TABLE customers(
          first_name text, 
          last_name text,
          email text)
          """)

#data types -> NULL INTEGER, REAL, TEXT BLOB

#commit our connection
conn.commit()

conn.close()
