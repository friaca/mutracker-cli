from typing import List
from .utils import join, or_like_clause
from .models import Release
from .database import Database
from . import config

class ReleaseRepository():
  def __init__(self):
    self._database = Database(config['DB_PATH'])

  def map_release(self, query_results):
    releases = [Release(*release) for release in query_results]

    for release in releases:
      release.genres = self.get_genres(release.id)

    return releases

  def get_genres(self, id):
    query = 'SELECT name FROM genre WHERE id_release = ?'
    return [name_tuple[0] for name_tuple in self._database.query(query, (id,))]

  def list(self, which: str):
    query = ['SELECT * FROM release']

    if which == 'listened':
      query += ['WHERE status_listened = 1']
    elif which == 'pending':
      query += ['WHERE status_listened = 0']
    
    return self.map_release(self._database.query(join(query)))

  def find(self, columns: List[str], value: str):
    or_like = or_like_clause(columns)
    query = join(['SELECT * FROM release', 'WHERE', or_like])
    releases = self.map_release(self._database.query(query, (f"%{value}%",) * len(columns)))
    
    return releases

  def find_by_id(self, id: int):
    query = 'SELECT * FROM release WHERE id = ?'
    return self.map_release(self._database.query(query, (id,)))

  def find_by_genre(self, genre: str):
    sql = """SELECT * FROM release WHERE id IN 
      (SELECT id_release FROM genre WHERE name LIKE ? OR name LIKE ?)"""
    
    releases = self.map_release(self._database.query(sql, (f"%{genre}%",) * 2))

    return releases

  def add_release(self, pseudo_release: Release):
    genres = pseudo_release.genres if pseudo_release.genres else []

    fields = [(key, value) for key, value in pseudo_release.__dict__.items() if key not in ['genres'] and value]
    columns = [key for key, value in fields]
    values = [value for key, value in fields]

    release_query = f"INSERT INTO release ({join(columns, ',')}) VALUES ({join(['?'] * len(values), ',')})"
    self._database.execute(release_query, values)

    # Isso retorna uma tupla dentro de uma lista
    id_release = self._database.query("SELECT last_insert_rowid()")[0][0]

    if genres:
      genre_query_values = join([f"(?, {id_release})"] * len(genres), ', ')
      genres_query = f"INSERT INTO genre (name, id_release) VALUES {genre_query_values}"
      self._database.execute(genres_query, genres)

    self._database.commit()
    return self.find_by_id(id_release)


