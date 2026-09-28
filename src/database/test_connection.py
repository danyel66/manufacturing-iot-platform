import psycopg


connection = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="manufacturing",
    user="data_engineer",
    password="postgres",
)

print("Connected to PostgreSQL successfully.")

connection.close()

print("Connection closed.")