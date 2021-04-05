from typing import List

def join(words: List[str], joiner=' '):
  return joiner.join(words)

def or_like_clause(columns: List[str]):
  mapped = map(lambda column: f"{column} LIKE ?", columns)
  return ' or '.join(mapped)