import mysql.connector
import json
import time

start = time.time()

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="hotel"
)
cur = conn.cursor()

cur.execute("""
SELECT room, checkin, checkout FROM ALL_RESERVATIONS
""")

room_data = {}

for room, ci, co in cur.fetchall():
    room_data.setdefault(room, []).append({
        "checkin": str(ci),
        "checkout": str(co)
    })

for room, reservations in room_data.items():
    cur.execute("""
        UPDATE ROOM
        SET reservations_json = %s
        WHERE room_number = %s
    """, (json.dumps(reservations), room))

conn.commit()
conn.close()

print("Execution time (ROOM JSON external):", time.time() - start)
