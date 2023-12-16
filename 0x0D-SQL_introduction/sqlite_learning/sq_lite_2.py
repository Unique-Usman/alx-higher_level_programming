import sqlite3 

conn = sqlite3.connect("customer.db")

c = conn.cursor()

c.execute("""
           INSERT INTO customers VALUES('Arib', 'Elder', 'joh@gmail.com')
           """)

conn.commit()
conn.close()
