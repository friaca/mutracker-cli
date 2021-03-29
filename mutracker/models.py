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
  listened_date: datetime

class ListOptions(Enum):
  all = 'all'
  listened = 'listened'
  pending = 'pending'
  # TODO: Implement query-like prop, so the user can retrieve custom lists
  # query = 'query'

  def __str__(self):
    return self.value