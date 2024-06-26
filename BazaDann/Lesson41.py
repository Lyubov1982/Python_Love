# 16/06/2024

# import sqlite3
#
# with sqlite3.connect("car.db") as con:
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost(
#         name TEXT, tr_in INTEGER, buy INTEGER
#     );
#     """)

# cur.execute("INSERT INTO cars VALUES(NULL, 'Запорожец', 1000)")
# last_row_id = cur.lastrowid
# buy_car_id = 2
# cur.execute("INSERT INTO cost VALUES('Илья', ?, ?)", (last_row_id, buy_car_id))

# cur.execute("SELECT model, price FROM cars")

# rows = cur.fetchone()  # всегда возвращает только первую запись
# print(rows)
# rows1 = cur.fetchmany(5)  # всегда возвращает список из одного значения, если в скобках ничего не указано
# print(rows1)
# # rows2 = cur.fetchall()
# print(rows2)

# for res in cur:
#     # print(res[0], '=>', res[1])
#     print(res['model'], '=>', res['price'])

#
# import sqlite3
#
#
# def read_ave(n):
#     try:
#         with open(f'avatars/{n}.png', 'rb') as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
#
# def write_ava(name, data):
#     try:
#         with open(name, "wb") as f:
#             f.write(data)
#     except IOError as e:
#         print(e)
#
#
# with sqlite3.connect("car.db") as con:
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS users(
#         name TEXT,
#         ava BLOB,
#         score INTEGER
#     )""")
#     # img = read_ave(1)
#     # if img:
#     #     binary = sqlite3.Binary(img)
#     #     cur.execute("INSERT INTO users VALUES('Илья', ?, 1000)", (binary,))
#
#     cur.execute("SELECT ava FROM users")
#     img = cur.fetchone()['ava']
#
#     write_ava("out.png", img)


# import sqlite3

# with sqlite3.connect("car.db") as con:
#     cur = con.cursor()
#
#     with open("sql_dump.sql", "w") as f:
#         for sql in con.iterdump():
#             f.write(sql)

# with sqlite3.connect("car_project.db") as con:  # делаем дубляж базы данных
#     cur = con.cursor()
#
#     with open("sql_dump.sql", "r") as f:
#         sql = f.read()
#         cur.executescript(sql)

# ORM - реляционное сопоставление объектов
# SQLAlchemy ORM

import os

from sqlalchemy import and_, or_, not_, desc, func

from models.database import DATABASE_NAME, Session
import create_database as db_creator

from models.lesson import Lesson, association_table
from models.student import Student
from models.group import Group


if __name__ == "__main__":
    db_is_creator = os.path.exists(DATABASE_NAME)
    if not db_is_creator:
        db_creator.create_database()

    session = Session()
    # print(session.query(Lesson).all())
    # print("*" * 60)
    #
    # # for it in session.query(Lesson):
    # #     print(it)
    # # print("*" * 60)
    # #
    # # for it in session.query(Lesson):
    # #     print(it.lesson_title)
    # # print("*" * 60)
    #
    # print(session.query(Lesson).count())
    # print("*" * 60)
    #
    # print(session.query(Lesson).first())
    # print("*" * 60)
    #
    # for it in session.query(Lesson).filter(Lesson.id >= 3):
    #     print(it.lesson_title)
    # print("*" * 60)
    #
    # for it in session.query(Lesson).filter(and_(Lesson.id >= 3, Lesson.lesson_title.like('Ф%'))):
    #     print(it.lesson_title)
    # print("*" * 60)
    #
    # for it in session.query(Lesson).filter(or_(Lesson.id >= 3, Lesson.lesson_title.like('Ф%'))):
    #     print(it.lesson_title)
    # print("*" * 60)
    #
    # for it in session.query(Lesson).filter(not_(Lesson.id >= 3), not_(Lesson.lesson_title.like('Ф%'))):
    #     print(it.lesson_title)
    # print("*" * 60)
    #
    # print(session.query(Lesson).filter(Lesson.lesson_title is None).all())
    # print("*" * 60)
    #
    # print(session.query(Lesson).filter(Lesson.lesson_title.in_(['Математика', 'Линейная алгебра'])).all())
    # print("*" * 60)
    #
    # print(session.query(Lesson).filter(Lesson.lesson_title.not_in(['Математика', 'Линейная алгебра'])).all())
    # print("*" * 60)  # notin
    #
    # print(session.query(Student).filter(Student.age.between(16, 17)).all())
    # print("*" * 60)
    #
    # print(session.query(Student).filter(not_(Student.age.between(17, 24))).all())
    # print("*" * 60)
    #
    # for it in session.query(Student).filter(Student.age.like("1%")).limit(4).offset(3):
    #     print(it)
    # print("*" * 60)
    #
    # for it in session.query(Student).order_by(Student.surname):
    #     print(it)
    # print("*" * 60)
    #
    # for it in session.query(Student).order_by(desc(Student.surname)):
    #     print(it)
    # print("*" * 60)
    #
    # for it in session.query(Student).join(Group).filter(Group.group_name == "MDA-9"):
    #     print(it)
    # print("*" * 60)
    #
    # for it in session.query(func.count(Student.surname), Group.group_name).join(Group).group_by(Group.group_name):
    #     print(it)
    # print("*" * 60)
    #
    # for it in session.query(func.count(Student.surname), Group.group_name).join(Group).group_by(Group.group_name).having(func.count(Student.surname) < 25):
    #     print(it)
    # print("*" * 60)
    #
    # for it in session.query(Student.age).filter(Student.age < 20).distinct():
    #     print(it)
    # print("*" * 60)

    for it in session.query(Lesson):
        print(it)
    print("*" * 60)

    # i = session.query(Lesson).first()
    # i.lesson_title = "Информатика"
    # session.add(i)
    # session.commit()

    for it in session.query(Lesson):
        print(it)
    print("*" * 60)

    session.add(Lesson(Lesson_title="Математика"))
    session.commit()

    # i = session.query(Lesson).filter(Lesson.lesson_title == "Физика").one()
    # session.delete()
    # session.commit()

    for it in session.query(Lesson):
        print(it)
    print("*" * 60)