# system
import os
import json

#Server
from flask import Flask, request

# slack
from slack_sdk import WebClient
from slack_bolt import App, Say
from slack_bolt.adapter.flask import SlackRequestHandler

# utility
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.


# files
from api.api import api_blueprint
import test_functions as TestFunctions
from day_simulator.day_simulator import  *
from services.lightspeed.lightspeed_r.endpoints import *


# Slack OAuth
# -------------------------------------------------------------------------------------------------------------



# Start Flask and Slack Bolt apps
# -------------------------------------------------------------------------------------------------------------
app = Flask(__name__) # Flask App
client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))
bolt_app=App(token=os.environ.get("SLACK_BOT_TOKEN"),
            signing_secret=os.environ.get("SLACK_SIGNING_SECRET"))



# Messages
# -------------------------------------------------------------------------------------------------------------

@bolt_app.message("hello ls")
def greetings(payload: dict, say: Say):
    """ This will check all the message and pass only those which has 'hello slacky' in it """
    user = payload.get("user")
    say(f"Hi <@{user}>") 


# Slash Commands
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------


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


@bolt_app.action("open_register")
def open_reg(ack):
    # Acknowledge the command request
    ack()
    # Call views_open with the built-in client
    open_register()


@bolt_app.action("close_register")
def close_reg(ack):
    # Acknowledge the command request
    ack()
    # Call views_open with the built-in client
    close_register()
    

@bolt_app.action("create_sale")
def create_sales(ack):
    # Acknowledge the command request
    ack()
    # Call views_open with the built-in client
    create_sale()
    

@bolt_app.action("create_ecom_sale")
def create_ecom_sales(ack):
    # Acknowledge the command request
    ack()
    # Call views_open with the built-in client
    
    create_ecom_sale()
    

@bolt_app.action("stop_day_simulation")
def stop_day_simulation(ack):
    # Acknowledge the command request
    ack()
    # Call views_open with the built-in client
    stop_day_sim()





@bolt_app.view("view_1")
def handle_day_simulation_config_sumbit(ack, view):
    ack()
    
    input_data = view["state"]["values"]
  

    
    get_day_simulation_config(input_data)



@bolt_app.command("/end")
def testLS(ack):
	ack()
	TestFunctions.testfunction()



# Events
# -------------------------------------------------------------------------------------------------------------
handler = SlackRequestHandler(bolt_app)

@ app.route("/simulation/events", methods=["POST"])
def slack_events():
    """ Declaring the route where slack will post a request """
    return handler.handle(request)



# Home Tab
# ---------------------------------------------------------
with open('simulation/home/block_templates/home/homeTemplate.json') as home:
    homeTemplate = json.load(home)


@bolt_app.view("view_1")
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



# Simulation API Flask Blueprint
# -------------------------------------------------------------------------------------------------------------
app.register_blueprint(api_blueprint)





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3002, debug=True)
