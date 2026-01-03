import mysql.connector
import sys

def run_sql_file(filename):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",  
        autocommit=True
    )
    cur = conn.cursor()

    with open(filename, "r", encoding="utf-8") as f:
        sql = f.read()

    for stmt in sql.split(";"):
        stmt = stmt.strip()
        if stmt:
            cur.execute(stmt)

    cur.close()
    conn.close()

if __name__ == "__main__":
    run_sql_file(sys.argv[1])
    print(f"{sys.argv[1]} executed successfully.")
