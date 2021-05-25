import sys
from .ui import Ui
from .service import ReleaseService
from .scraper import fetch_release

class ArgsList():
  def __init__(self, where=None, **kwargs):
    self.where = where

class ArgsFind():
  def __init__(self, id=None, name=None, artist=None, genre=None, **kwargs):
    self.search_dict = self.set_search_dict(id, name, artist, genre)

  def set_search_dict(self, id, name, artist, genre):
    identity = (('id', id), ('name', name), ('artist', artist), ('genre', genre))
    return { key : [' '.join(search) for search in value] for (key, value) in identity if value }

class ArgsAdd():
  def __init__(self, url=None, name=None, artist=None, genres=None, dt_release=None, type=None, status_listened=None, dt_listened=None, notes=None, **kwargs):
    self.url = url
    self.name = name
    self.artist = artist
    self.genres = genres.split(',') if genres and ',' in genres else [genres]
    self.dt_release = dt_release
    self.type = {'album': 1,'ep': 2}[type.lower()]
    self.status_listened = status_listened
    self.dt_listened = dt_listened
    self.notes = notes

class ArgsUpdate(ArgsAdd):
  def __init__(self, id=None, **kwargs):
    super().__init__(**kwargs)
    self.id = id

def main(args):
  ui = Ui()
  service = ReleaseService()

  if args.command == 'list':
    list = ArgsList(**vars(args))
    releases = service.list_release(list.where)
  elif args.command == 'find':
    find = ArgsFind(**vars(args))
    releases = service.find_release(find.search_dict)
  elif args.command == 'add':
    if args.url:
      add = ArgsAdd(**fetch_release(url=args.url))
    else:
      add = ArgsAdd(**vars(args))
    releases = service.add_release(add)
  elif args.command == 'update':
    update = ArgsUpdate(**vars(args))
    releases = service.update_release(update)
  else:
    print('bruh')
    sys.exit(1)
  
  ui.display_table_releases(releases)
