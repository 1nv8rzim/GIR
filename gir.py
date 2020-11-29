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
    try:
        data = request.form
        text = data.get('text')
        user_id = data.get('user_id')
        channel = data.get('channel_id')
        user_name = data.get('user_name')
        try:
            name, officer = text.split(' ', 1)
            officer = officer.split(', ')
            officer = officer if len(officer) > 1 else officer[0]
        except:
            name, officer = text, None
        db = get_db()
        db.update(
            {user_id: {'name': name, 'user_name': user_name, 'officer': officer, 'channel': channel}})
        write_db(db)
        client.chat_postMessage(
            text=f'Hi {name}!\n\nYou have been updated to in the database to have name={name}, officer={officer}, and user_name={user_name}', channel=channel)
    except:
        return Response(), 400
    return Response(), 200


@app.route('/excuse', methods=['POST'])
def excuse():
    pass


@app.route('/loose-ends', methods=['POST'])
def loose_ends():
    pass


@app.route('/new-business', methods=['POST'])
def new_business():
    pass


@app.route('/jboard', methods=['POST'])
def jboard():
    pass


@app.route('/anonymous', methods=['POST'])
def anonymous():
    pass


@app.route('/event', methods=['POST'])
def _event():
    pass


@app.route('/report', methods=['POST'])
def report():
    pass


@app.route('/eboard', methods=['POST'])
def eboard():
    pass


# Run Web App
if __name__ == '__main__':
    app.run(debug=True)
