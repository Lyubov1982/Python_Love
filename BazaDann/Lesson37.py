# 02/06/2024 База данных LESSON 37

import sqlite3


# con = sqlite3.connect("profile.db")
# cur = con.cursor()
#
# cur.execute("""
# """)
#
# con.close()


with sqlite3.connect("profile.db") as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    summa REAL,
    date BLOB)""")

    # cur.execute("DROP TABLE users")
