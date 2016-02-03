#!/usr/bin/env python

import random
import settings
import slackbot

replies = ['woof', 'woof', 'bark', 'woof woof', 'https://youtu.be/AOAtz8xWM0w']


class Laika(slackbot.SlackBot):
    def __init__(self):
        super().__init__(settings.SLACK_TOKEN)
        self.start()

    def process_mention(self, channel, message):
        print("I WAS MENTIONED")  # Send 'woof' to channel
        reply = random.choice(replies)
        self.send_to_channel(channel, reply)


if __name__ == "__main__":
    laika = Laika()
    print("Username:", laika.user_name)
    print("ID:", laika.user_id)
    laika.listen()
