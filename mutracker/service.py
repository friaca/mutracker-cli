from typing import List
from .models import Release
from .repository import Repository

class Service():
  def __init__(self):
    self._repository = Repository()
    pass

  def list_release(self, argv) -> List[Release] or None:
    results = None
    if argv in ['all', 'listened', 'pending']:
      results = self._repository.list(argv)
    elif argv == 'query':
      pass
    else:
      print(f'Option {argv} not valid for --list')
      return
    
    return results

  def find_release(argv):
    pass

  def add_release(argv):
    pass

  def delete_release(argv):
    pass

  def update_release(argv):
    pass