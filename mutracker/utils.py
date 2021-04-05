from typing import List

class DbUtils():
  @staticmethod
  def join_query(statements: List[str]):
    return ' '.join(statements)

  @staticmethod
  def or_like_clause(columns: List[str]):
    mapped = map(lambda column: f"{column} LIKE ?", columns)
    return ' or '.join(mapped)

class Utils():
  @staticmethod
  def is_int(s):
    try:
        return float(str(s)).is_integer()
    except:
        return False