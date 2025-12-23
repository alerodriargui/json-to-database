import mysql.connector
import random
import time

start = time.time()

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="hotel"
)
cur = conn.cursor()

# Countries
cur.execute("""
INSERT IGNORE INTO COUNTRY(country_code, country_name)
SELECT DISTINCT country, country FROM ALL_RESERVATIONS
""")

# Clients
cur.execute("""
INSERT INTO CLIENT(name, country_code)
SELECT DISTINCT nombre, country FROM ALL_RESERVATIONS
""")

# Rooms
cur.execute("""
INSERT IGNORE INTO ROOM(room_number, price)
SELECT DISTINCT room, ROUND(RAND()*100+50,2)
FROM ALL_RESERVATIONS
""")

# Reservations
cur.execute("""
INSERT INTO RESERVATION(room_number, client_id, checkin, checkout, reserv_date, pax)
SELECT A.room, C.client_id, A.checkin, A.checkout, A.reservdate, A.pax
FROM ALL_RESERVATIONS A
JOIN CLIENT C ON C.name = A.nombre
""")

conn.commit()
conn.close()

print("Execution time (External populate):", time.time() - start)
