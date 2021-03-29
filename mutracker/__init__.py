import sys
import pathlib
import os
from .db.migrations import run_migrations
from dotenv import dotenv_values
dotenv_values()

curr_path = pathlib.Path(__file__).parent.absolute()
db_path = os.path.join(os.path.sep, curr_path, 'db', 'mutracker.db')

config = {
  **({
    'DB_PATH': db_path
  }),
  **dotenv_values('.env'),
}


if not pathlib.Path(config['DB_PATH']).is_file():
  try:
    print('Running migrations...')
    run_migrations(config['DB_PATH'])
    print('Initial migrations complete, the database is ready.')
  except Exception as e:
    print("Couldn't open database!", e)
    sys.exit(1)