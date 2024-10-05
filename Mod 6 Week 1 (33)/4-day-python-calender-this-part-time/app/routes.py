from flask import Blueprint, render_template
import os
import sqlite3
import datetime


DB_FILE = os.environ.get("DB_FILE")

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def main():
    with sqlite3.connect(DB_FILE) as conn:
        curs = conn.cursor()
        curs.execute(
            '''
            SELECT id, name, start_datetime, end_datetime
            FROM appointments
            ORDER BY start_datetime;
            '''
        )
        rows = curs.fetchall()
        starttime_str = '2024-10-04 14:00:00'
        starttime_obj = datetime.datetime.strptime(starttime_str, '%Y-%m-%d %H:%M:%S')
        endtime_str = '2024-10-04 15:00:00'
        endtime_obj = datetime.datetime.strptime(endtime_str, '%Y-%m-%d %H:%M:%S')
    return render_template('main.html', rows=rows, start=starttime_obj, end=endtime_obj)
