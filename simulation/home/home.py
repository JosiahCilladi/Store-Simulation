# set up Flask Blueprint

from flask import Blueprint
import json



with open('simulation/home/block_templates/home/homeTemplate.json') as home:
    homeTemplate = json.load(home)


def construc_blueprint(slack_event):
    home_blueprint = Blueprint('home_blueprint', __name__)


    @home_blueprint.slack_events("app_home_opened")
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
