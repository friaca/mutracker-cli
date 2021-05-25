import sys
import functools
from typing import Dict, List
from .models import Release
from .repository import ReleaseRepository

class ReleaseService():
  def __init__(self):
    self._repository = ReleaseRepository()

  def list_release(self, where) -> List[Release] or None:
    if where in ['all', 'listened', 'pending']:
      return self._repository.list(where)
    elif where in ['query']:
      print(f'{where} is not yet supported')
      sys.exit(1)
    else:
      print(f'Option "{where}" not valid for `list`')
      sys.exit(1)

  def find_release_by_id(self, id: int):
    return self._repository.find_by_id(id)

  def find_release_by_name(self, name: str):
    return self._repository.find(['name'], name)

  def find_release_by_artist(self, artist: str):
    return self._repository.find(['artist'], artist)
  
  def find_release_by_genre(self, genres: str):
    return self._repository.find_by_genre(genres)

  def find_release_default(self, value: str):
    return self._repository.find(['name', 'artist'], value)

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

  def update_release(self, pseudo_release: Release):
    old_release, = self.find_release_by_id(pseudo_release.id)
    old_genres = old_release.genres
    updated_release = old_release + pseudo_release
    release = self._repository.update_release(updated_release, set(old_genres) != set(updated_release.genres))
    return release

  def delete_release(argv):
    pass