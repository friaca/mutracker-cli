from .database import config_db
import pathlib
import os
import sys

try:
  from dotenv import dotenv_values
  env_dict = dotenv_values('.env')
except ImportError:
  from dotenv import load_dotenv
  __env__ = ['ENV', 'MOCK_DATA', 'DB_PATH']
  load_dotenv('.env')
  env_dict = { item : os.environ.get(item) for item in __env__ }

DB_NAME = 'mutracker.db'

if os.name == 'nt':
  DB_PATH = os.getenv('APPDATA')
  FOLDER_NAME = 'mutracker'
elif os.name == 'posix':
  DB_PATH = os.getenv('HOME')
  FOLDER_NAME = '.mutracker'
else:
  print('Oops, not using Windows nor Unix-based? Sorry...')
  sys.exit(1)

DB_DIR = os.path.join(DB_PATH, FOLDER_NAME)
FULL_DB_PATH = os.path.join(DB_DIR, DB_NAME)

config = { 
  **{ 'DB_PATH': FULL_DB_PATH }, 
  **env_dict
}

if not pathlib.Path(DB_DIR).is_dir():
  pathlib.Path(DB_DIR).mkdir(parents=True)
  config_db(config)
