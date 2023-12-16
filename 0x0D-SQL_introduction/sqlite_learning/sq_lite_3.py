import sqlite3

conn = sqlite3.connect("customer.db")

c = conn.cursor()

many_customer = [
        ("Was", "Brown", "wesbrown.com"),
        ("Steph", "Kuewa", "steph.com"),
        ("Dan", "Pas", "dean.com"),
        ]
c.executemany("INSERT INTO customers VALUES (?, ?, ? )", many_customer)

conn.commit()
conn.close()
