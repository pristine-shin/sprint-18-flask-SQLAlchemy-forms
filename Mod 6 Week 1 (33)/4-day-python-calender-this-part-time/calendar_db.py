import sqlite3
import datetime

DB_FILE = "dev.db"

# with sqlite3.connect(DB_FILE) as conn:
#     curs = conn.cursor()
#     curs.execute(
#         '''
#             CREATE TABLE appointments(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name VARCHAR(200) NOT NULL,
#             start_datetime TIMESTAMP NOT NULL,
#             end_datetime TIMESTAMP NOT NULL,
#             description TEXT NOT NULL,
#             private BOOLEAN NOT NULL
#             );
#         '''
#     )


# with sqlite3.connect(DB_FILE) as conn:
#     curs = conn.cursor()
#     curs.execute(
#         '''
#         INSERT INTO appointments(name, start_datetime, end_datetime, description, private)
#         VALUES('My appointment', '2024-10-04 14:00:00', '2024-10-04 15:00:00','An appointment for me', false);
#         '''
#     )


def get_all_appointments():
    with sqlite3.connect(DB_FILE) as conn:
        curs = conn.cursor()
        curs.execute(
            '''
            SELECT * FROM appointments;
            '''
        )
        results = curs.fetchall()
        print(results)

get_all_appointments()
