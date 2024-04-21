# app.py
import sqlite3

import lab


def main():

    # If conn is type of Database Connection...
    if isinstance(lab.conn, sqlite3.Connection):
        lab.create_dogs_table()
        lab.insert_dog("Scooby", "Great Dane", 4)
        print(lab.select_all_dogs())
    else:
        print("Failed to create database connection.")


if __name__ == "__main__":
    main()
