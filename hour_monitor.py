import calendar
from datetime import date, time, timedelta
from typing import List

from config import Config
from days.day import Day
from days.days import Days
from utils import Utils


class HourMonitor:
    def __init__(self):
        self.days = Days()

    def store_entry_hour(self, day_date: str, entry_hour: str) -> None:
        day_date = Utils.to_date(day_date)
        entry_hour = Utils.to_time(entry_hour)
        day_to_store = Day(day_date, entry_hour=entry_hour)
        self.store_day(day_date, day_to_store)

    def check_entry_hour(self, day_date: str) -> str:
        day_date = Utils.to_date(day_date)
        day = self.days.get_day(day_date)
        return Utils.hour_to_string(day.entry_hour)

    def update_entry_hour(self, day_date: str, new_entry_hour: str) -> None:
        day_date = Utils.to_date(day_date)
        new_entry_hour = Utils.to_time(new_entry_hour)
        day_to_update = self.days.get_day(day_date)
        day_to_update.entry_hour = new_entry_hour
        self.days.update_day(day_date, day_to_update)

    def store_exit_hour(self, day_date: str, exit_hour: str) -> None:
        day_date = Utils.to_date(day_date)
        exit_hour = Utils.to_time(exit_hour)
        day_to_store = Day(day_date, exit_hour=exit_hour)
        self.store_day(day_date, day_to_store)

    def check_exit_hour(self, day_date: str) -> str:
        day_date = Utils.to_date(day_date)
        day = self.days.get_day(day_date)
        return Utils.hour_to_string(day.exit_hour)

    def update_exit_hour(self, day_date: str, new_exit_hour: str) -> None:
        day_date = Utils.to_date(day_date)
        new_exit_hour = Utils.to_time(new_exit_hour)
        day_to_update = self.days.get_day(day_date)
        day_to_update.exit_hour = new_exit_hour
        self.days.update_day(day_date, day_to_update)

    def store_day(self, day_date: date, day_to_store: Day) -> None:
        if self.days.day_exists(day_date):
            self.days.update_day(day_date, day_to_store)
        else:
            self.days.add_day(day_to_store)

    def check_daily_hours(self, day_date: str) -> float:
        day_date = Utils.to_date(day_date)
        day = self.days.get_day(day_date)
        return day.get_daily_hours()

    def check_weekly_hours(self, day_date: str) -> float:
        day_date = Utils.to_date(day_date)
        first_date_of_the_week = HourMonitor.get_first_date_of_the_week(day_date)
        week = self.get_week(first_date_of_the_week)
        weekly_hours = 0
        for day in week:
            weekly_hours += day.get_daily_hours()
        return weekly_hours

    @staticmethod
    def get_first_date_of_the_week(day_date: date) -> date:
        first_date_of_the_week = day_date - timedelta(days=day_date.weekday())
        return first_date_of_the_week

    def get_week(self, first_date_of_the_week: date) -> List[Day]:
        week = list()
        for i in range(7):
            weekday_date = first_date_of_the_week + timedelta(days=i)
            if self.days.day_exists(weekday_date):
                weekday_day = self.days.get_day(weekday_date)
                week.append(weekday_day)
        return week

    def check_monthly_hours(self, day_date: str) -> float:
        day_date = Utils.to_date(day_date)
        first_day_of_the_month = HourMonitor.get_first_date_of_the_month(day_date)
        weekstarts = HourMonitor.get_week_starts(first_day_of_the_month)
        monthly_hours = 0
        for weekstart in weekstarts:
            weekstart = Utils.day_date_to_string(weekstart)
            monthly_hours += self.check_weekly_hours(weekstart)
        return monthly_hours

    @staticmethod
    def get_first_date_of_the_month(day_date: date) -> date:
        return day_date.replace(day=1)

    @staticmethod
    def get_week_starts(first_day_of_the_month: date) -> List[date]:
        c = calendar.Calendar()
        for weekstart in filter(lambda d: d.weekday() == c.firstweekday,
                                c.itermonthdates(first_day_of_the_month.year, first_day_of_the_month.month)):
            yield weekstart

    def check_remaining_daily_hours(self, day_date: str) -> float:
        day_date = Utils.to_date(day_date)
        day = self.days.get_day(day_date)
        return Config.DAILY_HOURS - day.get_daily_hours()

    def check_remaining_weekly_hours(self, day_date: str) -> float:
        weekly_hours = self.check_weekly_hours(day_date)
        return Config.WEEKLY_HOURS - weekly_hours

    def remove_day(self, day_date: str) -> None:
        day_date = Utils.to_date(day_date)
        self.days.remove_day(day_date)
