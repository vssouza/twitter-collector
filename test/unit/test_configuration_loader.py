from unittest import TestCase
from config import ConfigurationLoader, ConfigUtil
import os


class TestConfigurationLoader(TestCase):

    def setUp(self):
        self.config_file_path = os.path.dirname(__file__)
        self.config_file_path = os.path.join(self.config_file_path, "test_" + ConfigUtil.CONFIG_FILENAME)
        self.config = ConfigurationLoader(self.config_file_path)

    def test_load_log_config(self):
        logs = self.config.get_logs_config()
        self.assertEquals(logs[0]["name"], "test-console-log")

    def test_load_database_config(self):
        database = self.config.get_database_config()
        self.assertEquals(database["name"], "mongodb")

    def test_load_mq_config(self):
        mq = self.config.get_mq_config()
        self.assertEquals(mq["name"], "rabbit-server")

    def test_not_defined_property(self):
        twitter = self.config.get_twitter_config()
        self.assertEquals(twitter, None)
