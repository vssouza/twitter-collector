import json


class ConfigurationLoader:
    def __init__(self, config_file_path):
        with open(config_file_path) as json_config_file:
            self._json_config = json.load(json_config_file)

    def get_logs_config(self):
        return self._get_key_value('logs')

    def get_database_config(self):
        return self._get_key_value('database')

    def get_mq_config(self):
        return self._get_key_value('mq')

    def get_twitter_config(self):
        return self._get_key_value('twitter')

    def _get_key_value(self, key):
        if key in self._json_config:
            return self._json_config[key]
        return None
