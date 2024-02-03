from google.cloud import bigquery
from database_processor import DatabaseProcessor

class BigQueryProcessor(DatabaseProcessor):
    def __init__(self, dataset_name):
        self.client = bigquery.Client()
        self.dataset_name = dataset_name

    def get_table_names(self):
        tables = list(self.client.list_tables(self.dataset_name))
        return [table.table_id for table in tables]

    def get_unique_count(self, table):
        query = f"SELECT COUNT(DISTINCT A) as count_a FROM `{self.dataset_name}.{table}`"
        query_job = self.client.query(query)
        results = query_job.result()
        for row in results:
            return row.count_a

    def sort_and_compare(self, sorted_tables):
        for i in range(len(sorted_tables)):
            for j in range(i + 1, len(sorted_tables)):
                table_k = sorted_tables[i]
                table_l = sorted_tables[j]
                query = f"""
                SELECT DISTINCT A
                FROM `{self.dataset_name}.{table_l}`
                WHERE A NOT IN (
                    SELECT DISTINCT A
                    FROM `{self.dataset_name}.{table_k}`
                )
                """
                query_job = self.client.query(query)
                results = query_job.result()
                for row in results:
                    print(row.A)

