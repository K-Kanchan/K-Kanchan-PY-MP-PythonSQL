# PY-MP-PythonSQL

## Background 

A database connection is an integral part of any modern API. Many standard functionalities of modern backend application aren't possible to implement without durable long term data storage. Remember the acronym "CRUD". An API will typically be able to Create, Read, Update, and Delete data. In this mini project, we'll explore how to use python to create a connection to a database, create a database table, and create/read the data in the database. 

The primary technologies you will leverage in this project are Python and SQL. The project will be written in Python, and the database will be SQLite.

## Files

### lab.py
The lab.py file contains variables and functions that must be initialized and implemented to complete the Mini Project.

### app.py
The app.py file serves as the main entry point for the project. It runs the functions in lab.py to test if it has been correctly implemented.

### lab_test.py
The lab_test.py file contains unit tests for your work in lab.py.

## Project Structure
- src/
  - main/
    - app.py
    - lab.py
  - test/
    - lab_test.py

## Database Table

The following table will be initialized in your project's create_dogs_table() function.

### dogs
```
id INTEGER PRIMARY KEY,
name TEXT,
breed TEXT,
age INTEGER
```

# User Stories


### Establish a Connection and a Cursor
- Initialize the conn and cursor variables defined at the top of lab.py.
- conn will hold the connection to the database.
- cursor will hold the cursor object for the connection, allowing you to manipulate the database.

### Implement create_dogs_table
- Use your cursor object to execute a sql statement that creates the dogs table
- Follow the "Database Table" specification above.

### Implement insert_dog
- Use your cursor object to execute a sql statement that creates a new record in the dogs table.
- The values for the insert statement will be provided in the parameters of insert_dog. (name, breed, age). You just have to write the actual statement.

### Implement select_all_dogs
- Use your cursor object to execute a sql statement that selects all record from the dogs table
