import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd
from faker import Faker


fake = Faker()

NUM_SENSORS = 10
RECORDS_PER_SENSOR = 100
OUTPUT_FILE = "data/sensor_readings.csv"

sensors = []

for i in range(1, NUM_SENSORS + 1):
    sensors.append(
        {
            "sensor_id": f"S{i:03d}",
            "machine_id": f"M{((i - 1) // 2) + 1:03d}",
        }
    )


records = []

start_time = datetime.now() - timedelta(hours=24)

for sensor in sensors:
    for reading_number in range(RECORDS_PER_SENSOR):
        timestamp = start_time + timedelta(
            minutes=reading_number
        )

        records.append(
            {
                "sensor_id": sensor["sensor_id"],
                "machine_id": sensor["machine_id"],
                "timestamp": timestamp,
                "temperature": round(np.random.normal(75, 10), 2),
                "pressure": round(np.random.normal(30, 5), 2),
                "vibration": round(abs(np.random.normal(0.1, 0.05)), 3),
                "rpm": int(np.random.normal(1500, 150)),
                "status": random.choice(
                    ["RUNNING", "RUNNING", "RUNNING", "IDLE", "WARNING"]
                ),
            }
        )

df = pd.DataFrame(records)

df.to_csv(OUTPUT_FILE, index=False)

print(f"Generated {len(df):,} sensor readings.")
print(f"Saved to {OUTPUT_FILE}")