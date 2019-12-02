from data_source.data_source import DataSource
from data_source.json_data_source import JsonDataSource


class DataSourceFactory:
    @staticmethod
    def create() -> DataSource:
        return JsonDataSource()
