from typing import List
from .utils import join, or_like_clause, add_release_dict
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
    sql = 'SELECT name FROM genre WHERE id_release = ?'
    return [name_tuple[0] for name_tuple in self._database.query(sql, (id,))]

  def list(self, which: str):
    sql = ['SELECT * FROM release']

    if which == 'listened':
      sql += ['WHERE status_listened = 1']
    elif which == 'pending':
      sql += ['WHERE status_listened = 0']
    
    return self.map_release(self._database.query(join(sql)))

  def find(self, columns: List[str], value: str):
    or_like = or_like_clause(columns)
    sql = join(['SELECT * FROM release', 'WHERE', or_like])
    releases = self.map_release(self._database.query(sql, (f"%{value}%",) * len(columns)))
    
    return releases

  def find_by_id(self, id: int):
    sql = 'SELECT * FROM release WHERE id = ?'
    return self.map_release(self._database.query(sql, (id,)))

  def find_by_genre(self, genre: str):
    sql = """SELECT * FROM release WHERE id IN 
      (SELECT id_release FROM genre WHERE name LIKE ? OR name LIKE ?)"""
    
    releases = self.map_release(self._database.query(sql, (f"%{genre}%",) * 2))

    return releases

  def add_release(self, pseudo_release: Release):
    dict = add_release_dict(pseudo_release)
    insert_release_query = f"INSERT INTO release ({join(dict['release'][0], ',')}) VALUES ({join(dict['release'][1], ',')})"
    self._database.query(insert_release_query)

    # Isso retorna uma tupla dentro de uma lista
    id = self._database.query("SELECT last_insert_rowid()")[0][0]

    if len(dict['genres']) > 0 and dict['genres'][0]:
      values_clause = join([f"('{genre.strip()}', {id})" for genre in dict['genres']], ',')
      insert_genre_query = f"INSERT INTO genre (name, id_release) VALUES {values_clause}"
      self._database.query(insert_genre_query)
    
    self._database.commit()

    return self.find_by_id(id)