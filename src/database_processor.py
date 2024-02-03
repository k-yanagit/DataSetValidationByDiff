from abc import ABC, abstractmethod

class DatabaseProcessor(ABC):
    @abstractmethod
    def get_table_names(self):
        pass

    @abstractmethod
    def get_unique_count(self, table):
        pass

    @abstractmethod
    def sort_and_compare(self, sorted_tables):
        pass

    def process_tables(self):
        table_names = self.get_table_names()
        table_counts = {table: self.get_unique_count(table) for table in table_names}
        sorted_tables = sorted(table_counts, key=table_counts.get, reverse=True)
        self.sort_and_compare(sorted_tables)
