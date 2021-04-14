from .models import Release
from typing import Dict, List
from rich import box
from rich.console import Console
from rich.table import Table
from .service import ReleaseService

class Ui():
  def __init__(self):
    self._console = Console(color_system="auto")
    self._service = ReleaseService()
  
  def ask(self, question: str):
    answer = None

    while answer == None:
      answer = input(f'> {question}:')
    
    return answer

  def display_table(self, table_opts: Dict[str, str], column_names: List[str], column_opts: Dict[str, str], rows: List[List[str]]):
    table = Table(**table_opts)

    for column_name in column_names:
      table.add_column(column_name, **column_opts)

    for index, row in enumerate(rows):
      styles = ["color(12)", "color(15)"]
      table.add_row(*row, style=styles[index % 2])

    self._console.print(table)

  def display_table_releases(self, releases: List[Release]):
    self.display_table(
      {'box': box.SIMPLE_HEAD, 'show_lines': True}, 
      ['ID', 'Name', 'Artist', 'Genres', 'Release date', 'Type', 'Listened', 'Listened date', 'Notes'], 
      {'justify': 'left', 'no_wrap': False},
      map(lambda r: r.get_renderable(), releases)
    )

  def list_releases(self, where: str):
    releases = self._service.list_release(where)
    self.display_table_releases(releases)

  # TODO: Find multiple things, like if I want to find albums by Pink Floyd and The Avalanches
  def find_releases(self, identifier: str, search_terms: List[str]):
    releases = self._service.find_release(identifier, search_terms)
    self.display_table_releases(releases)

  def add_release(self, pseudo_release: Release):
    release = self._service.add_release(pseudo_release)
    self.display_table_releases(release)

  def update_release(self, pseudo_release: Release):
    pass
