import rich
from .service import Service

class Ui():
  def __init__(self):
    self._service = Service()
  
  def ask(self, question):
    answer = None

    while answer == None:
      answer = input(f'> {question}:')
    
    return answer

  def list_releases(self):
    print('Listing all releases...')
    releases = self._service.list_release('all')

    rich.print(releases)