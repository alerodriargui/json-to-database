import mysql.connector
import time

start = time.time()

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="hotel"
)
cur = conn.cursor()

cur.callproc("populate_internal")

conn.commit()
cur.close()
conn.close()

print("Internal procedure time:", time.time() - start)
