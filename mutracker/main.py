from .ui import Ui

class ArgsList():
  def __init__(self, where=None, **kwargs):
    self.where = where

class ArgsFind():
  def __init__(self, id=None, name=None, artist=None, **kwargs):
    self.identifier = id or name or artist

class ArgsAdd():
  def __init__(self, name=None, artist=None, genres=None, date_release=None, type=None, listened=None, date_listened=None, notes=None, **kwargs):
    self.name = name
    self.artist = artist
    self.genres = ','.split(genres) if ',' in genres else genres
    self.date_release = date_release
    self.type = type
    self.listened = listened
    self.date_listened = date_listened
    self.notes = notes

def main(args):
  ui = Ui()

  if args.command == 'list':
    list = ArgsList(**vars(args))
    ui.list_releases(list.where)
  elif args.command == 'find':
    find = ArgsFind(**vars(args))
    ui.find_releases(find.identifier)
  elif args.command == 'add':
    add = ArgsAdd(**vars(args))
    ui.add_release(add)
  
  pass
