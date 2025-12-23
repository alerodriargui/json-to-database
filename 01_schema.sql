CREATE DATABASE IF NOT EXISTS hotel;
USE hotel;

DROP TABLE IF EXISTS RESERVATION, CLIENT, ROOM, COUNTRY, ALL_RESERVATIONS;
DROP TABLE IF EXISTS RESERVATION2, CLIENT2, ROOM2, COUNTRY2;

CREATE TABLE COUNTRY (
    country_code CHAR(2) PRIMARY KEY,
    country_name VARCHAR(100)
);

CREATE TABLE CLIENT (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    country_code CHAR(2),
    FOREIGN KEY (country_code) REFERENCES COUNTRY(country_code)
);

CREATE TABLE ROOM (
    room_number INT PRIMARY KEY,
    price DECIMAL(6,2),
    reservations_json TEXT
);

CREATE TABLE RESERVATION (
    reservation_id INT AUTO_INCREMENT PRIMARY KEY,
    room_number INT,
    client_id INT,
    checkin DATE,
    checkout DATE,
    reserv_date DATE,
    pax INT,
    FOREIGN KEY (room_number) REFERENCES ROOM(room_number),
    FOREIGN KEY (client_id) REFERENCES CLIENT(client_id)
);

CREATE TABLE ALL_RESERVATIONS (
    room INT,
    checkin DATE,
    checkout DATE,
    nombre VARCHAR(100),
    country CHAR(2),
    pax INT,
    reservdate DATE
);
