import pandas as pd
import psycopg


INPUT_FILE = "data/clean_sensor_readings.csv"


df = pd.read_csv(INPUT_FILE)

print(f"Loaded {len(df):,} clean records.")


connection = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="manufacturing",
    user="data_engineer",
    password="postgres",
)

print("Connected to PostgreSQL.")


with connection.cursor() as cursor:
    for _, row in df.iterrows():
        cursor.execute(
            """
            INSERT INTO sensor_readings (
                sensor_id,
                machine_id,
                timestamp,
                temperature,
                pressure,
                vibration,
                rpm,
                status
            )
            VALUES (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            )
            """,
            (
                row["sensor_id"],
                row["machine_id"],
                row["timestamp"],
                row["temperature"],
                row["pressure"],
                row["vibration"],
                row["rpm"],
                row["status"],
            ),
        )


connection.commit()

print(f"Inserted {len(df):,} records.")

connection.close()

print("Connection closed.")