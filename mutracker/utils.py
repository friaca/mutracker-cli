from mutracker.models import Release
from typing import List

def join(words: List[str], joiner=' '):
  stringified = list(map(lambda word: str(word), words))
  return joiner.join(stringified)

def or_like_clause(columns: List[str]):
  mapped = map(lambda column: f"{column} LIKE ?", columns)
  return ' or '.join(mapped)

# TODO: Melhorar esse método, tá bem feio
def add_release_dict(pseudo_release: Release):
  genres = []

  if pseudo_release.genres is not None:
    genres = pseudo_release.genres
    pseudo_release.genres = None
  
  populated_fields = list(filter(lambda prop: prop[1] is not None, pseudo_release.__dict__.items()))
  columns = list(map(lambda entry: entry[0], populated_fields))
  # TODO: Lidar com outros tipos de dado e não tratar tudo como string
  values = list(map(lambda entry: f"'{entry[1]}'", populated_fields))

  return { 'release': (columns, values), 'genres': genres }