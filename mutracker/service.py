from typing import List
from .models import Release
from .repository import ReleaseRepository

class ReleaseService():
  def __init__(self):
    self._repository = ReleaseRepository()

  def list_release(self, argv) -> List[Release] or None:
    if argv in ['all', 'listened', 'pending']:
      return self._repository.list(argv)
    elif argv == 'query':
      pass
    else:
      print(f'Option {argv} not valid for --list')
      return

  def find_release(argv):
    pass

  def add_release(argv):
    pass

  def delete_release(argv):
    pass

  def update_release(argv):
    pass