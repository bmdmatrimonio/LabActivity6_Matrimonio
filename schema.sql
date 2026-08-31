--OpenGauss Table Schema Creation
DROP TABLE IF EXISTS energy_metrics;

CREATE TABLE energy_metrics (
    metric_id SERIAL PRIMARY KEY,
    device_name VARCHAR(50) NOT NULL,
    voltage_v REAL NOT NULL,
    current_a REAL NOT NULL,
    status VARCHAR(20) DEFAULT 'NORMAL'
);

--Insert Sample Records
INSERT INTO energy_metrics (device_name, voltage_v, current_a, status) VALUES
('CT Sensor Lab 1', 220.5, 12.4, 'NORMAL'),
('CT Sensor Lab 2', 218.0, 32.1, 'HIGH_LOAD'),
('Voltage Sensor Lab 1', 245.2, 0.5, 'OVERVOLTAGE'),
('CT Sensor Lab 3', 221.1, 8.2, 'NORMAL');

--Filtered Queries
--All Records
SELECT * FROM energy_metrics;

--Normal Status Only
SELECT device_name, current_a FROM energy_metrics WHERE status = 'NORMAL';

--Overvoltage Threshold
SELECT device_name, voltage_v, status FROM energy_metrics WHERE voltage_v > 230.0;