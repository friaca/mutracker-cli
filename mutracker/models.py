from enum import Enum
from datetime import datetime
from typing import List, Literal

class BaseModel:
  # Database UID
  id: int
  # Entry create date timestamp
  dt_create: datetime

class Release(BaseModel):
  # Name of the album
  name: str
  # Release date of the record
  dt_release: datetime 
  # Artist's/band's name
  artist: str
  # Release genres
  genres: List[str]
  # Release type (Album or EP)
  type: Literal['Album', 'EP', '?']
  # Wheter the user has listened to the release or not
  status_listened: bool
  # If listened, the date in which the user listened to the album
  dt_listened: datetime
  # Notes on the release, whatever the user might want to write
  notes: str

  def __init__(self, id, name, artist, dt_release, type, status_listened, dt_listened, notes, dt_create, genres = None):
    self.id = id or 0
    self.name = name
    self.artist = artist
    self.genres = genres
    self.dt_release = self.parse_date(dt_release)
    self.type = self.parse_type(type)
    self.status_listened = status_listened
    self.dt_listened = self.parse_date(dt_listened)
    self.notes = notes
    self.dt_create = dt_create

  def parse_type(self, type: int):
    if type == 1:
      return 'Album'
    elif type == 2:
      return 'EP'
    
    return '?'

  def parse_date(self, date: str):
    if date is None: 
      return None
    else:
      # '2020-12-31' -> [2020, 12, 31]
      date_to_int_list = [int(part) for part in date.split('-')]

      return datetime(*date_to_int_list)

  def get_renderable(self):
    # Fields to hide when rendering table
    # block_list = ['dt_create']

    parse_bool = lambda val: 'Yes' if val == 1 else 'No'
    parse_array = lambda arr: ', '.join(arr)
    format_date = lambda date: date.strftime("%d/%m/%Y")

    def mapper(entry):
      if entry[0] in ['status_listened']:
        return parse_bool(entry[1])
      if entry[0] in ['genres']:
        return parse_array(entry[1])
      if entry[0] in ['dt_release', 'dt_listened'] and entry[1] is not None:
        return format_date(entry[1])

      return str(entry[1])

    # items = [item for item in self.__dict__.items() if item[0] not in block_list]
    items = self.__dict__.items()
    return [mapper(entry) for entry in items]