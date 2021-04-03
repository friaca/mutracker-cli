from typing import List

class DbUtils():
  @staticmethod
  def or_like_clause(columns: List[str]):
    mapped = map(lambda column: f"{column} LIKE ?", columns)
    return ' or '.join(mapped)