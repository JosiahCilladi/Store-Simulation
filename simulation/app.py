import os
import re
import json

from flask import Flask, request

#slack
from slack_sdk import WebClient
from slack_bolt import App, Say
from slack_bolt.adapter.flask import SlackRequestHandler


#files
import test_functions as TestFunctions

#utility
from dotenv import load_dotenv


load_dotenv()  # take environment variables from .env.

app = Flask(__name__) # Flask App
client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))
bolt_app=App(token=os.environ.get("SLACK_BOT_TOKEN"),
            signing_secret=os.environ.get("SLACK_SIGNING_SECRET"))



# Messages
# -------------------------------------------------------------------------------------------------------------

# @bolt_app.message(re.compile("(hi|hello|hey) simulation"))
def reply_in_thread(payload: dict):
    """ This will reply in thread instead of creating a new thread """
    response = client.chat_postMessage(channel=payload.get('channel'),
                                       thread_ts=payload.get('ts'),
                                       text=f"Hi<@{payload['user']}>")


@bolt_app.message("hello ls")
def greetings(payload: dict, say: Say):
    """ This will check all the message and pass only those which has 'hello slacky' in it """
    user = payload.get("user")
    say(f"Hi <@{user}>")


# Slash Commands
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

# Start ---------------------------------------------------------------
with open('simulation/day_simulator/block_templates/configure_simulation/day_simulator_settings.json') as f:
    startTemplateBlock = json.load(f)


@bolt_app.command("/start")
@bolt_app.action("configure_simulation_button")
def open_modal(ack, body, client):
    # Acknowledge the command request
    ack()
    # Call views_open with the built-in client
    client.views_open(
        # Pass a valid trigger_id within 3 seconds of receiving it
        trigger_id=body["trigger_id"],
        # View payload
        view=startTemplateBlock
    )


@bolt_app.command("/end")
def testLS(ack):
	ack()
	TestFunctions.testfunction()



@bolt_app.command("/createecom")
def help_command(say, ack):
    ack()
    text = {
	"blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                        				"text": "Create - eCom Order"
                   
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                        				"text": "Create A Lightspeed eCom Order."
                }
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                                "text": {
                                    "type": "plain_text",
                                      						"text": "Yes"
                                   
                                },
                        "style": "primary",
                        "value": "click_me_123",
                   					"action_id": "actionId-0"
                    },
                    {
                        "type": "button",
                                "text": {
                                    "type": "plain_text",
                                      						"text": "No"
                                   
                                },
                        "style": "danger",
                        "value": "click_me_124",
                   					"action_id": "actionId-1"
                    }
                ]
            }
	]
    }
    say(text=text)




handler = SlackRequestHandler(bolt_app)



# Events
# -------------------------------------------------------------------------------------------------------------

@ app.route("/simulation/events", methods=["POST"])
def slack_events():
    """ Declaring the route where slack will post a request """
    return handler.handle(request)


# Home Tab
# ---------------------------------------------------------

with open('simulation/home/block_templates/home/homeTemplate.json') as home:
    homeTemplate = json.load(home)

@bolt_app.event("app_home_opened")
def update_home_tab(client, event, logger):
    try:
        # Call views.publish with the built-in client
        client.views_publish(
            # Use the user ID associated with the event
            user_id=event["user"],
            # Home tabs must be enabled in your app configuration
            view=homeTemplate
            
        )
    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3002, debug=True)
