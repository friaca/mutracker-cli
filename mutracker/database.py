import sqlite3
import sys
import pathlib

# https://stackoverflow.com/a/38078544/9426143
class Database:
  def __init__(self, name):
    self._conn = sqlite3.connect(name)
    self._cursor = self._conn.cursor()

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    self.close()

  @property
  def connection(self):
    return self._conn

  @property
  def cursor(self):
    return self._cursor

  def commit(self):
    self.connection.commit()

  def close(self, commit=True):
    if commit:
        self.commit()
    self.connection.close()

  def execute(self, sql, params=None):
    self.cursor.execute(sql, params or ())

  def fetchall(self):
    return self.cursor.fetchall()

  def fetchone(self):
    return self.cursor.fetchone()

  def query(self, sql, params=None):
    self.cursor.execute(sql, params or ())
    return self.fetchall()

def run_migrations(db_path: str):
  db = Database(db_path)

  # Releases table
  db.execute("""CREATE TABLE IF NOT EXISTS release (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    artist TEXT NOT NULL,
    dt_release TEXT,
    type INTEGER NOT NULL,
    status_listened INTEGER NOT NULL DEFAULT 0, 
    dt_listened TEXT,
    notes TEXT,
    dt_create TEXT DEFAULT (DATE('now','localtime'))
  )""")

  # Release's type table
  db.execute("""CREATE TABLE IF NOT EXISTS type (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
  )""")
  
  # Release's type rows
  db.execute("INSERT INTO type (name) VALUES ('Album'), ('EP')")

  # Genres table
  db.execute("""CREATE TABLE IF NOT EXISTS genre (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    id_release INTEGER NOT NULL
  )""")

  db.commit()
  db.close()

def insert_mock_data(db_path: str):
  db = Database(db_path)

  db.execute("""INSERT INTO release (name, dt_release, artist, type, status_listened, dt_listened) 
    VALUES ('We Will Always Love You', '2020-12-11', 'The Avalanches', 1, 0, NULL),
    ('The Piper at the Gates of Dawn', '1967-05-21', 'Pink Floyd', 1, 0, NULL),
    ('무너지기 (Crumbling)', '2018-07-31', '공중도둑 [Mid-Air Thief]', 1, 1, NULL)
  """)

  db.execute("""INSERT INTO genre (name, id_release) 
    VALUES ('Electronic', 1),
    ('Neo-Psychedelia', 1),
    ('Psychedelic Rock', 2),
    ('Psychedelic Pop', 2),
    ('Neo-Psychedelia', 3),
    ('Folktronica', 3),
    ('Psychedelic Pop', 3)
  """)

  db.commit()
  db.close()
  
def config_db(config):
  try:
    print('Running migrations...')
    run_migrations(config['DB_PATH'])

    if config['ENV'] == 'development' and config['MOCK_DATA'] == 'yes':
      print('Inserting mocked data on the database...')
      insert_mock_data(config['DB_PATH'])
      print('Mocked data insertion complete.')

    print('Initial migrations complete, the database is ready.')
  except Exception as e:
    print("Couldn't open database!\n[ERROR] ", e)
    sys.exit(1)