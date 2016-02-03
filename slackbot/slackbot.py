import re
import time
from slackclient import SlackClient


class SlackBot(object):
    def __init__(self, token, slack_client=SlackClient):
        self.slack = slack_client(token)
        self.user_id = None
        self.user_id_re = None

    def start(self):
        self.slack.rtm_connect()
        self.user_id = self.slack.server.login_data['self']['id']

    @property
    def user_name(self):
        return self.slack.server.username

    def is_mention(self, text):
        if not self.user_id_re:
            self.user_id_re = re.compile(r'.*{}.*'.format(self.user_id))
        result = self.user_id_re.match(text)
        if result:
            return True
        return False

    def listen(self):
        # TODO yield from the stream
        while True:
            events = self.slack.rtm_read()
            for event in events:
                self.process_event(event)
            time.sleep(1)

    def process_event(self, event):
        event_type = event.get('type')
        if not event_type:
            print(event) # TODO wat?
            self.process_type_free_event()
        elif event_type == 'message':
            if self.is_mention(event.get('text', '')):
                self.process_mention(event['channel'], event.get('text', ''))
            else:
                self.process_message(event['channel'], event.get('text', ''))
        elif event_type == 'user_typing':
            self.process_user_typing(event['channel'], event['user'])
        elif event_type == 'hello':
            self.process_hello()
        elif event_type == 'reconnect_url':
            self.process_reconnect_url()
        elif event_type == 'presence_change':
            self.process_presence_change()
        elif event_type == 'file_public':
            self.process_file_public()
        elif event_type == 'file_shared':
            self.process_file_shared()
        elif event_type == 'file_changed':
            self.process_file_changed()
        elif event_type == 'channel_joined':
            self.process_channel_joined()
        elif event_type == 'channel_created':
            self.process_channel_created()
        elif event_type == 'emoji_changed':
            self.process_emoji_changed()
        else:
            raise NotImplementedError("Unrecognised event type: {}".format(event_type))

    def process_type_free_event(self):
        self.noop()

    def process_message(self, channel, message):
        self.noop()

    def process_mention(self, channel, message):
        self.noop()

    def process_hello(self):
        self.noop()

    def process_reconnect_url(self):
        self.noop()

    def process_user_typing(self, channel, user):
        self.noop()

    def process_presence_change(self):
        self.noop()

    def process_file_public(self):
        self.noop()

    def process_file_shared(self):
        self.noop()

    def process_file_changed(self):
        self.noop()

    def process_channel_created(self):
        self.noop()

    def process_channel_joined(self):
        self.noop()

    def process_emoji_changed(self):
        self.noop()

    def noop(self):
        '''
        This method is the bot doing nothing
        '''
        pass

    def send_to_channel(self, channel, message):
        self.slack.rtm_send_message(channel, message)
