import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", "..", ".env.test"))
except FileNotFoundError:
    pass

DB_FILENAME = os.getenv("DB_FILENAME") or "test_database.db"
SCHEMA_FILENAME = os.getenv("SCHEMA_FILENAME") or "schema.sql"
