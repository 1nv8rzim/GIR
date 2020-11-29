import slack
from flask import Flask, request, Response
from private.information import OAUTH_TOKEN, SIGNING_SECRET
from slackeventsapi import SlackEventAdapter
import json

# Intializing Flask Web App
app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(SIGNING_SECRET, '/slack/events', app)

# Initializing Slack Web Client
client = slack.WebClient(token=OAUTH_TOKEN)

# Global Variables
BOT_ID = client.api_call('auth.test')['user_id']
OFFICERS = 'officers.json'

# Functions


def get_db():
    with open(OFFICERS, 'r') as officers:
        return json.load(officers)


def write_db(db):
    with open(OFFICERS, 'w') as officers:
        json.dump(db, officers)


# Event Handlers
@app.route('/gir', methods=['POST'])
def gir():
    data = request.form
    text = data.get('text')
    user_id = data.get('user_id')
    print(data)
    return Response(), 200


# Run Web App
if __name__ == '__main__':
    app.run(debug=True)
