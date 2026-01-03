USE hotel;
DROP TABLE IF EXISTS ROOM2;

CREATE TABLE ROOM2 (
    room_number INT PRIMARY KEY,
    price DECIMAL(6,2),
    reservations_json JSON
);

UPDATE ROOM2 R
SET reservations_json = (
    SELECT JSON_ARRAYAGG(
        JSON_OBJECT(
            'checkin', A.checkin,
            'checkout', A.checkout
        )
    )
    FROM ALL_RESERVATIONS A
    WHERE A.room = R.room_number
);
