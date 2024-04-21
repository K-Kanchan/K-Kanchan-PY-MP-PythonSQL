"""
This lab will explore establishing a database connection via Python and SQLite,
as well as creating a table, inserting data, and selecting that data.
"""
import sqlite3


conn = sqlite3.connect(":memory:")
cursor = conn.cursor()


# TODO: Complete create_dogs_table() by creating a table in the database called "dogs".
def create_dogs_table():

    # Create a table called "dogs"
    cursor.execute("CREATE TABLE IF NOT EXISTS dogs (id INTEGER PRIMARY KEY AUTOINCREMENT, "
                   "name TEXT, "
                   "breed TEXT, "
                   "age INTEGER)")


# TODO: Complete insert_dog() by inserting a new dog (provided in the parameters) into the "dogs" table.
def insert_dog(name, breed, age):

    # insert a new dog into the "dogs" table
    cursor.execute("INSERT INTO dogs (name, breed, age) VALUES (?, ?, ?)", (name, breed, age))


# TODO: Complete select_all_dogs() by selecting all rows from the "dogs" table *and returning them*.
def select_all_dogs():

    # select all rows from the "dogs" table
    cursor.execute("SELECT * FROM dogs")

    # fetch all rows
    rows = cursor.fetchall()

    # return the rows
    return rows  # return "TODO: return the rows"
