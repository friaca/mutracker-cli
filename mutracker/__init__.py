from .database import config_db
from dotenv import dotenv_values
import pathlib
import os

ROOT = pathlib.Path(__file__).parent.absolute()
DEV_DB_PATH = os.path.join(os.path.sep, ROOT, 'mutracker.db')

config = { 
  **{ 'DB_PATH': DEV_DB_PATH }, 
  **dotenv_values('.env') 
}

config_db(config)