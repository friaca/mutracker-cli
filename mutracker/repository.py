from .utils import DbUtils
from typing import List
from .models import Release
from .database import Database
from . import config

class ReleaseRepository():
  def __init__(self):
    self._database = Database(config['DB_PATH'])

  def map_release(self, query_results):
    releases = list(map(lambda r: Release(*r), query_results))

    for release in releases:
      release.genres = self.get_genres(release.id)

    return releases

  def get_genres(self, id):
    sql = f'SELECT name FROM genre WHERE id_release = ?'
    return list(map(lambda name_tuple: name_tuple[0], self._database.query(sql, (id,))))

  def list(self, which: str):
    sql = ['SELECT * FROM release']

    if which == 'listened':
      sql += ['WHERE status_listened = 1']
    elif which == 'pending':
      sql += ['WHERE status_listened = 0']
    

    return self.map_release(self._database.query(DbUtils.join_query(sql)))

  def find(self, columns: List[str], value: str):
    db_utils = DbUtils.or_like_clause(columns)
    sql = DbUtils.join_query(['SELECT * FROM release', 'WHERE', db_utils])
    releases = self.map_release(self._database.query(sql, (f"%{value}%",) * len(columns)))
    
    return releases

  def find_by_genre(self, genre: str):
    sql = """SELECT * FROM release WHERE id IN 
      (SELECT id_release FROM genre WHERE name LIKE ? OR name LIKE ?)"""
    
    releases = self.map_release(self._database.query(sql, (f"%{genre}%",) * 2))

    return releases