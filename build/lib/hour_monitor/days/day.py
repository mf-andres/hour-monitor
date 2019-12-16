from datetime import date, time, datetime

from hour_monitor.utils import Utils
from hour_monitor.config import Config


class Day:
    day_date_attribute_name = "day_date"
    entry_hour_attribute_name = "entry_hour"
    exit_hour_attribute_name = "exit_hour"

    def __init__(self, day_date: date,  entry_hour: time = None, exit_hour: time = None):
        self.day_date = day_date
        self.entry_hour = entry_hour
        self.exit_hour = exit_hour

    def get_daily_hours(self):
        daily_seconds = self.get_daily_seconds()
        daily_hours = daily_seconds / Config.SECONDS_HOUR - Config.LUNCH_BREAK
        return daily_hours

    def get_daily_seconds(self):
        daily_seconds_timedelta = Day.__to_datetime(self.exit_hour) - Day.__to_datetime(self.entry_hour)
        daily_seconds = daily_seconds_timedelta.seconds
        return daily_seconds

    @staticmethod
    def __to_datetime(hour: time) -> datetime:
        return datetime.combine(date.today(), hour)

    def update(self, updated_day: "Day"):
        if updated_day.day_date is not None:
            self.day_date = updated_day.day_date
        if updated_day.entry_hour is not None:
            self.entry_hour = updated_day.entry_hour
        if updated_day.exit_hour is not None:
            self.exit_hour = updated_day.exit_hour

    def to_json_dict(self):
        json_writable_dict = dict()
        json_writable_dict[self.day_date_attribute_name] = Utils.day_date_to_string(self.day_date)
        if self.entry_hour is not None:
            json_writable_dict[self.entry_hour_attribute_name] = Utils.hour_to_string(self.entry_hour)
        if self.exit_hour is not None:
            json_writable_dict[self.exit_hour_attribute_name] = Utils.hour_to_string(self.exit_hour)
        return json_writable_dict

    @staticmethod
    def create_from_json_dict(json_dict):
        day_date = Utils.to_date(json_dict[Day.day_date_attribute_name])
        if Day.entry_hour_attribute_name in json_dict.keys():  # todo refactor conditionals?
            entry_hour = Utils.to_time(json_dict[Day.entry_hour_attribute_name])
        else:
            entry_hour = None
        if Day.exit_hour_attribute_name in json_dict.keys():
            exit_hour = Utils.to_time(json_dict[Day.exit_hour_attribute_name])
        else:
            exit_hour = None
        return Day(day_date, entry_hour, exit_hour)
