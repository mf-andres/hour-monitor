import pytest

from hour_monitor import HourMonitor

from test.test_config import TestConfig
from test.test_utils import TestUtils


class TestIntegration:
    day_date = "11/3/1996"  # It was a monday
    next_day_date = "12/3/1996"
    next_week_day_date = "18/3/1996"
    entry_hour = "9:00"
    next_entry_hour = "9:30"
    exit_hour = "17:30"  # 8 hours working day
    next_exit_hour = "18:00"

    @pytest.fixture(scope="function")  # todo refactor (one file)
    def set_and_restore_data_dir(self):
        TestUtils.clear_datafile(TestConfig.DATAFILE_PATH)
        yield
        TestUtils.clear_datafile(TestConfig.DATAFILE_PATH)

    @pytest.fixture("function")
    def hour_monitor(self) -> HourMonitor:
        return HourMonitor()

    def test_store_and_check_entry_hour(self, set_and_restore_data_dir, hour_monitor):
        hour_monitor.store_entry_hour(self.day_date, self.entry_hour)
        new_entry_hour = hour_monitor.check_entry_hour(self.day_date)
        assert self.entry_hour == new_entry_hour

    def test_update_entry_hour(self, set_and_restore_data_dir, hour_monitor):
        hour_monitor.store_entry_hour(self.day_date, self.entry_hour)
        old_entry_hour = hour_monitor.check_entry_hour(self.day_date)
        hour_monitor.update_entry_hour(self.day_date, self.next_entry_hour)
        checked_next_entry_hour = hour_monitor.check_entry_hour(self.day_date)
        assert self.next_entry_hour == checked_next_entry_hour
        assert old_entry_hour != checked_next_entry_hour

    def test_store_and_check_exit_hour(self, set_and_restore_data_dir, hour_monitor):
        hour_monitor.store_exit_hour(self.day_date, self.exit_hour)
        new_exit_hour = hour_monitor.check_exit_hour(self.day_date)
        assert self.exit_hour == new_exit_hour

    def test_update_exit_hour(self, set_and_restore_data_dir, hour_monitor):
        hour_monitor.store_exit_hour(self.day_date, self.exit_hour)
        old_exit_hour = hour_monitor.check_exit_hour(self.day_date)
        hour_monitor.update_exit_hour(self.day_date, self.next_exit_hour)
        checked_next_exit_hour = hour_monitor.check_exit_hour(self.day_date)
        assert self.next_exit_hour == checked_next_exit_hour
        assert old_exit_hour != checked_next_exit_hour

    def test_check_daily_hours(self, set_and_restore_data_dir, hour_monitor):
        hour_monitor.store_entry_hour(self.day_date, self.entry_hour)
        hour_monitor.store_exit_hour(self.day_date, self.exit_hour)
        daily_hours = hour_monitor.check_daily_hours(self.day_date)
        assert daily_hours == 8.5 - TestConfig.LUNCH_BREAK

    def test_check_weekly_hours(self, set_and_restore_data_dir, hour_monitor):
        hour_monitor.store_entry_hour(self.day_date, self.entry_hour)
        hour_monitor.store_exit_hour(self.day_date, self.exit_hour)
        hour_monitor.store_entry_hour(self.next_day_date, self.entry_hour)
        hour_monitor.store_exit_hour(self.next_day_date, self.exit_hour)
        weekly_hours = hour_monitor.check_weekly_hours(self.day_date)
        assert weekly_hours == (8.5 - TestConfig.LUNCH_BREAK) * 2

    def test_check_monthly_hours(self, set_and_restore_data_dir, hour_monitor):
        hour_monitor.store_entry_hour(self.day_date, self.entry_hour)
        hour_monitor.store_exit_hour(self.day_date, self.exit_hour)
        hour_monitor.store_entry_hour(self.next_week_day_date, self.entry_hour)
        hour_monitor.store_exit_hour(self.next_week_day_date, self.exit_hour)
        monthly_hours = hour_monitor.check_monthly_hours(self.day_date)
        assert monthly_hours == (8.5 - TestConfig.LUNCH_BREAK) * 2

    def test_check_remaining_daily_hours(self, set_and_restore_data_dir, hour_monitor):
        hour_monitor.store_entry_hour(self.day_date, self.entry_hour)
        hour_monitor.store_exit_hour(self.day_date, self.exit_hour)
        remaining_daily_hours = hour_monitor.check_remaining_daily_hours(self.day_date)
        assert remaining_daily_hours == 0

    def test_check_remaining_weekly_hours(self, set_and_restore_data_dir, hour_monitor):
        hour_monitor.store_entry_hour(self.day_date, self.entry_hour)
        hour_monitor.store_exit_hour(self.day_date, self.exit_hour)
        remaining_weekly_hours = hour_monitor.check_remaining_weekly_hours(self.day_date)
        assert remaining_weekly_hours == TestConfig.WEEKLY_HOURS - TestConfig.DAILY_HOURS

    def test_remove_day(self, set_and_restore_data_dir, hour_monitor):
        hour_monitor.store_entry_hour(self.day_date, self.entry_hour)
        hour_monitor.remove_day(self.day_date)
        with pytest.raises(Exception):
            hour_monitor.check_entry_hour(self.day_date)

    def test_store_and_check_entry_hour_two_sessions(self, set_and_restore_data_dir, hour_monitor):
        hour_monitor.store_entry_hour(self.day_date, self.entry_hour)
        second_hour_monitor = HourMonitor()
        new_entry_hour = second_hour_monitor.check_entry_hour(self.day_date)
        assert self.entry_hour == new_entry_hour
