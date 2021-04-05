import sys
from typing import List
from .models import Release
from .repository import ReleaseRepository

class ReleaseService():
  def __init__(self):
    self._repository = ReleaseRepository()

  def get_column_and_search(self, argv):
    # TODO: Handling of multiple search terms, 
    # like if I want to search for both Pink Floyd and The Avalanches
    if len(argv) == 1:
      return None, argv[0]
    else:
      column, *search_terms = argv
      return column, ' '.join(search_terms)

  def list_release(self, argv) -> List[Release] or None:
    if argv in ['all', 'listened', 'pending']:
      return self._repository.list(argv)
    elif argv == 'query':
      print('Query is not yet supported')
      sys.exit(1)
    else:
      print(f'Option {argv} not valid for --list')
      sys.exit(1)

  def find_release_by_id(self, id: int):
    return self._repository.find_by_id(id)

  def find_release_by_name(self, name: str):
    return self._repository.find(['name'], name)

  def find_release_by_artist(self, artist: str):
    return self._repository.find(['artist'], artist)
  
  def find_release_default(self, value: str):
    return self._repository.find(['name', 'artist'], ' '.join(value))

  def find_release_by_genre(self, genres: List[str]):
    return self._repository.find_by_genre(genres)

  def find_release(self, argv: List[str] or str or int):
    column, search_terms = self.get_column_and_search(argv)

    COLUMN_MAP = {
      'id': self.find_release_by_id,
      'name': self.find_release_by_name,
      'artist': self.find_release_by_artist,
      'genre': self.find_release_by_genre,
      None: self.find_release_default,
    }

    return COLUMN_MAP[column](search_terms)
    
  def add_release(argv):
    pass

  def delete_release(argv):
    pass

  def update_release(argv):
    pass