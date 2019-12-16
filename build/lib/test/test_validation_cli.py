import pytest
from click.testing import CliRunner

from hour_monitor.cli import main
from test_config import TestConfig
from test.test_utils import TestUtils


class TestValidationCli:
    day_date = "11/3/1996"  # It was a monday
    next_day_date = "12/3/1996"
    next_week_day_date = "18/3/1996"
    entry_hour = "9:00"
    next_entry_hour = "9:30"
    exit_hour = "17:30"  # 8 hours working day
    next_exit_hour = "18:00"

    store_entry_args = ["--store_entry", "--day", day_date,  "--hour", entry_hour]
    store_exit_args = ["--store_exit", "--day", day_date,  "--hour", exit_hour]
    upd_entry_args = ["--upd_entry", "--day", day_date, "--hour", next_entry_hour]
    upd_exit_args = ["--upd_exit", "--day", day_date, "--hour", next_exit_hour]
    look_day_args = ["--look_day", "--day", day_date]
    look_week_args = ["--look_week", "--day", day_date]
    look_month_args = ["--look_month", "--day", day_date]
    rem_day_args = ["--rem_day", "--day", day_date]
    rem_week_args = ["--rem_week", "--day", day_date]
    del_day_args = ["--del_day", "--day", day_date]

    @pytest.fixture(scope="function")  # todo refactor (one file)
    def set_and_restore_data_dir(self):
        TestUtils.clear_datafile(TestConfig.DATAFILE_PATH)
        yield
        TestUtils.clear_datafile(TestConfig.DATAFILE_PATH)

    @pytest.fixture(scope="function")
    def runner(self):
        return CliRunner()

    def test_store_entry(self, set_and_restore_data_dir, runner):
        result = runner.invoke(main, self.store_entry_args)
        assert result.exit_code == 0

    def test_store_exit(self, set_and_restore_data_dir, runner):
        result = runner.invoke(main, self.store_exit_args)
        assert result.exit_code == 0

    def test_upd_entry(self, set_and_restore_data_dir, runner):
        store_result = runner.invoke(main, self.store_entry_args)
        update_result = runner.invoke(main, self.upd_entry_args)
        assert store_result.exit_code == 0
        assert update_result.exit_code == 0

    def test_upd_exit(self, set_and_restore_data_dir, runner):
        store_result = runner.invoke(main, self.store_exit_args)
        update_result = runner.invoke(main, self.upd_exit_args)
        assert store_result.exit_code == 0
        assert update_result.exit_code == 0

    def test_look_day(self, set_and_restore_data_dir, runner):
        store_entry_result = runner.invoke(main, self.store_entry_args)
        store_exit_result = runner.invoke(main, self.store_exit_args)
        look_result = runner.invoke(main, self.look_day_args)
        assert store_entry_result.exit_code == 0
        assert store_exit_result.exit_code == 0
        assert look_result.exit_code == 0
        assert look_result.output == "entry hour:  9:00  exit hour:  17:30  daily hours: 8.0\n"

    def test_look_week(self, set_and_restore_data_dir, runner):
        store_entry_result = runner.invoke(main, self.store_entry_args)
        store_exit_result = runner.invoke(main, self.store_exit_args)
        look_result = runner.invoke(main, self.look_week_args)
        assert store_entry_result.exit_code == 0
        assert store_exit_result.exit_code == 0
        assert look_result.exit_code == 0
        assert look_result.output == "weekly hours:  8.0\n"

    def test_look_month(self, set_and_restore_data_dir, runner):
        store_entry_result = runner.invoke(main, self.store_entry_args)
        store_exit_result = runner.invoke(main, self.store_exit_args)
        look_result = runner.invoke(main, self.look_month_args)
        assert store_entry_result.exit_code == 0
        assert store_exit_result.exit_code == 0
        assert look_result.exit_code == 0
        assert look_result.output == "monthly hours:  8.0\n"

    def test_rem_day(self, set_and_restore_data_dir, runner):
        store_entry_result = runner.invoke(main, self.store_entry_args)
        store_exit_result = runner.invoke(main, self.store_exit_args)
        remaining_result = runner.invoke(main, self.rem_day_args)
        assert store_entry_result.exit_code == 0
        assert store_exit_result.exit_code == 0
        assert remaining_result.exit_code == 0
        assert remaining_result.output == "remaining hours:  0.0\n"

    def test_rem_week(self, set_and_restore_data_dir, runner):
        store_entry_result = runner.invoke(main, self.store_entry_args)
        store_exit_result = runner.invoke(main, self.store_exit_args)
        remaining_result = runner.invoke(main, self.rem_week_args)
        assert store_entry_result.exit_code == 0
        assert store_exit_result.exit_code == 0
        assert remaining_result.exit_code == 0
        assert remaining_result.output == "remaining hours:  32.0\n"

    def test_del_day(self, set_and_restore_data_dir, runner):
        store_entry_result = runner.invoke(main, self.store_entry_args)
        delete_day_result = runner.invoke(main, self.del_day_args)
        assert store_entry_result.exit_code == 0
        assert delete_day_result.exit_code == 0
