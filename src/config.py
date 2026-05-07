import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)
path_to_dotenv=os.path.join(dirname, "..", ".env")
load_dotenv(path_to_dotenv)

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME", "database.sqlite")
DATABASE_FILE_PATH = os.path.join(dirname, "..", "data", DATABASE_FILENAME)
