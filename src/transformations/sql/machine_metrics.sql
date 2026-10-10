WITH machine_metrics AS (
    SELECT
        machine_id,
        COUNT(*) AS total_readings,

        ROUND(AVG(temperature), 2) AS avg_temperature,
        ROUND(MAX(temperature), 2) AS max_temperature,

        ROUND(AVG(pressure), 2) AS avg_pressure,

        ROUND(AVG(vibration), 3) AS avg_vibration,
        ROUND(MAX(vibration), 3) AS max_vibration,

        ROUND(AVG(rpm), 0) AS avg_rpm,

        COUNT(*) FILTER (WHERE status = 'RUNNING') AS running_readings,
        COUNT(*) FILTER (WHERE status = 'IDLE') AS idle_readings,
        COUNT(*) FILTER (WHERE status = 'WARNING') AS warning_readings

    FROM sensor_readings

    GROUP BY machine_id
)

SELECT
    *,
    ROUND(
        warning_readings::NUMERIC / total_readings * 100,
        2
    ) AS warning_rate,

    CASE
        WHEN max_temperature >= 105
             OR max_vibration >= 0.24
             OR warning_readings >= 40
            THEN 'CRITICAL'

        WHEN max_temperature >= 100
             OR max_vibration >= 0.22
             OR warning_readings >= 35
            THEN 'WATCH'

        ELSE 'NORMAL'
    END AS health_status

FROM machine_metrics

ORDER BY machine_id;