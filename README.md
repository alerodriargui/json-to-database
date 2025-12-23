# Exercise 5 – Storage and Data Recovery  
Master’s Degree in Intelligent Systems

## 1. Description

This project implements the complete solution for **Exercise 5** of the subject *Storage and Data Recovery*.  
The objective is to process a JSON file containing hotel reservation data and evaluate different storage and processing strategies.

The work compares:
- External programs vs internal DBMS procedures
- Normalized relational schemas vs JSON attributes inside tables
- JOIN-based queries vs JOIN-free approaches
- MapReduce for scalable computation

The final delivery includes source code, database export, and a presentation.

---

## 2. Technologies Used

- **Python 3**
- **MySQL / MariaDB**
- **SQL (Stored Procedures)**
- **JSON**

Python dependency:
- `mysql-connector-python`

---

## 3. Project Structure

```
Exercise5/
│
├── reservations.json
│
├── 01_schema.sql
├── 02_load_json.py
├── 03_external_populate.py
├── 04_internal.sql
│
├── 05_split_json.py
├── 06_map_reduce.py
│
├── 07_room_json_external.py
├── 08_room2_json_internal.sql
│
├── occupancy.json
├── part_0.json ... part_9.json
│
└── README.md
```

---

## 4. Database Schema

Tables included:

- `ALL_RESERVATIONS` – Raw data mirroring the JSON structure
- `ROOM`, `CLIENT`, `COUNTRY`, `RESERVATION` – Normalized schema
- `ROOM2`, `CLIENT2`, `COUNTRY2`, `RESERVATION2` – Internally populated schema

Foreign keys are used to ensure referential integrity.

---

## 5. Execution Instructions

### 5.1 Create Database and Tables

Run in MySQL:

```sql
SOURCE 01_schema.sql;
```

---

### 5.2 Load JSON into ALL table (External Program)

```bash
python 02_load_json.py
```

---

### 5.3 External Population of Normalized Tables

```bash
python 03_external_populate.py
```

---

### 5.4 Internal Population Using Stored Procedure

```sql
SOURCE 04_internal.sql;
CALL populate_internal();
```

---

## 6. MapReduce Room Occupancy Calculation

```bash
python 05_split_json.py
python 06_map_reduce.py
```

---

## 7. Avoiding JOINs Using JSON Attributes

```bash
python 07_room_json_external.py
```

```sql
SOURCE 08_room2_json_internal.sql;
```

---

## 8. Discussion Summary

- External programs provide flexibility and easier JSON handling.
- Internal procedures are faster due to reduced data transfer.
- MapReduce enables scalable processing of large datasets.
- JSON attributes avoid JOINs but break normalization.

---

## 9. Deliverables

- Python source code
- SQL scripts
- Exported database
- `occupancy.json`
- PPT presentation (10–15 slides)
