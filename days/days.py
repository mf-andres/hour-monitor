from datetime import date
from typing import Dict

from data_source.data_source import DataSource
from data_source.data_source_factory import DataSourceFactory
from days.day import Day


class Days:
    def __init__(self):
        self.data_source: DataSource = DataSourceFactory.create()
        self.days: Dict[date, Day] = self.data_source.fetch()

    def day_exists(self, day_date: date):
        return day_date in self.days

    def get_day(self, day_date):
        return self.days[day_date]

    def add_day(self, new_day: Day):
        self.days[new_day.day_date] = new_day
        self.commit()

    def update_day(self, day_date: date, updated_day: Day):
        day_to_update = self.get_day(day_date)
        day_to_update.update(updated_day)
        self.commit()
        pass

    def remove_day(self, day_date):
        self.days.pop(day_date)
        self.commit()

    def commit(self):
        self.data_source.commit(self.days)
