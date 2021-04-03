from .ui import Ui 

def main(args):
  ui = Ui()
  
  if args.list:
    ui.list_releases(args.list)
  elif args.find:
    pass
  elif args.add:
    pass
  elif args.update:
    pass
  elif args.delete:
    pass
  
  pass
