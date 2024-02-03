# Database Table Comparison Tool

This tool is designed to compare tables across different databases (BigQuery, MySQL, and PostgreSQL) to find unique records in a specified column (column A). The program sorts tables based on the count of unique records in column A and then compares the records between each pair of tables.

## How to Use

1. Ensure you have the required permissions and database credentials.
2. Install necessary Python libraries:
   - For BigQuery: `google-cloud-bigquery`
   - For MySQL: `mysql-connector-python`
   - For PostgreSQL: `psycopg2-binary`
3. Configure database connection settings in each processor file.
4. Execute the main processing file for your database.

## Files

1. `database_processor.py`:
   - Abstract base class defining the template for database operations.

2. `bigquery_processor.py`:
   - Implementation of the DatabaseProcessor for BigQuery.
   - Methods: `get_table_names`, `get_unique_count`, `sort_and_compare`.

3. `mysql_processor.py`:
   - Implementation of the DatabaseProcessor for MySQL.
   - Methods: `get_table_names`, `get_unique_count`, `sort_and_compare`.
   - Cleans up database resources using `__del__`.

4. `postgresql_processor.py`:
   - Implementation of the DatabaseProcessor for PostgreSQL.
   - Methods: `get_table_names`, `get_unique_count`, `sort_and_compare`.
   - Cleans up database resources using `__del__`.

## Requirements

- Python 3.x
- Access to the respective databases with the appropriate privileges.
- Necessary Python packages installed.

## Installation

Install the required Python packages by running:

- Big Query
```bash
pip install google-cloud-bigquery mysql-connector-python psycopg2-binary
```

- MySQL
```bash
pip install mysql-connector-python
```

- postgresSQL
```bash
pip install psycopg2-binary
```
## Configuration

Before running the program, ensure that the database connection settings in each processor file (`bigquery_processor.py`, `mysql_processor.py`, `postgresql_processor.py`) are correctly configured to match your database setup.

## Execution

To execute the program, run the main processing file for your database. For example, for MySQL:

```python
from mysql_processor import MySQLProcessor

mysql_processor = MySQLProcessor("host", "user", "password", "database_name")
mysql_processor.process_tables()
```

Replace the connection parameters and database name with your own details.

## License

Apache License Version 2.0
