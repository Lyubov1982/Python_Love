# 15/06/2024

# import sqlite3

# cars_list = [
#     ("Toyta", 42000),
#     ("Daewoo", 12000),
#     ("Citroen", 42000),
#     ("Honda", 42000),
#     ("Lada", 8000)
# ]
#
# with sqlite3.connect("car.db") as con:  # выполняет запрос только один раз
#     cur = con.cursor()
#
#     cur.execute("""CREATE TABLE IF NOT EXISTS cars(
#     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     model TEXT,
#     price INTEGER)""")
#
#     cur.executescript("""
#     DELETE FROM cars WHERE model LIKE 'D%';
#     UPDATE cars SET price = price + 100;
#     """)

    # cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars_list)  # делает набор однотипных запросов

    # for car in cars_list:
    #     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)

    # cur.execute("INSERT INTO cars VALUES(1, 'BMV', 52000)")
    # cur.execute("INSERT INTO cars VALUES(2, 'Audi', 53000)")
    # cur.execute("INSERT INTO cars VALUES(3, 'Opel', 12000)")
    # cur.execute("INSERT INTO cars VALUES(4, 'Volvo', 14000)")
    # cur.execute("INSERT INTO cars VALUES(5, 'Mercedes', 54000)")

# con.commit() сохранение
# con.close()  закрытие

# import sqlite3
# con = None
# try:
#     con = sqlite3.connect("car.db")
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     BEGIN;
#     INSERT INTO cars VALUES(NULL, 'Reno', 32000);
#     UPDATE cars SET price = price + 100;
#     """)
#     con.commit()
# except sqlite3.Error as e:
#     if con:
#         con.rollback()
#     print("Ошибка выполнения запроса")
# finally:
#     if con:
#         con.close()
