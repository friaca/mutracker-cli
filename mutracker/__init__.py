import pathlib
import os
from .db.migrations import run_migrations

curr_path = pathlib.Path(__file__).parent.absolute()
db_path = os.path.join(os.path.sep, curr_path, 'db', 'mutracker.db')

if not pathlib.Path(db_path).is_file():
  print('Running migrations...')
  run_migrations(db_path)
  print('Initial migrations complete, the database is ready.')