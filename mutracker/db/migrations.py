import sqlite3

def run_migrations(db_path: str):
  con = sqlite3.connect(db_path)
  cur = con.cursor()

  # Releases table
  cur.execute("""CREATE TABLE IF NOT EXISTS release (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    artist TEXT NOT NULL,
    dt_release TEXT NOT NULL,
    type INTEGER NOT NULL,
    status_listened INTEGER NOT NULL, 
    listened_date TEXT
  )""")

  # Release's type table
  cur.execute("""CREATE TABLE IF NOT EXISTS type (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
  )""")
  
  # Release's type rows
  cur.execute("INSERT INTO type (name) VALUES ('Album'), ('EP')")

  # Genres table
  cur.execute("""CREATE TABLE IF NOT EXISTS genre (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    id_release INTEGER NOT NULL
  )""")

  con.commit()
  con.close()

def insert_mock_data(db_path: str):
  con = sqlite3.connect(db_path)
  cur = con.cursor()

  cur.execute("""INSERT INTO release (name, dt_release, artist, type, status_listened, listened_date) 
    VALUES ('We Will Always Love You', '11-12-2020', 'The Avalanches', 1, 0, NULL),
    ('The Piper at the Gates of Dawn', '21-05-1967', 'Pink Floyd', 1, 0, NULL),
    ('무너지기 (Crumbling)', '31-07-2018', '공중도둑 [Mid-Air Thief]', 1, 1, NULL)
  """)

  cur.execute("""INSERT INTO genre (name, id_release) 
    VALUES ('Electronic', 1),
    ('Neo-Psychedelia', 1),
    ('Psychedelic Rock', 2),
    ('Psychedelic Pop', 2),
    ('Neo-Psychedelia', 3),
    ('Folktronica', 3),
    ('Psychedelic Pop', 3)
  """)

  con.commit()
  con.close()