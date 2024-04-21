import sqlite3
import unittest
from src.main import lab


class TestLab(unittest.TestCase):

    def test_connect_to_database(self):

        # Assert that the connection was successful
        self.assertTrue(isinstance(lab.conn, sqlite3.Connection), "conn is not of type sqlite3.Connection.")

    def test_create_dogs_table(self):

        lab.create_dogs_table()

        # select all tables in the database (should only be one, called dogs)
        tables = lab.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()

        # Assert that the dogs table exists and is named correctly
        self.assertEqual(tables[0], ('dogs',), "Failed to create dogs table.")

    def test_insert_and_select_dog(self):

        lab.insert_dog("Mister", "Foxhound", 5)

        # assert that there is a row in the dogs table
        lab.cursor.execute("SELECT * FROM dogs")
        row = lab.cursor.fetchone()
        self.assertIsNotNone(row, "No rows found in the dogs table.")

        # select all rows from the "dogs" table
        rows = lab.cursor.execute("SELECT * FROM dogs").fetchall()

        # assert that the dog was inserted correctly
        self.assertIn(("Mister", "Foxhound", 5), rows, "Failed to insert dog correctly.")


if __name__ == "__main__":
    unittest.main()
