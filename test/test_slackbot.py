import unittest
from unittest.mock import Mock

from slackbot.slackbot import SlackBot


class SlackBotTestCase(unittest.TestCase):
    def setUp(self):
        self.token = 'xoxb-00000000000-ddddddddddddddddddddddddd'
        self.client_mock = Mock()
        self.subject = SlackBot(self.token, slack_client=self.client_mock)

    def test_start(self):
        self.assertFalse(self.subject.slack.rtm_connect.called)
        self.subject.slack.server.login_data = dict(self=dict(id="U0MMM0UW"))
        self.subject.start()
        self.assertTrue(self.subject.slack.rtm_connect.called)
        self.assertEqual(self.subject.user_id, "U0MMM0UW")

    def test_user_name(self):
        self.subject.slack.server.username = "TEST"
        name = self.subject.user_name
        self.assertEqual(name, "TEST")

    def test_listen(self):
        pass

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

    def test_process_message(self):
        '''
        This defined in the subclasses
        '''
        with self.assertRaises(NotImplementedError):
            self.subject.process_message('chan', 'text')

    def test_process_mention(self):
        '''
        This defined in the subclasses
        '''
        with self.assertRaises(NotImplementedError):
            self.subject.process_mention('chan', 'text')

    def test_send_to_channel(self):
        self.assertFalse(self.subject.slack.rtm_connect.called)

        self.subject.send_to_channel('channel', 'message')

        self.subject.slack.rtm_send_message.assert_called_with('channel', 'message')


if __name__ == '__main__':
    unittest.main()
