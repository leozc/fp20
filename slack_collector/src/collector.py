import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


def main():
    client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])

    try:
        response = client.chat_postMessage(channel='#random', text="Hello world!")
        assert response["message"]["text"] == "Hello world!"
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["ok"] is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        print(f"Got an error: {e.response['error']}")