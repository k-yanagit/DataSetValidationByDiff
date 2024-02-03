import psycopg2
from database_processor import DatabaseProcessor

class PostgreSQLProcessor(DatabaseProcessor):
    def __init__(self, host, dbname, user, password, port=5432):
        self.conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password, port=port)
        self.cursor = self.conn.cursor()

    def get_table_names(self):
        self.cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
        tables = [table[0] for table in self.cursor.fetchall()]
        return tables

    def get_unique_count(self, table):
        self.cursor.execute(f"SELECT COUNT(DISTINCT A) FROM {table}")
        count_a = self.cursor.fetchone()[0]
        return count_a

    def sort_and_compare(self, sorted_tables):
        for i in range(len(sorted_tables)):
            for j in range(i + 1, len(sorted_tables)):
                table_k = sorted_tables[i]
                table_l = sorted_tables[j]
                query = f"""
                SELECT DISTINCT A
                FROM {table_l}
                WHERE A NOT IN (
                    SELECT DISTINCT A
                    FROM {table_k}
                )
                """
                self.cursor.execute(query)
                results = self.cursor.fetchall()
                for row in results:
                    print(row[0])

    def __del__(self):
        self.cursor.close()
        self.conn.close()

