from enum import Enum

class ListOptions(Enum):
  all = 'all'
  listened = 'listened'
  pending = 'pending'
  # TODO: Implement query-like prop, so the user can retrieve custom lists
  # query = 'query'

  def __str__(self):
    return self.value