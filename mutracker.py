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
  args_group = parser.add_mutually_exclusive_group()
  args_group.add_argument('-l', '--list')
  args_group.add_argument('-f', '--find', nargs='+')
  args_group.add_argument('-a', '--add', nargs='+')
  args_group.add_argument('-d', '--delete')
  args_group.add_argument('-u', '--update')

  args = parser.parse_args()

  main(args)

if __name__ == '__main__':
  entry()