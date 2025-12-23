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
