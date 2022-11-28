"""
Creates a database based on the schema.sql
file in the same directory
"""
from os import path, remove
import sqlite3

basedir = path.abspath(path.dirname(__file__))
file_path = path.join(basedir, 'schema.sql')

if path.exists('database.db'):
  remove('database.db')

connection = sqlite3.connect('database.db')

with open(file_path, encoding='utf-8') as schema:
    connection.executescript(schema.read())
