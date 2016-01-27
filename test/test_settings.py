import os
import unittest
import importlib


class SettingsTestCase(unittest.TestCase):
    def setUp(self):
        self._previous_env_value = os.environ.get('SLACK_TOKEN', '')
        print(self._previous_env_value)
        os.environ['SLACK_TOKEN'] = 'test-env var'

        self.settings = importlib.import_module('slackbot.settings')
        from slackbot import settings

    def tearDown(self):
        os.environ['SLACK_TOKEN'] = self._previous_env_value

    def test_token_is_loaded_from_env(self):
        self.assertEqual('test-env var', self.settings.SLACK_TOKEN)
