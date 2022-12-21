import os
import re

from flask import Flask, request

from slack_sdk import WebClient
from slack_bolt import App, Say
from slack_bolt.adapter.flask import SlackRequestHandler

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

app = Flask(__name__) # Flask App
client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))
bolt_app=App(token=os.environ.get("SLACK_BOT_TOKEN"),
            signing_secret=os.environ.get("SLACK_SIGNING_SECRET"))



# Messages
# -----------------------------------------------------------

@bolt_app.message(re.compile("(hi|hello|hey) slacky"))
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






#Slash Commands
#-----------------------------------------------------------
@bolt_app.command("/help")
def help_command(say, ack):
    ack()
    text = {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "/Sales : Sales Report"
                }
            }
        ]
    }
    say(text=text)


@bolt_app.command("/sales")
def help_command(say, ack):
    ack()
    text = {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": """Sales Report"""
                }
            }
        ]
    }
    say(text=text)


handler = SlackRequestHandler(bolt_app)






# Events
# -----------------------------------------------------------

@ app.route("/lightspeedSlackApp/events", methods=["POST"])
def slack_events():
    """ Declaring the route where slack will post a request """
    return handler.handle(request)


@bolt_app.event("app_home_opened")
def update_home_tab(client, event, logger):
    try:
        # Call views.publish with the built-in client
        client.views_publish(
            # Use the user ID associated with the event
            user_id=event["user"],
            # Home tabs must be enabled in your app configuration
            view=
                {
	"type": "home",
	"blocks": [
		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "Alerts"
				
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "Sales"
				
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "conversations_select",
					"placeholder": {
						"type": "plain_text",
						"text": "Select a conversation"
						
					},
					"action_id": "actionId-0"
				},
				{
					"type": "channels_select",
					"placeholder": {
						"type": "plain_text",
						"text": "Select a channel"
						
					},
					"action_id": "actionId-1"
				},
				{
					"type": "users_select",
					"placeholder": {
						"type": "plain_text",
						"text": "Select a user"
						
					},
					"action_id": "actionId-2"
				},
				{
					"type": "static_select",
					"placeholder": {
						"type": "plain_text",
						"text": "Select an item"
						
					},
					"options": [
						{
							"text": {
								"type": "plain_text",
								"text": "*this is plain_text text*"
								
							},
							"value": "value-0"
						},
						{
							"text": {
								"type": "plain_text",
								"text": "*this is plain_text text*"
								
							},
							"value": "value-1"
						},
						{
							"text": {
								"type": "plain_text",
								"text": "*this is plain_text text*"
								
							},
							"value": "value-2"
						}
					],
					"action_id": "actionId-3"
				}
			]
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "Registers"
				
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "conversations_select",
					"placeholder": {
						"type": "plain_text",
						"text": "Select a conversation"
						
					},
					"action_id": "actionId-0"
				},
				{
					"type": "channels_select",
					"placeholder": {
						"type": "plain_text",
						"text": "Select a channel"
						
					},
					"action_id": "actionId-1"
				},
				{
					"type": "users_select",
					"placeholder": {
						"type": "plain_text",
						"text": "Select a user"
						
					},
					"action_id": "actionId-2"
				},
				{
					"type": "static_select",
					"placeholder": {
						"type": "plain_text",
						"text": "Select an item"
						
					},
					"options": [
						{
							"text": {
								"type": "plain_text",
								"text": "*this is plain_text text*"
								
							},
							"value": "value-0"
						},
						{
							"text": {
								"type": "plain_text",
								"text": "*this is plain_text text*"
								
							},
							"value": "value-1"
						},
						{
							"text": {
								"type": "plain_text",
								"text": "*this is plain_text text*"
								
							},
							"value": "value-2"
						}
					],
					"action_id": "actionId-3"
				}
			]
		},
		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "Reports"
				
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "Sales"
				
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "conversations_select",
					"placeholder": {
						"type": "plain_text",
						"text": "Select a conversation"
						
					},
					"action_id": "actionId-0"
				},
				{
					"type": "channels_select",
					"placeholder": {
						"type": "plain_text",
						"text": "Select a channel"
						
					},
					"action_id": "actionId-1"
				},
				{
					"type": "users_select",
					"placeholder": {
						"type": "plain_text",
						"text": "Select a user"
						
					},
					"action_id": "actionId-2"
				},
				{
					"type": "static_select",
					"placeholder": {
						"type": "plain_text",
						"text": "Select an item"
						
					},
					"options": [
						{
							"text": {
								"type": "plain_text",
								"text": "*this is plain_text text*"
								
							},
							"value": "value-0"
						},
						{
							"text": {
								"type": "plain_text",
								"text": "*this is plain_text text*"
								
							},
							"value": "value-1"
						},
						{
							"text": {
								"type": "plain_text",
								"text": "*this is plain_text text*"
								
							},
							"value": "value-2"
						}
					],
					"action_id": "actionId-3"
				}
			]
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "Register"
				
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "conversations_select",
					"placeholder": {
						"type": "plain_text",
						"text": "Select a conversation"
						
					},
					"action_id": "actionId-0"
				},
				{
					"type": "channels_select",
					"placeholder": {
						"type": "plain_text",
						"text": "Select a channel"
						
					},
					"action_id": "actionId-1"
				},
				{
					"type": "users_select",
					"placeholder": {
						"type": "plain_text",
						"text": "Select a user"
						
					},
					"action_id": "actionId-2"
				},
				{
					"type": "static_select",
					"placeholder": {
						"type": "plain_text",
						"text": "Select an item"
						
					},
					"options": [
						{
							"text": {
								"type": "plain_text",
								"text": "*this is plain_text text*",
								
							},
							"value": "value-0"
						},
						{
							"text": {
								"type": "plain_text",
								"text": "*this is plain_text text*",
								
							},
							"value": "value-1"
						},
						{
							"text": {
								"type": "plain_text",
								"text": "*this is plain_text text*",
								
							},
							"value": "value-2"
						}
					],
					"action_id": "actionId-3"
				}
			]
		}
	]
}
            
        )
    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
