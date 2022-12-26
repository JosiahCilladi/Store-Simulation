# System
import os
import json

# requests
import requests

# time
from time import *
import datetime

# Utilty
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

# Environment Varibales 
client_secret = os.environ.get("CLIENT_SECRET")
client_id=os.environ.get("CLIENT_ID")
refresh_token = os.environ.get("REFRESH_TOKEN")

access_token = ""
header = ""
accountID = ""
expires_in = ""
my_timer = ""
Bucket_Limit = 0/60
Drip_Rate = float(00.00)


class LightSpeed_API_Calls:
    def __init__(self):
        print("Address of self = ", id(self))
    

    def Get_New_Access_Token(self, client_id, client_secret, rt):
        # print(client_id)
        # print(client_secret)
        # print(rt)
        global today
        today = datetime.datetime.now()
        print("Today's date:", today)

        payload = {
            'refresh_token': rt,
            'client_secret': client_secret,
            'client_id': client_id,
            'grant_type': 'refresh_token',
        }
        at = requests.post(
            'https://cloud.lightspeedapp.com/oauth/access_token.php', data=payload).json()

        # print()
        # print("Lightspeed Responce")
        # print(at)

        global access_token

        access_token = at['access_token']
        global expires_in
        expires_in = at['expires_in']
        expires_in = int(expires_in)

        print()
        print("access_token = ", access_token)
        print("expires_in", expires_in)

        global header
        header = {"Authorization": "Bearer {0}".format(access_token)}
        url = 'https://api.lightspeedapp.com/API/Account.json'

        print("HEADER = ", header)
        print()

        responce = requests.get(url=url, headers=header)

        global Bucket_Limit
        global Drip_Rate

        #! **** **** ****
        print("********************")
        print()
        Bucket_Limit = responce.headers["x-ls-api-bucket-level"]
        print("Bucket_Limit = ", Bucket_Limit)
        Drip_Rate = responce.headers["x-ls-api-drip-rate"]
        print("Drop_Rate =", Drip_Rate)
        # print(responce.headers)
        print()
        print("********************")
        print()
        #! **** **** ****

        at = responce.json()
        # print("ACCOUNT Status")
        # print(at)

        respnce = json.loads(responce.text)
    

        AS = (respnce['Account']['accountID'])
        global accountID
        accountID = AS
        print("LightSpeed accountID = ", AS)
        print()




    def calculateExperation():
        now = datetime.datetime.now()

        print("CALCULATE EXperation Time")
        print("now", now)
        print("expires_in", expires_in)
        print("today", today)
        timeElapst = now - today
        print("timeElapst", timeElapst)
        timeRemaining = datetime.timedelta(seconds=expires_in) - timeElapst
        print(timeRemaining)

        addSeconds = expires_in - 20
        x = today + datetime.timedelta(seconds=addSeconds)
        print("expiredTime Cal", x)

        if x <= now:
            print()
            print("REFRESHING Lightspeed Token")
            time.sleep(40)
            a = LightSpeed_API_Calls()
            a.Refresh_Auth_Token()

        else:
            print("Dont need to Refresh token yet")







    temp_Token = "acf302bcaf1d10a2e04df616b58140bab6586e51"

    def Onboard_New_Access_Token(self, client_id, client_secret, temp_Token):
        global today
        today = datetime.datetime.now()
        print("Today's date:", today)

        payload = {
            'code':  temp_Token,
            'client_secret': client_secret,
            'client_id': client_id,
            'grant_type': 'authorization_code',
        }
        at = requests.post(
            'https://cloud.lightspeedapp.com/oauth/access_token.php', data=payload).json()

        print(at)

    
    Get_New_Access_Token("x", client_id, client_secret, refresh_token)

   