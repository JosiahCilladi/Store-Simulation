# ---------------------------------------------------------
""" Lightspeed_Command.py """
# ---------------------------------------------------------
# ---------------------------------------------------------
# Project:       FERAL_USED_Gear
# Company:       FERAL
# Auther:        Josiah Cilladi
# File Name:     Lightspeed/Lightspeed_Command.py
# Description:   Python Dictionary / Lightspeed API Converstion
# Created:       Wed Dec 30 14:31:54 2020

# """ Resources """
# ---------------------------------------------------------
#   Settings.db
# ---------------------------------------------------------
# ---------------------------------------------------------

import requests
import json
from time import *
import os
import sys
import time
import datetime
from datetime import date

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


def resource_path(relative_path):

    # Get absolute path to resource
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(
        os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)



# import threading
# from oauthlib.oauth2 import LegacyApplicationClient
# from requests_oauthlib import OAuth2Session
client_secret = os.environ.get("CLIENT_SECRET")
client_id=os.environ.get("CLIENT_ID")

# refresh_token = '743dbf0176fe575f56e50d96721b7f3b0cda9d9d' # FERAL Lightspeed Account
refresh_token = os.environ.get("REFRESH_TOKEN")
print("refresh_toaken", refresh_token)
access_token = ""
header = ""
accountID = ""
expires_in = ""
my_timer = ""
Bucket_Limit = 0/60
Drip_Rate = float(00.00)


# Test_Order = True will put all items in LS Order # 1120
# Test_Order = False will Creat New Order for each Quote upload
Test_Order = False


class LightSpeed_API_Calls:

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
        # print("ACCOUNT Status and Header")
        # print(type(respnce))
        # print(respnce)
        # print()

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
        # result = datetime.datetime.now() - datetime.timedelta(seconds=X)
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

    # def Refresh_Auth_Token(self):
    #     self.Get_New_Access_Token(client_id, client_secret, refresh_token)

    # -- Item --
    # ---------------------------------------------------
    # ---------------------------------------------------




    

    #This is used to get a Access_Token and and Refresh_Token
    # will be used to on bourd new lightspeed accounts

    # https://cloud.lightspeedapp.com/oauth/authorize.php?response_type=code&client_id=156d1bed0cc92d4ee2e704a680e2e028b77dbedd8968a783781216b7b6ce7e00&scope=employee:all

    temp_Token = "acf302bcaf1d10a2e04df616b58140bab6586e51"

    def Onboard_New_Access_Token(self, client_id, client_secret, temp_Token):
        # print(client_id)
        # print(client_secret)
        # print(rt)
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
        # print("Lightspeed Responce")
        # print(at)

      
        

    # Onboard_New_Access_Token("X", client_id, client_secret, temp_Token)
    Get_New_Access_Token("x", client_id, client_secret, refresh_token)


    