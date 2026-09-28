import pandas as pd


INPUT_FILE = "data/raw_sensor_readings.csv"
CLEAN_FILE = "data/clean_sensor_readings.csv"
QUARANTINE_FILE = "data/quarantine_sensor_readings.csv"


df = pd.read_csv(INPUT_FILE)

print(f"Loaded {len(df):,} records.")


required_columns = [
    "sensor_id",
    "machine_id",
    "timestamp",
]

missing_required = df[required_columns].isna().any(axis=1)

print(
    f"Records with missing required fields: "
    f"{missing_required.sum()}"
)


measurement_columns = [
    "temperature",
    "pressure",
    "vibration",
    "rpm",
]

missing_measurements = df[measurement_columns].isna().any(axis=1)

print(
    f"Records with missing measurements: "
    f"{missing_measurements.sum()}"
)

# Check duplicates
duplicate_record = df.duplicated(
    subset=["sensor_id", "timestamp"],
    keep=False
)

print(
    f"Records with duplicate sensor/timestamp combinations: "
    f"{duplicate_record.sum()}"
)

invalid_temperature = (
    (df["temperature"] < -20)
    | (df["temperature"] > 150)
)

invalid_pressure = (
    (df["pressure"] < 0)
    | (df["pressure"] > 100)
)

invalid_vibration = (
    (df["vibration"] < 0)
    | (df["vibration"] > 5)
)

invalid_rpm = (
    (df["rpm"] < 0)
    | (df["rpm"] > 5000)
)

invalid_measurements = (
    invalid_temperature
    | invalid_pressure
    | invalid_vibration
    | invalid_rpm
)

print(
    f"Records with invalid measurements: "
    f"{invalid_measurements.sum()}"
)

invalid_record = (
    missing_required
    | missing_measurements
    | invalid_measurements
    | duplicate_record
)

print(
    f"Total invalid records: "
    f"{invalid_record.sum()}"
)

clean_df = df[~invalid_record].copy()

quarantine_df = df[invalid_record].copy()

clean_df.to_csv(CLEAN_FILE, index=False)

quarantine_df.to_csv(QUARANTINE_FILE, index=False)

print(f"Clean records: {len(clean_df):,}")
print(f"Quarantined records: {len(quarantine_df):,}")

print(f"Saved clean data to {CLEAN_FILE}")
print(f"Saved quarantine data to {QUARANTINE_FILE}")