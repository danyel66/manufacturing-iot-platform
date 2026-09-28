CREATE TABLE sensor_readings (
    sensor_id VARCHAR(20) NOT NULL,
    machine_id VARCHAR(20) NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    temperature NUMERIC(10, 2),
    pressure NUMERIC(10, 2),
    vibration NUMERIC(10, 3),
    rpm INTEGER,
    status VARCHAR(20) NOT NULL,

    PRIMARY KEY (sensor_id, timestamp)
);