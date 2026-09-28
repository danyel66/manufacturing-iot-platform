import random

import pandas as pd


INPUT_FILE = "data/sensor_readings.csv"
OUTPUT_FILE = "data/raw_sensor_readings.csv"

df = pd.read_csv(INPUT_FILE)

random.seed(42)

# 1. Introduce missing values
for _ in range(20):
    row = random.randrange(len(df))
    column = random.choice(["temperature", "pressure", "vibration"])

    df.loc[row, column] = None


# 2. Introduce invalid measurements
for _ in range(10):
    row = random.randrange(len(df))
    column = random.choice(["temperature", "pressure", "vibration"])

    if column == "temperature":
        df.loc[row, column] = 500

    elif column == "pressure":
        df.loc[row, column] = -20

    elif column == "vibration":
        df.loc[row, column] = 10


# 3. Introduce duplicate records
duplicates = df.sample(n=20, random_state=42)
df = pd.concat([df, duplicates], ignore_index=True)


# Save the messy dataset
df.to_csv(OUTPUT_FILE, index=False)

print(f"Generated raw dataset with {len(df):,} records.")
print(f"Saved to {OUTPUT_FILE}")