import sqlite3
import time
import math


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = "SELECT * FROM mainmenu"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print("Ошибка чтения из БД")
        return []

    def add_post(self, title, text):
        try:
            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO posts VALUES(NULL, ?, ?, ?)", (title, text, tm))
            self.__db.commit()
            return True
        except sqlite3.Error as e:
            print("Ошибка добавления статьи в базу данных" + str(e))
            return False

    def get_post(self, post_id):
        try:
            self.__cur.execute(f"SELECT title, text FROM posts WHERE id={post_id}")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения статьи из базы данных" + str(e))
        return False, False

    def get_post_annonce(self):
        try:
            self.__cur.execute("SELECT id, title, text FROM posts ORDER BY time DESC")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения статей из базы данных" + str(e))
        return []
