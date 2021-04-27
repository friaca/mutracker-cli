import sys
import functools
from .utils import join
from typing import Dict, List
from .models import Release
from .repository import ReleaseRepository

class ReleaseService():
  def __init__(self):
    self._repository = ReleaseRepository()

  def list_release(self, where) -> List[Release] or None:
    if where in ['all', 'listened', 'pending']:
      return self._repository.list(where)
    elif where == 'query':
      print('Query is not yet supported')
      sys.exit(1)
    else:
      print(f'Option "{where}" not valid for --list')
      sys.exit(1)

  def find_release_by_id(self, id: int):
    return self._repository.find_by_id(id)

  def find_release_by_name(self, name: str):
    return self._repository.find(['name'], name)

  def find_release_by_artist(self, artist: List[str]):
    return self._repository.find(['artist'], join(artist))
  
  def find_release_by_genre(self, genres: List[str]):
    return self._repository.find_by_genre(join(genres))

  def find_release_default(self, value: str):
    return self._repository.find(['name', 'artist'], join(value))

  def find_release(self, search_dict: Dict[str, List[str]]):
    COLUMN_MAP = {
      'id': self.find_release_by_id,
      'name': self.find_release_by_name,
      'artist': self.find_release_by_artist,
      'genre': self.find_release_by_genre,
      None: self.find_release_default,
    }

    def reducer(accumulator, current):
      key, search_terms = current

      for term in search_terms:
        accumulator += COLUMN_MAP[key](term)

      return accumulator
    
    results = functools.reduce(reducer, search_dict.items(), [])
    return results
    
  def add_release(self, pseudo_release: Release):
    release = self._repository.add_release(pseudo_release)
    return release

  def delete_release(argv):
    pass

  def update_release(argv):
    pass