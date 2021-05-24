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
  find_parser.add_argument('-i', '--id', nargs='+', action='append')
  find_parser.add_argument('-n', '--name', nargs='+', action='append')
  find_parser.add_argument('-a', '--artist', nargs='+', action='append')
  find_parser.add_argument('-g', '--genre', nargs='+', action='append')

  add_parser = subparsers.add_parser('add')
  add_parser.add_argument('-u', '--url')
  add_parser.add_argument('-n', '--name')
  add_parser.add_argument('-a', '--artist')
  add_parser.add_argument('-g', '--genres', nargs='?')
  add_parser.add_argument('-dr', '--date-release', dest='dt_release')
  add_parser.add_argument('-t', '--type', choices=['album', 'ep'], default='album')
  add_parser.add_argument('-l', '--listened', type=int, dest='status_listened')
  add_parser.add_argument('-dl', '--date-listened', dest='dt_listened')
  add_parser.add_argument('-nt', '--notes')

  update_parser = subparsers.add_parser('update')
  update_parser.add_argument('-i', '--id', required=True)
  update_parser.add_argument('-n', '--name')
  update_parser.add_argument('-a', '--artist')
  update_parser.add_argument('-g', '--genres', nargs='?')
  update_parser.add_argument('-dr', '--date-release', dest='dt_release')
  update_parser.add_argument('-t', '--type', choices=['album', 'ep'])
  update_parser.add_argument('-l', '--listened', type=int, dest='status_listened')
  update_parser.add_argument('-dl', '--date-listened', dest='dt_listened')
  update_parser.add_argument('-nt', '--notes')


  # delete_parser = subparsers.add_parser('delete')

  args = parser.parse_args()

  main(args)

if __name__ == '__main__':
  entry()