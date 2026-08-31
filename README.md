## Lab Activity 6: openGauss Database Operations
**Description**
    This project demonstrates connecting to an openGauss/PostgreSQL relational database management system using Python's `psycopg2` driver. It handles schema creation, record insertion, and sample filtered query retrievals.

**Prerequisites**
* **Python 3.x**
* **PostgreSQL / openGauss Database Engine** running locally on port `5432`
* **psycopg2 Library**: Used as the database adapter for Python to execute SQL commands.

## Environment Setup

1. **Install psycopg2 Driver:**
   Run the following command in your terminal/WSL environment:
   `pip install psycopg2-binary`

## Database Service:
    Ensure your local PostgreSQL or openGauss service is active and listening on port 5432, and create the target database if necessary:
        ```SQL
        `CREATE DATABASE opengauss_db`

## How to Run
1. Open your terminal or WSL Ubuntu environment.

2. Navigate to the project directory:
    `cd lab_activity_6`

3. Run the Python script:
    `python3 opengauss_script.py`

Sample Terminal Output
Connected to openGauss database successfully.

Table 'energy_metrics' created.
Sample data inserted.

=== Test Case 1: Select All Records ===
ID: 1 | Device: CT Sensor Lab 1      | Voltage: 220.5V | Current: 12.4A | Status: NORMAL
ID: 2 | Device: CT Sensor Lab 2      | Voltage: 218.0V | Current: 32.1A | Status: HIGH_LOAD
ID: 3 | Device: Voltage Sensor Lab 1 | Voltage: 245.2V | Current: 0.5A | Status: OVERVOLTAGE
ID: 4 | Device: CT Sensor Lab 3      | Voltage: 221.1V | Current: 8.2A | Status: NORMAL

=== Test Case 2: Filter by Status ('NORMAL') ===
Device: CT Sensor Lab 1 | Current Reading: 12.4A
Device: CT Sensor Lab 3 | Current Reading: 8.2A

=== Test Case 3: Filter High Voltage (> 230V) ===
Device: Voltage Sensor Lab 1 | Voltage: 245.2V | Alert: OVERVOLTAGE