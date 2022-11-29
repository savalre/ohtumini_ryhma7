"""
Creates a database based on the schema.sql
file in the same directory
"""
from os import path, remove
import sqlite3
from db.get_db_filepath import db_filepath, schema_filepath

def init_db():
    """
    Creates the database
    ALL DATA WILL BE LOST!
    """
    if path.exists(db_filepath):
        remove(db_filepath)

    connection = sqlite3.connect(db_filepath)

    with open(schema_filepath, encoding='utf-8') as schema:
        connection.executescript(schema.read())

if __name__=="__main__":
    init_db()
