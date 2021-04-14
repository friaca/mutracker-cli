from .ui import Ui

class ArgsList():
  def __init__(self, where=None, **kwargs):
    self.where = where

class ArgsFind():
  def __init__(self, id=None, name=None, artist=None, **kwargs):
    self.identifier = self.set_identifier(id, name, artist)
    self.search_terms = id or name or artist

  def set_identifier(self, id, name, artist):
    if id is not None:
      return 'id'
    elif name is not None:
      return 'name'
    elif artist is not None:
      return 'artist'

class ArgsAdd():
  def __init__(self, name=None, artist=None, genres=None, dt_release=None, type=None, listened=None, dt_listened=None, notes=None, **kwargs):
    self.name = name
    self.artist = artist
    self.genres = genres.split(',') if genres is not None and ',' in genres else [genres]
    self.dt_release = dt_release
    self.type = {'album': 1,'ep': 2}[type]
    self.listened = listened
    self.dt_listened = dt_listened
    self.notes = notes

class ArgsUpdate(ArgsAdd):
  pass

def main(args):
  ui = Ui()

  if args.command == 'list':
    list = ArgsList(**vars(args))
    ui.list_releases(list.where)
  elif args.command == 'find':
    find = ArgsFind(**vars(args))
    ui.find_releases(find.identifier, find.search_terms)
  elif args.command == 'add':
    add = ArgsAdd(**vars(args))
    ui.add_release(add)
  elif args.command == 'update':
    update = ArgsUpdate(**vars(args))
    ui.update_release(update)
  
  pass
