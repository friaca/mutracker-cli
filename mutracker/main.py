from .ui import Ui

class ArgsList():
  def __init__(self, where=None, **kwargs):
    self.where = where

class ArgsFind():
  def __init__(self, id=None, name=None, artist=None, **kwargs):
    self.search_dict = self.set_search_dict(id, name, artist)

  def set_search_dict(self, id, name, artist):
    identity = (('id', id), ('name', name), ('artist', artist))
    return { key : [' '.join(search) for search in value] for (key, value) in identity if value is not None }

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
    ui.find_releases(find.search_dict)
  elif args.command == 'add':
    add = ArgsAdd(**vars(args))
    ui.add_release(add)
  elif args.command == 'update':
    update = ArgsUpdate(**vars(args))
    ui.update_release(update)
  
  pass
