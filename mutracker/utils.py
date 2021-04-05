from typing import List

def join_query(statements: List[str]):
  return ' '.join(statements)

def or_like_clause(columns: List[str]):
  mapped = map(lambda column: f"{column} LIKE ?", columns)
  return ' or '.join(mapped)