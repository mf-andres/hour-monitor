import os
from datetime import date, timedelta

from hour_monitor.days.day import Day
from hour_monitor.utils import Utils


class TestUtils:
    @staticmethod
    def clear_datafile(datafile_path: str):
        if os.path.exists(datafile_path):
            os.remove(datafile_path)

    @staticmethod
    def create_today_and_tomorrow_dictionary():
        entry_hour = Utils.to_time("8:00")
        exit_hour = Utils.to_time("18:00")
        today = Day(date.today(), entry_hour, exit_hour)
        tomorrow = Day(date.today() + timedelta(days=1), entry_hour, exit_hour)
        days = dict()
        days[today.day_date] = today
        days[tomorrow.day_date] = tomorrow
        return days
