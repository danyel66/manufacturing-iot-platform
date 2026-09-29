from sqlalchemy import create_engine


DATABASE_URL = (
    "postgresql+psycopg://"
    "data_engineer:postgres@localhost:5432/manufacturing"
)


engine = create_engine(DATABASE_URL)