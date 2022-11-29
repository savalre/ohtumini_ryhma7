"""
Form the correct filepath for the DB and schema files
"""
import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", "..", ".env"))
except FileNotFoundError:
    pass

DB_FILENAME = os.getenv("DB_FILENAME") or "database.db"
SCHEMA_FILENAME = os.getenv("SCHEMA_FILENAME") or "schema.sql"

db_filepath = os.path.join(dirname, DB_FILENAME)
schema_filepath = os.path.join(dirname, SCHEMA_FILENAME)
