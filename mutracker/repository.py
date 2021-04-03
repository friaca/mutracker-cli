from .models import Release
from .database import Database
from . import config

class ReleaseRepository():
  def __init__(self):
    self._database = Database(config['DB_PATH'])

  def list(self, which: str):
    sql = ['SELECT * FROM release']

    if which == 'listened':
      sql += ['WHERE status_listened = 1']
    elif which == 'pending':
      sql += ['WHERE status_listened = 0']
    

    return map(lambda r: Release(*r), self._database.query(' '.join(sql)))