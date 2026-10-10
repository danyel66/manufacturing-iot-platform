from pathlib import Path

import pandas as pd

from database.connection import engine


SQL_FILE = Path(__file__).parent / "sql" / "machine_metrics.sql"


query = SQL_FILE.read_text()


with engine.connect() as connection:
    df = pd.read_sql_query(query, connection)


print(df)