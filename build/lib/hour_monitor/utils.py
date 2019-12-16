from datetime import datetime, time, date


class Utils:
    @staticmethod
    def to_time(hour: str) -> time:
        return datetime.strptime(hour, '%H:%M').time()

    @staticmethod
    def to_date(day_date: str) -> date:
        return datetime.strptime(day_date, '%d/%m/%Y').date()

    @staticmethod
    def hour_to_string(hour: time) -> str:
        return hour.strftime('%-H:%M')

    @staticmethod
    def day_date_to_string(day_date: date) -> str:
        return day_date.strftime('%d/%m/%Y')
