import argparse
from mutracker.main import main

def entry():
  print("""
                      __                  __            
     ____ ___  __  __/ /__________ ______/ /_____  _____
    / __ `__ \/ / / / __/ ___/ __ `/ ___/ //_/ _ \/ ___/
   / / / / / / /_/ / /_/ /  / /_/ / /__/ ,< /  __/ /    
  /_/ /_/ /_/\__,_/\__/_/   \__,_/\___/_/|_|\___/_/     
  """)

  parser = argparse.ArgumentParser(description="Mutracker | Music Tracking")
  subparsers = parser.add_subparsers(dest='command')

  list_parser = subparsers.add_parser('list')
  list_parser.add_argument('--where', nargs='?', const='all', default='all')

  find_parser = subparsers.add_parser('find')
  find_group = find_parser.add_mutually_exclusive_group(required=True)
  find_group.add_argument('-i', '--id')
  find_group.add_argument('-n', '--name')
  find_group.add_argument('-a', '--artist')

  add_parser = subparsers.add_parser('add')
  add_parser.add_argument('-n', '--name', required=True)
  add_parser.add_argument('-a', '--artist', required=True)
  add_parser.add_argument('-g', '--genres', nargs='?')
  add_parser.add_argument('-dr', '--date-release')
  add_parser.add_argument('-t', '--type', choices=['album', 'ep'], default='album')
  add_parser.add_argument('-l', '--listened')
  add_parser.add_argument('-dl', '--date-listened')
  add_parser.add_argument('-nt', '--notes')

  # update_parser = subparsers.add_parser('update')

  # delete_parser = subparsers.add_parser('delete')

  args = parser.parse_args()

  main(args)

if __name__ == '__main__':
  entry()