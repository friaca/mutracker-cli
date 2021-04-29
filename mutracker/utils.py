from mutracker.models import Release
from typing import Any, List

def join(words: List[Any], joiner=' '):
  return joiner.join([str(word) for word in words])

def or_like_clause(columns: List[str]):
  mapped = [f"{column} LIKE ?" for column in columns]
  return ' or '.join(mapped)

# TODO: Melhorar esse método, tá bem feio
def add_release_dict(pseudo_release: Release):
  genres = []

  if pseudo_release.genres is not None:
    genres = pseudo_release.genres
    pseudo_release.genres = None
  
  populated_fields = list(filter(lambda prop: prop[1] is not None, pseudo_release.__dict__.items()))
  columns = [entry[0] for entry in populated_fields]
  # TODO: Lidar com outros tipos de dado e não tratar tudo como string
  values = [f"'{entry[1]}'" for entry in populated_fields]

  return { 'release': (columns, values), 'genres': genres }