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
    listened_date TEXT NOT NULL
  )""")

  # Release's type table
  cur.execute("""CREATE TABLE IF NOT EXISTS type (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
  )""")
  
  # Release's type rows
  cur.execute("""INSERT INTO type (name)
    VALUES ('Album'), ('EP')
  """)

  # Genres table
  cur.execute("""CREATE TABLE IF NOT EXISTS genre (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    id_release INTEGER NOT NULL
  )""")

  con.commit()
  con.close()