"""
Creates a database based on the schema.sql
file in the same directory
"""
import sqlite3


connection = sqlite3.connect('database.db')

with open('schema.sql', encoding='utf-8') as schema:
    connection.executescript(schema.read())
