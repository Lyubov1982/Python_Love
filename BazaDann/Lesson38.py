# 08/06/2024
# import sqlite3

# con = sqlite3.connect("profile.db")
# cur = con.cursor()
#
# cur.execute("""
# """)
#
# con.close()


# with sqlite3.connect("profile.db") as con:
#     cur = con.cursor()
#
#     cur.execute("""CREATE TABLE IF NOT EXISTS users(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     summa REAL,
#     date BLOB)""")

    # cur.execute("DROP TABLE users")


# with sqlite3.connect("users.db") as con:
#     cur = con.cursor()

    # cur.execute("""CREATE TABLE IF NOT EXISTS person(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # phone BLOB NOT NULL DEFAULT "+79090000000",
    # age INTEGER CHECK(age > 0 AND age < 100),
    # email TEXT UNIQUE
    # )""")

# Переименовать таблицу
    # cur.execute("""
    # ALTER TABLE person
    # RENAME TO person_table;
    # """)
# Добавить столбец в таблицу
#     cur.execute("""
#     ALTER TABLE person_table
#     ADD COLUMN address
#     """)
# Добавить столбец в таблицу c обязательным заполнение / ошибка выдается если есть уже значения в таблице
#     cur.execute("""
#     ALTER TABLE person_table
#     ADD COLUMN address NOT NULL DEFAULT "Москва"
#     """)
#
# Удалить столбец
#     cur.execute("""
#     ALTER TABLE person_table
#     DROP COLUMN address
#     """)

# Переименовать столбец
#     cur.execute("""
#     ALTER TABLE person_table
#     RENAME COLUMN address TO home_address
#     """)

# Удаление таблицы
#     cur.execute("""
#     DROP TABLE person_table
#     """)

# with sqlite3.connect("db_3.db") as con:
#     cur = con.cursor()
#
#     cur.execute("""
#     SELECT *
#     FROM
#     T1
#     LIMIT 2, 5
#     """)
#
#     # for i in cur:
#     #     print(i)
#
#     res = cur.fetchone()
#     print(res)
#
#     res2 = cur.fetchmany(2)
#     print(res2)
#
#     res3 = cur.fetchall()
#     print(res3)
