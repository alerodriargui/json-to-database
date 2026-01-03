import mysql.connector
from time import time

# --- Conexión MySQL ---
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",  
    database="hotel"
)
cursor = conn.cursor()

# --- Crear tablas nuevas ---
tables_sql = [
    "CREATE TABLE IF NOT EXISTS COUNTRY2 LIKE COUNTRY",
    "CREATE TABLE IF NOT EXISTS CLIENT2 LIKE CLIENT",
    "CREATE TABLE IF NOT EXISTS ROOM2 LIKE ROOM",
    "CREATE TABLE IF NOT EXISTS RESERVATION2 LIKE RESERVATION"
]

for stmt in tables_sql:
    cursor.execute(stmt)

conn.commit()

# --- Eliminar procedimiento si existe ---
cursor.execute("DROP PROCEDURE IF EXISTS populate_internal")
conn.commit()

# --- Crear procedimiento ---
proc_sql = """
CREATE PROCEDURE populate_internal()
BEGIN
    -- Insertar países
    INSERT IGNORE INTO COUNTRY2(country_code, country_name)
    SELECT DISTINCT Country, Country FROM ALL_RESERVATIONS;

    -- Insertar clientes
    INSERT INTO CLIENT2(name, country_code)
    SELECT DISTINCT Nombre, Country FROM ALL_RESERVATIONS;

    -- Insertar habitaciones
    INSERT IGNORE INTO ROOM2(room_number, price)
    SELECT DISTINCT Room, RAND()*100+50 FROM ALL_RESERVATIONS;

    -- Insertar reservas
    INSERT INTO RESERVATION2(room_number, client_id, checkin, checkout, reserv_date, pax)
    SELECT A.Room, C.client_id, A.Checkin, A.Checkout, A.ReservDate, A.Pax
    FROM ALL_RESERVATIONS A
    JOIN CLIENT2 C ON C.name = A.Nombre;
END
"""

# Ejecutar la creación del procedimiento
cursor.execute(proc_sql)
conn.commit()

# --- Ejecutar procedimiento y medir tiempo ---
start_time = time()
cursor.callproc("populate_internal")
conn.commit()
end_time = time()

print(f"Execution time (Internal populate): {end_time - start_time:.4f} seconds")

cursor.close()
conn.close()
