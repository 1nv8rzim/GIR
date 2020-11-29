from flask import Flask
from private.information import OAUTH_TOKEN, SIGNING_SECRET
import slack

client = slack.WebClient(token=OAUTH_TOKEN)

client.chat_postMessage(channel='#general', text='test')
