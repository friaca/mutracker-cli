from .models import Release
from typing import Dict, List
from rich import box
from rich.console import Console
from rich.table import Table

class Ui():
  def __init__(self):
    self._console = Console(color_system="auto")

  def print(self, message: str, status: str = 'info'):
    color = {
      'info': 'bold white',
      'success': 'bold green',
      'warning': 'bold yellow',
      'error': 'bold red'
    }[status]

    self._console.print(message, style=color)
    pass
  
  def ask(self, question: str):
    answer = None

    while answer == None:
      answer = input(f'> {question} ')
    
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
      ['ID', 'Name', 'Artist', 'Genres', 'Release date', 'Type', 'Listened', 'Listened date', 'Notes', 'Reg. date'], 
      {'justify': 'left', 'no_wrap': False},
      [release.get_renderable() for release in releases]
    )