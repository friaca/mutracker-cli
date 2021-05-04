import random
import requests
import re
from bs4 import BeautifulSoup
from rich.console import Console
from os import system
from .utils import USER_AGENTS, MONTHS

console = Console()

def is_valid_url(url: str):
  DOMAINS = ['rateyourmusic.com']
  
  for domain in DOMAINS:
    if domain in url:
      return True

  return False

def fetch_release(url: str = None, stream: str = None):

  if stream is not None:
    content = stream
  elif url is not None:
    if not is_valid_url(url):
      print('Invalid URL')
      system.exit(1)
    
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
    def select_name(dom):
      full_name = dom.select('.page_section .album_title')[0].get_text(strip=True)
      by_index = full_name.index('By')
      return full_name[:by_index]

    def select_dt_release(dom):
      full_date = dom.findAll('th', {'class':'info_hdr'})[2].find_next().get_text(strip=True)
      regex = r'^(\d+) ([a-zA-Z]+)(\d+)$'
      matches = re.search(regex, full_date)
      return f'{matches.group(3)}-{MONTHS[matches.group(2)]}-{matches.group(1)}'
    
    def select_type(dom):
      value = dom.findAll('th', {'class':'info_hdr'})[1].find_next().get_text(strip=True)
      return value

    selectors = {
      'name': lambda dom: select_name(dom),
      'artist': lambda dom: dom.select('.page_section .artist')[0].get_text(strip=True),
      'dt_release': lambda dom: select_dt_release(dom),
      'genres': lambda dom: dom.select('.release_pri_genres')[0].get_text(strip=True),
      'type': lambda dom: select_type(dom)
    }
    
    parsed = BeautifulSoup(content, 'html.parser')
    release_map = {
      'id': None,
      'name': None,
      'artist': None,
      'genres': None,
      'dt_release': None,
      'type': None,
      'dt_create': None,
      'status_listened': None,
      'dt_listened': None,
      'notes': None,
      'genres': None
    }

    for key, fn in selectors.items():
      value = fn(parsed)
      release_map[key] = value

  return release_map