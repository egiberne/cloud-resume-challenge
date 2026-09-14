# Create the SQLite database file
# This file contains the functions to initialize the database and get a connection to it.
import sqlite3

# Function to get a connection to the SQLite database
def get_connection():
    conn = sqlite3.connect("database/visits.db")
    conn.row_factory = sqlite3.Row
    return conn

# Initialize the database  
def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS visits (
            dbID INTEGER PRIMARY KEY AUTOINCREMENT,
            userId TEXT NOT NULL,
            visitCount INTEGER NOT NULL
        )
    """)

    conn.commit()
    conn.close()