from slackclient import SlackClient
from private.information import OAUTH_TOKEN
import time
import re

gir = SlackClient(OAUTH_TOKEN)

RTM_READ_DELAY = 1
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

if __name__ == '__main__':
    if gir.rtm_connect(with_team_state=False):
        print("GIR has connected and is running!")
        starterbot_id = gir.api_call("auth.test")["user.id"]
        while True:
            command, channel = parse_command(command)
