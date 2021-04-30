import random
import requests
from bs4 import BeautifulSoup
from rich.console import Console
from os import system
from .utils import USER_AGENTS

console = Console()

def fetch_release(url: str = None, stream: str = None):
  if stream is not None:
    content = stream
  elif url is not None:
    with console.status("[bold green]Downloading...") as status:
      headers = {
        'user-agent': random.choice(USER_AGENTS),
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'upgrade-insecure-requests': '1'
      }

      response = requests.get(url, headers=headers)
      content = response.content
  else:
    print('No URL or stream provided!')
    system.exit(1)

  with console.status("[bold green]Processing...") as status:
    selectors = {
      'name': lambda dom: dom.select('.page_section .album_title')[0],
      'artist': lambda dom: dom.select('.page_section .artist')[0],
      'dt_release': lambda dom: dom.findAll('th', {'class':'info_hdr'})[2],
      'genres': lambda dom: dom.select('.release_pri_genres')[0],
      'type': lambda dom: dom.findAll('th', {'class':'info_hdr'})[1].find_next()
    }
    
    parsed = BeautifulSoup(content, 'html.parser')
    release_map = {}

    for key, fn in selectors.items():
      elem = fn(parsed)
      print(elem)
      text = elem.get_text(strip=True)
      print(text)
      release_map[key] = text

  print(release_map)
  pass