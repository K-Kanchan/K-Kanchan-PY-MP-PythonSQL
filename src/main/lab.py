import sqlite3

conn = sqlite3.connect('dogsp.db')
cursor = conn.cursor()


# TODO: Complete create_dogs_table() by creating a table in the database called "dogs".
def create_dogs_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS dogs (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        breed TEXT,
                        age INTEGER
                    )''')
    conn.commit()
  


# TODO: Complete insert_dog() by inserting a new dog (provided in the parameters) into the "dogs" table.
def insert_dog(name, breed, age):
    cursor.execute('''INSERT INTO dogs (name, breed, age) VALUES (?, ?, ?)''', (name, breed, age))
    conn.commit()



# TODO: Complete select_all_dogs() by selecting all rows from the "dogs" table and returning them.
def select_all_dogs():
    # return the rows
    cursor.execute('''SELECT * FROM dogs''')
    return cursor.fetchall()
