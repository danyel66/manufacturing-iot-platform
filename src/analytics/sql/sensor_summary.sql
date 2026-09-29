SELECT
    sensor_id,
    machine_id,
    COUNT(*) AS reading_count,
    ROUND(AVG(temperature), 2) AS avg_temperature,
    ROUND(MAX(temperature), 2) AS max_temperature,
    ROUND(AVG(pressure), 2) AS avg_pressure,
    ROUND(AVG(vibration), 3) AS avg_vibration,
    ROUND(AVG(rpm), 0) AS avg_rpm
FROM sensor_readings
GROUP BY sensor_id, machine_id
ORDER BY sensor_id;