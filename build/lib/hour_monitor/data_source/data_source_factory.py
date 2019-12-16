from hour_monitor.data_source.data_source import DataSource
from hour_monitor.data_source.json_data_source import JsonDataSource


class DataSourceFactory:
    @staticmethod
    def create() -> DataSource:
        return JsonDataSource()
