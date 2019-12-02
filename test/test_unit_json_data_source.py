import json
import os

import pytest

from data_source.json_data_source import JsonDataSource
from test.test_config import TestConfig
from test.test_utils import TestUtils


class TestUnitJsonDatasource:
    @pytest.fixture(scope="function")
    def set_and_restore_data_dir(self):
        TestUtils.clear_datafile(TestConfig.DATAFILE_PATH)
        yield
        TestUtils.clear_datafile(TestConfig.DATAFILE_PATH)

    def test_commit_two_days(self, set_and_restore_data_dir):
        days = TestUtils.create_today_and_tomorrow_dictionary()
        json_data_source = JsonDataSource()
        json_data_source.commit(days)

        assert os.path.exists(TestConfig.DATAFILE_PATH)

        with open(TestConfig.DATAFILE_PATH, "r") as json_file:
            days_data = json.load(json_file)

        assert len(days_data) == 2

        for day in days_data.items():
            assert day is not None
