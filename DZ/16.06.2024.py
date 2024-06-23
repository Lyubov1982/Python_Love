import sqlite3

dogs_list = [
    ("Пудель", 3, 15000),
    ("Шпиц", 1, 25000),
    ("Доберман", 3, 18000),
    ("Овчарка", 1, 12000),
    ("Бульдог", 4, 8000)
]

with sqlite3.connect("gog.db") as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS dogs(
    dog_id INTEGER PRIMARY KEY AUTOINCREMENT,
    breed TEXT,
    age INTEGER,
    price INTEGER)""")

    cur.executemany("INSERT INTO dogs (breed, age, price) VALUES (?, ?, ?)", dogs_list)

    cur.execute("ALTER TABLE dogs ADD COLUMN new_price INTEGER")

    cur.execute("UPDATE dogs SET new_price = price - 500")

    con.commit()


    # con.close()
