from .database import config_db, insert_mock_data, run_migrations
from dotenv import dotenv_values
import pathlib
import os

DB_NAME = 'mutracker.db'

if os.name == 'nt':
  DB_PATH = os.getenv('APPDATA')
  FOLDER_NAME = 'mutracker'
elif os.name == 'posix':
  DB_PATH = os.getenv('HOME')
  FOLDER_NAME = '.mutracker'

DB_DIR = os.path.join(DB_PATH, FOLDER_NAME)
FULL_DB_PATH = os.path.join(DB_DIR, DB_NAME)

config = { 
  **{ 'DB_PATH': FULL_DB_PATH }, 
  **dotenv_values('.env') 
}

if not pathlib.Path(DB_DIR).is_dir():
  pathlib.Path(DB_DIR).mkdir(parents=True)
  config_db(config)