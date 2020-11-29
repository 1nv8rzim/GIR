import slack
from flask import Flask, request, Response
from private.information import OAUTH_TOKEN, SIGNING_SECRET
from slackeventsapi import SlackEventAdapter

client = slack.WebClient(token=OAUTH_TOKEN)

client.chat_postMessage(channel='#general', text='test')
