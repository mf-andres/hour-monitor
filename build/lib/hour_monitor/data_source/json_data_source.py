import json
from datetime import date
from typing import Dict

from hour_monitor.config import Config
from hour_monitor.days.day import Day
from hour_monitor.data_source.data_source import DataSource


class JsonDataSource(DataSource):
    def __init__(self):
        pass

    def commit(self, days: Dict[date, Day]) -> None:
        json_writable_days = JsonDataSource.to_json_days(days)
        with open(Config.DATAFILE_PATH, "w") as json_file:
            json.dump(json_writable_days, json_file)

    def fetch(self) -> Dict[date, Day]:
        try:
            with open(Config.DATAFILE_PATH, "r") as json_file:
                json_days = json.load(json_file)
                days_dict = JsonDataSource.to_days(json_days)
                return days_dict
        except FileNotFoundError:
            return dict()

    @staticmethod
    def to_json_days(days: Dict[date, Day]) -> Dict[str, Dict[str, str]]:
        json_days = dict()
        for day_date in days:
            json_day_to_include = days[day_date].to_json_dict()
            json_days[json_day_to_include[Day.day_date_attribute_name]] = json_day_to_include
        return json_days

    @staticmethod
    def to_days(json_days: Dict[str, Dict[str, str]]) -> Dict[date, Day]:
        days = dict()
        for day_date_string in json_days:
            day = Day.create_from_json_dict(json_days[day_date_string])
            days[day.day_date] = day
        return days
