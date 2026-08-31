import psycopg2


#Connection configuration for openGauss database instance
DB_CONFIG = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "JezNbsX)93Cx4",
    "host": "localhost",
    "port": "5432"  #Default openGauss port is 5432
}


def run_lab_activity():
    try:
        #Establish connection to openGauss
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        print("Connected to openGauss database successfully.\n")

        #Schema Creation
        cursor.execute("""
            DROP TABLE IF EXISTS energy_metrics;
            CREATE TABLE energy_metrics (
                metric_id SERIAL PRIMARY KEY,
                device_name VARCHAR(50) NOT NULL,
                voltage_v REAL NOT NULL,
                current_a REAL NOT NULL,
                status VARCHAR(20) DEFAULT 'NORMAL'
            );
        """)
        conn.commit()
        print("Table 'energy_metrics' created.")

        #Data Insertion
        cursor.execute("""
            INSERT INTO energy_metrics (device_name, voltage_v, current_a, status) VALUES
                ('CT Sensor Lab 1', 220.5, 12.4, 'NORMAL'),
                ('CT Sensor Lab 2', 218.0, 32.1, 'HIGH_LOAD'),
                ('Voltage Sensor Lab 1', 245.2, 0.5, 'OVERVOLTAGE'),
                ('CT Sensor Lab 3', 221.1, 8.2, 'NORMAL');
        """)
        conn.commit()
        print("Sample data inserted.\n")

        #Test Cases / Filtered Queries

        print("=== Test Case 1: Select All Records ===")
        cursor.execute("SELECT * FROM energy_metrics;")
        for row in cursor.fetchall():
            print(f"ID: {row[0]} | Device: {row[1]:<20} | Voltage: {row[2]}V | Current: {row[3]}A | Status: {row[4]}")

        print("\n=== Test Case 2: Filter by Status ('NORMAL') ===")
        cursor.execute("SELECT device_name, current_a FROM energy_metrics WHERE status = 'NORMAL';")
        for row in cursor.fetchall():
            print(f"Device: {row[0]} | Current Reading: {row[1]}A")

        print("\n=== Test Case 3: Filter High Voltage (> 230V) ===")
        cursor.execute("SELECT device_name, voltage_v, status FROM energy_metrics WHERE voltage_v > 230.0;")
        for row in cursor.fetchall():
            print(f"Device: {row[0]} | Voltage: {row[1]}V | Alert: {row[2]}")

        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error executing openGauss script: {e}")


if __name__ == "__main__":
    run_lab_activity()