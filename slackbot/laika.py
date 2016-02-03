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
        if "DON'T WANNA" in message:
             reply = "http://gph.is/1aRCF94"
        if "UGH" in message:
             reply = "http://49.media.tumblr.com/tumblr_l61wni9Xbi1qcwsd8o1_250.gif "
        else:
            reply = "NO SPEEKY HUMAN"
        self.send_to_channel(channel, reply)


if __name__ == "__main__":
    laika = Laika()
    print("Username:", laika.user_name)
    print("ID:", laika.user_id)
    laika.listen()
