from datetime import date
from typing import Dict

from days.day import Day


class DataSource:
    def fetch(self) -> Dict[date, Day]:
        pass

    def commit(self, days: Dict[date, Day]) -> None:
        pass
