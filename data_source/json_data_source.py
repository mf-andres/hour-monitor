import json
from datetime import date
from typing import Dict

from config import Config
from days.day import Day
from data_source.data_source import DataSource


class JsonDataSource(DataSource):
    def __init__(self):
        pass

    def fetch(self) -> Dict[date, Day]:
        try:
            with open(Config.DATAFILE_PATH, "r") as json_file:
                days_data = json.load(json_file)
                return days_data
        except FileNotFoundError:
            return dict()

    def commit(self, days: Dict[date, Day]) -> None:
        json_writable_days = JsonDataSource.to_json_writable_days(days)
        with open(Config.DATAFILE_PATH, "w") as json_file:
            json.dump(json_writable_days, json_file)

    @staticmethod
    def to_json_writable_days(days: Dict[date, Day]) -> Dict[str, Dict[str, str]]:
        json_writable_days = dict()
        for day_date in days:
            json_writable_day_to_include = days[day_date].to_json_writable_dict()
            json_writable_days[json_writable_day_to_include[Day.day_date_attribute_name]] = json_writable_day_to_include
        return json_writable_days
