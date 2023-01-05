import sqlite3
from sqlite3 import Error as SqLiteError

import mysql.connector
from mysql.connector import Error as MySqlError

import psycopg2
from psycopg2 import Error as PostGreSqlError


"""
Install This Libraries
pip install sqlite3, mysql, mysql-connector, mysql-connector-python==8.0.29, psycopg2
"""


class SqLite:
    def __init__(self, db_path: str):
        self.connection = None
        self.db_path = db_path

    def connect(self):
        try:
            if self.db_path[-3:] != '.db':
                # print(f"\033[35m(SqLite)\033[31m The error 'DB not found' occurred\033[0m")
                return

            self.connection = sqlite3.connect(self.db_path)
            # print("\033[35m(SqLite)\033[36m Connection to DB successful\033[0m")
        except SqLiteError as e:
            pass
            # print(f"\033[35m(SqLite)\033[31m The error '{e}' occurred\033[0m")

    def executeQuery(self, query: str, reconnect: bool = True, close_connection: bool = True):
        if reconnect:
            self.connect()

        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            # print("\033[35m(SqLite)\033[36m Database updated successfully\033[0m")
            if close_connection:
                cursor.close()
                self.connection.commit()
                self.connection.close()
        except SqLiteError as e:
            # print(f"\033[35m(SqLite)\033[31m The error '{e}' occurred\033[0m")
            self.connection.close()

    def readQuery(self, query: str, reconnect: bool = True, close_connection: bool = True):
        if reconnect:
            self.connect()

        try:
            cursor = self.connection.cursor()
            # print("\033[35m(SqLite)\033[36m Database read successfully\033[0m")
            cursor.execute(query)
            result = cursor.fetchall()
            if close_connection:
                cursor.close()
                self.connection.close()
            return result
        except SqLiteError as e:
            # print(f"\033[35m(SqLite)\033[31m The error '{e}' occurred\033[0m")
            self.connection.close()


class MySql:
    def __init__(self, db_name: str, user: str, password: str, host: str):
        self.connection = None
        self.connection_info = {'db_name': db_name, 'user': user, 'password': password, 'host': host}

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.connection_info['host'],
                user=self.connection_info['user'],
                password=self.connection_info['password'],
                database=self.connection_info['db_name'])
            # print("\033[35m(MySql)\033[36m Connection to DB successful\033[0m")
        except MySqlError as e:
            pass
            print(f"\033[35m(MySql)\033[31m The error '{e}' occurred\033[0m")

    def executeQuery(self, query: str, reconnect: bool = True, close_connection: bool = True):  #для записи в бд
        if reconnect:
            self.connect()
        cursor = self.connection.cursor()

        try:
            cursor.execute(query)
            # print("\033[35m(MySql)\033[36m Database updated successfully\033[0m")
            if close_connection:
                cursor.close()
                self.connection.commit()
                self.connection.close()
        except MySqlError as e:
            print(f"\033[35m(MySql)\033[31m The error '{e}' occurred\033[0m")
            cursor.close()
            self.connection.close()

    def readQuery(self, query: str, reconnect: bool = True, close_connection: bool = True):
        if reconnect:
            self.connect()
        cursor = self.connection.cursor()

        try:
            cursor.execute(query)
            result = cursor.fetchall()
            # print("\033[35m(MySql)\033[36m Database read successfully\033[0m")
            if close_connection:
                cursor.close()
                self.connection.close()
            return result
        except MySqlError as e:
            print(f"\033[35m(MySql)\033[31m The error '{e}' occurred\033[0m")
            cursor.close()
            self.connection.close()


class PostGreSql:
    def __init__(self, db_name: str, user: str, password: str, host: str):
        self.connection = None
        self.connection_info = {'db_name': db_name, 'user': user, 'password': password, 'host': host}

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.connection_info['db_name'],
                user=self.connection_info['user'],
                password=self.connection_info['password'],
                host=self.connection_info['host'])
            print("\033[35m(PostGreSql)\033[36m Connection to DB successful\033[0m")
        except PostGreSqlError as e:
            print(f"\033[35m(PostGreSql)\033[31m The error '{e}' occurred\033[0m")

    def executeQuery(self, query: str, reconnect: bool = True, close_connection: bool = True):
        if reconnect:
            self.connect()
        cursor = self.connection.cursor()

        try:
            cursor.execute(query)
            print("\033[35m(PostGreSql)\033[36m Database updated successfully\033[0m")
            if close_connection:
                cursor.close()
                self.connection.commit()
                self.connection.close()
        except PostGreSqlError as e:
            print(f"\033[35m(PostGreSql)\033[31m The error '{e}' occurred\033[0m")
            cursor.close()
            self.connection.close()

    def readQuery(self, query: str, reconnect: bool = True, close_connection: bool = True):
        if reconnect:
            self.connect()
        cursor = self.connection.cursor()

        try:
            cursor.execute(query)
            result = cursor.fetchall()
            print("\033[35m(PostGreSql)\033[36m Database read successfully\033[0m")
            if close_connection:
                cursor.close()
                self.connection.close()
            return result
        except PostGreSqlError as e:
            print(f"\033[35m(PostGreSql)\033[31m The error '{e}' occurred\033[0m")
            cursor.close()
            self.connection.close()
