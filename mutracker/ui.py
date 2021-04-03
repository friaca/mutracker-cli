from .models import Release
from typing import Dict, List
from rich import print as rprint
from rich.console import Console
from rich.table import Table
from .service import ReleaseService

class Ui():
  def __init__(self):
    self._console = Console()
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

    for row in rows:
      table.add_row(*row)

    self._console.print(table)

  def display_table_releases(self, releases: List[Release]):
    self.display_table(
      {'title': 'Releases'}, 
      ['ID', 'Name', 'Artist', 'Release date', 'Type', 'Listened', 'Listened date', 'Notes'], 
      {'justify': 'left', 'no_wrap': True},
      map(lambda r: r.get_renderable(), releases)
    )

  def list_releases(self, which: str):
    releases = self._service.list_release(which)
    self.display_table_releases(releases)
