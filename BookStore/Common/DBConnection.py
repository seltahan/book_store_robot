import pyodbc as pyodbc
from robot.api import logger
from decimal import Decimal


class DBConnection(object):
    def __init__(self, server_ip, user_name,  password):
        self.connection_string = 'DRIVER={SQL Server};SERVER=' + server_ip + '\SQLE;DATABASE=bookstore;' \
                                                'UID=' + user_name + ';PWD=' + password + ';Integrated Security=False'
        self.connection = pyodbc.Connection
        self.cursor = pyodbc.Cursor

    def open_db_connection(self):
        self.connection = pyodbc.connect(self.connection_string)
        self.cursor = self.connection.cursor()
        return self.cursor

    def user_exists(self, user_name):
        cursor = self.open_db_connection()
        print 'verify user exists in DB'
        sql_statement = "SELECT member_login FROM bookstore.dbo.members where member_login = '{}'".format(user_name)
        cursor.execute(sql_statement)
        user_row = self.cursor.fetchone()
        print 'Row returned from DB is : ' + str(user_row)
        if user_row is None:
            logger.error('User {} is not found in DB'.format(user_name))
            return False
        elif user_row[0].lower() == user_name.lower():
            return True

    def user_email_exists(self, user_name):
        cursor = self.open_db_connection()
        print 'verify user email exists in DB'
        sql_statement = "SELECT email FROM bookstore.dbo.members where member_login = '{}'".format(user_name)
        cursor.execute(sql_statement)
        user_row = self.cursor.fetchone()
        print 'Row returned from DB is : ' + str(user_row)
        if user_row is None:
            return False
        elif user_row[0].lower() == user_name.lower():
            return True


    def book_exists(self, book_name):
        cursor = self.open_db_connection()
        print 'verify book exists in DB'
        sql_statement = "SELECT name FROM bookstore.dbo.items where name = '{}'".format(book_name)
        cursor.execute(sql_statement)
        user_row = self.cursor.fetchone()
        print 'Row returned from DB is : ' + str(user_row)
        if user_row is None:
            logger.error('User {} is not found in DB'.format(book_name))
            return False
        elif user_row[0].lower() == book_name.lower():
            return True

    def price_exists (self, price):
        cursor = self.open_db_connection()
        print 'verify book price exists in DB'
        sql_statement = "SELECT price FROM bookstore.dbo.items where price = '{}'".format(price)
        cursor.execute(sql_statement)
        user_row = self.cursor.fetchone()
        #print 'Row returned from DB is : ' + str(user_row)
        if user_row is None:
            return False
        elif user_row[0] == Decimal(price):
            return True

    def close_database_connection(self):
        self.cursor.close()
        del self.cursor
        self.connection.close()

# cls = DBConnection('.', 'testuser', '123@sta.com')
# cls.open_db_connection()
# cls.price_exists('100')
