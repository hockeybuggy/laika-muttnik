import time
from slackclient import SlackClient


class SlackBot(object):
    def __init__(self, token, slack_client=SlackClient):
        self.slack = slack_client(token)
        self.user_id = None

    def start(self):
        self.slack.rtm_connect()
        self.user_id = self.slack.server.login_data['self']['id']

    @property
    def user_name(self):
        return self.slack.server.username

    def listen(self):
        # TODO yield from the stream
        while True:
            events = self.slack.rtm_read()
            for event in events:
                self.process_event(event)
            time.sleep(1)

    def process_event(self, event):
        event_type = event.get('type')
        if event_type == 'message':
            if self.user_id in event.get('text', ''):  # TODO how inefficient is this?
                self.process_mention(event['channel'], event.get('text', ''))
            else:
                self.process_message(event['channel'], event.get('text', ''))
        if event_type == 'user_typing':
            self.process_user_typing(event['channel'], event['user'])
        else:
            print(event)

    def process_message(self, channel, message):
        raise NotImplementedError

    def process_mention(self, channel, message):
        raise NotImplementedError

    def process_user_typing(self, channel, user):
        pass  # No op by default

    def send_to_channel(self, channel, message):
        self.slack.rtm_send_message(channel, message)
