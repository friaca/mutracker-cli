from .utils import DbUtils
from typing import List
from .models import Release
from .database import Database
from . import config

class ReleaseRepository():
  def __init__(self):
    self._database = Database(config['DB_PATH'])

  def map_release(self, query_results):
    return list(map(lambda r: Release(*r), query_results))

  def get_genres(self, id):
    sql = f'SELECT name FROM genre WHERE id_release = ?'
    return ', '.join(map(lambda name_tuple: name_tuple[0], self._database.query(sql, (id,))))

  def list(self, which: str):
    sql = ['SELECT * FROM release']

    if which == 'listened':
      sql += ['WHERE status_listened = 1']
    elif which == 'pending':
      sql += ['WHERE status_listened = 0']
    

    return map(lambda r: Release(*r), self._database.query(' '.join(sql)))

  def find(self, columns: List[str], value: str):
    db_utils = DbUtils.or_like_clause(columns)

    sql = ' '.join(['SELECT * FROM release', 'WHERE', db_utils])
    releases = self.map_release(self._database.query(sql, (f"%{value}%",) * len(columns)))
    
    for release in releases:
      release.genres = self.get_genres(release.id)
    
    return releases