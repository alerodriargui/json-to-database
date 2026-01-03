import json
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

with open("Reservations.json", "r") as f:
    data = json.load(f)

for r in data:
    cur.execute("""
        INSERT INTO ALL_RESERVATIONS
        (room, checkin, checkout, nombre, country, pax, reservdate)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
    """, (
        r["Room"],
        r["Checkin"],
        r["Checkout"],
        r["Nombre"],
        r["Country"],
        r["Pax"],
        r["ReservDate"]
    ))

conn.commit()
conn.close()

print("Execution time (JSON → ALL):", time.time() - start)
