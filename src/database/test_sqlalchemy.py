from sqlalchemy import text

from database.connection import engine


with engine.connect() as connection:
    result = connection.execute(text("SELECT COUNT(*) FROM sensor_readings"))
    count = result.scalar()

    print(f"Sensor readings in database: {count:,}")