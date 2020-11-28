from slack_bolt import App
from private.information import *

app = App(
    token=OAUTH_TOKEN,
    signing_secret=SIGNING_SECRET
)


@app.command("/echo")
def repeat_text(ack, say, command):
    # Acknowledge command request
    ack()
    say(f"{command['text']}")


if __name__ == '__main__':
    app.start(port=3000)
