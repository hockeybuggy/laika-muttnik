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
        if "LIST" in message:
             reply = "UGH, DON'T WANNA, SADNESS, NIGHT, HAI"
        elif "UGH" in message:
             reply = "http://49.media.tumblr.com/tumblr_l61wni9Xbi1qcwsd8o1_250.gif"
        elif "DON'T WANNA" in message:
             reply = "http://49.media.tumblr.com/tumblr_l61wni9Xbi1qcwsd8o1_250.gif"
        elif "SADNESS" in message:
             reply = "http://49.media.tumblr.com/tumblr_luqra3t7R21qcwsd8o1_r1_500.gif"
        elif "NIGHT" in message:
             reply = "http://45.media.tumblr.com/tumblr_luhngj9X5H1qcwsd8o1_500.gif"
        elif "HAI" in message:
             reply = "http://49.media.tumblr.com/tumblr_l61wkkxLnG1qcwsd8o1_250.gif"
        else:
            reply = "NO SPEEKY HUMAN"
        self.send_to_channel(channel, reply)


if __name__ == "__main__":
    laika = Laika()
    print("Username:", laika.user_name)
    print("ID:", laika.user_id)
    laika.listen()
