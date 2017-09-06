import unittest
from unittest import TestCase
from BookStore.Common.DBConnection import DBConnection


class TestStringMethods(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.db_conn = DBConnection('.', 'testuser', '123@sta.com')
        cls.db_conn.open_db_connection()

    def test_valid_user_exits(self):
        user_flag = self.db_conn.user_exists('admin')
        self.assertTrue(user_flag)

    def test_invalid_user_exists(self):
        user_flag = self.db_conn.user_exists('no_user')
        self.assertFalse(user_flag)

    @classmethod
    def tearDownClass(cls):
        cls.db_conn.close_database_connection()

if __name__ == '__main__':
    unittest.main()
