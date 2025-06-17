import sqlite3

class DataBaseHandler:
    DB_NAME = 'students.db'
    
    @staticmethod
    def _connect():
        return sqlite3.connect(DataBaseHandler.DB_NAME)
    
    @staticmethod
    def create_table():
        with DataBaseHandler._connect() as conn:
            conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER NOT NULL,
                gender TEXT NOT NULL
            )
            """)

    @staticmethod
    def insert_student(name,email,age,gender):
        with DataBaseHandler._connect() as conn:
            conn.execute('INSERT INTO students(name,email,age,gender) VALUES (?,?,?,?)',(name,email,age,gender))

    @staticmethod
    def read_all_students():
        with DataBaseHandler._connect() as conn:
            return conn.execute('SELECT * FROM students').fetchall()

DataBaseHandler.create_table()