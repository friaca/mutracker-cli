from enum import Enum
from datetime import datetime
from typing import List

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
  type: str
  # Wheter the user has listened to the release or not
  status_listened: bool
  # If listened, the date in which the user listened to the album
  dt_listened: datetime
  # Notes on the release, whatever the user might want to write
  notes: str

  def __init__(self, id, name, artist, dt_release, type, status_listened, dt_listened, notes):
    self.id = id if id is not None else 0
    self.name = name
    self.artist = artist
    self.dt_release = dt_release
    self.type = type
    self.status_listened = status_listened
    self.dt_listened = dt_listened
    self.notes = notes

  def get_renderable(self):
    return map(lambda r: str(r), self.__dict__.values())