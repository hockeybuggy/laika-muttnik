from __future__ import print_function
import unittest
try:
    from unittest.mock import Mock  # Python 3 import
except:
    from mock import Mock  # Python 2 import

from slackbot.slackbot import SlackBot


class SlackBotTestCase(unittest.TestCase):
    def setUp(self):
        self.token = 'xoxb-00000000000-ddddddddddddddddddddddddd'
        self.user_id = 'U0MMM0MM'
        self.client_mock = Mock()
        self.subject = SlackBot(self.token, slack_client=self.client_mock)
        self.subject.slack.server.login_data = {'self': {'id': self.user_id}}
        self.subject.noop = Mock()

    def test_start(self):
        self.assertFalse(self.subject.slack.rtm_connect.called)
        self.assertIsNone(self.subject.user_id)
        self.subject.start()
        self.assertTrue(self.subject.slack.rtm_connect.called)
        self.assertEqual(self.subject.user_id, self.user_id)

    def test_user_name(self):
        self.subject.slack.server.username = "TEST"
        name = self.subject.user_name
        self.assertEqual(name, "TEST")

    def test_is_mention(self):
        self.subject.user_id = self.user_id
        instr_expected = [
            ("U0MMM0MM", True),
            ("U0MMM0MM Speak", True),
            ("Speak U0MMM0MM ", True),
            ("<@U0MMM0MM>", True),
            ("<@U0MMM0MM> Speak", True),
            ("", False),
            ("not here", False),
            ]

        for instr, expected in instr_expected:
            self.assertEqual(self.subject.is_mention(instr), expected, instr)

    def test_listen(self):
        pass # TODO

    def test_process_event_message(self):
        event = dict(type='message', channel='chan', text='text')
        self.subject.process_message = Mock()
        self.subject.user_id = "TEST"

        self.subject.process_event(event)

        self.subject.process_message.assert_called_with('chan', 'text')

    def test_process_event_mention(self):
        event = dict(type='message', channel='chan', text='Hello @TEST')
        self.subject.process_mention = Mock()
        self.subject.user_id = "TEST"

        self.subject.process_event(event)

        self.subject.process_mention.assert_called_with('chan', 'Hello @TEST')

    def test_process_event_bad_event(self):
        event = dict(type='weird type', channel='chan')

        with self.assertRaises(NotImplementedError):
            self.subject.process_event(event)

    def test_process_message(self):
        '''
        This defined in the subclasses
        '''
        self.subject.process_message('chan', 'text')
        self.assertTrue(self.subject.noop.called)

    def test_process_mention(self):
        '''
        This defined in the subclasses
        '''
        self.subject.process_mention('chan', 'text')
        self.assertTrue(self.subject.noop.called)

    def test_process_user_typing(self):
        self.subject.process_user_typing('chan', 'text')
        self.assertTrue(self.subject.noop.called)

    def test_process_hello(self):
        self.subject.process_hello()
        self.assertTrue(self.subject.noop.called)

    def test_process_reconnect_url(self):
        self.subject.process_reconnect_url()
        self.assertTrue(self.subject.noop.called)

    def test_process_presence_change(self):
        self.subject.process_presence_change()
        self.assertTrue(self.subject.noop.called)

    def test_process_file_public(self):
        self.subject.process_file_public()
        self.assertTrue(self.subject.noop.called)

    def test_process_file_shared(self):
        self.subject.process_file_shared()
        self.assertTrue(self.subject.noop.called)

    def test_send_to_channel(self):
        self.assertFalse(self.subject.slack.rtm_connect.called)

        self.subject.send_to_channel('channel', 'message')

        self.subject.slack.rtm_send_message.assert_called_with('channel', 'message')


if __name__ == '__main__':
    unittest.main()
