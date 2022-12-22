App Name: Simulation
Description: Allows you to quickly create recored in the Lightspeed Test Store.

Testing URL: https://simulationcontrols.ngrok.io/simulation/events



Slack App URL:
    https://api.slack.com/apps/A04FF0X0MLH/general?

Slack Flask Totorial:
    https://python.plainenglish.io/lets-create-a-slackbot-cause-why-not-2972474bf5c1




    Slack App:
        Name: alar
        Description: Alerts and Reports

        Home:

        StoreEvents:
            - Store Opens
            - Store Closes
            - Shift Ends


        Alerts:
            Sales: [slackChannel ,Shop, Threshold, Time]
            Registers: [slackChannel ,shop, Register, Cash Value Under]
            New eCom Order: [slackChannel]
            


        Reports:
            Sales: [slackChannel, storeEvent, store]
            Register: [slackChannel, storeEvent, store, Register]
            