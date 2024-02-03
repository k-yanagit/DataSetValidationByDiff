import mysql.connector
from database_processor import DatabaseProcessor

class MySQLProcessor(DatabaseProcessor):
    def __init__(self, host, user, password, database_name):
        self.mydb = mysql.connector.connect(host=host, user=user, password=password, database=database_name)
        self.mycursor = self.mydb.cursor()

    def get_table_names(self):
        self.mycursor.execute("SHOW TABLES")
        tables = [table[0] for table in self.mycursor.fetchall()]
        return tables

    def get_unique_count(self, table):
        self.mycursor.execute(f"SELECT COUNT(DISTINCT A) FROM `{table}`")
        count_a = self.mycursor.fetchone()[0]
        return count_a

    def sort_and_compare(self, sorted_tables):
        for i in range(len(sorted_tables)):
            for j in range(i + 1, len(sorted_tables)):
                table_k = sorted_tables[i]
                table_l = sorted_tables[j]
                query = f"""
                SELECT DISTINCT A
                FROM `{table_l}`
                WHERE A NOT IN (
                    SELECT DISTINCT A
                    FROM `{table_k}`
                )
                """
                self.mycursor.execute(query)
                results = self.mycursor.fetchall()
                for row in results:
                    print(row[0])

    def __del__(self):
        self.mycursor.close()
        self.mydb.close()
