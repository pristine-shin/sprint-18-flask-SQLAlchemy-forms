import sqlite3

DB_FILE = "dev.db"

with sqlite3.connect(DB_FILE) as conn:
    curs = conn.cursor()
    curs.execute(
        '''
            CREATE TABLE appointments(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(200) NOT NULL,
            start_datetime TIMESTAMP NOT NULL,
            end_datetime TIMESTAMP NOT NULL,
            description TEXT NOT NULL,
            private BOOLEAN NOT NULL
            );
        '''
    )
