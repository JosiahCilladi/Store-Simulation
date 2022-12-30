# System
import os
import json

# requests
import requests

# time
from time import *
from datetime import datetime, timedelta
from services.lightspeed.lightspeed_r.endpoints import *

# Utilty
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

# Environment Varibales 
client_secret = os.environ.get("CLIENT_SECRET")
client_id=os.environ.get("CLIENT_ID")
refresh_token = os.environ.get("REFRESH_TOKEN")


# today = datetime.now()
# print("Today's date:", today)

expires_time = datetime.now()


# Check Access Token Experation Date and Refersh 
def get_headers():
    # expires_timestamp = os.environ.get("EXPIRES_TIMESTAMP")
    
    # print("expires_time",expires_time)
    # if expires_time:
    #     pass
    # else:
    #     Get_New_Access_Token(client_id, client_secret, refresh_token)


    # expires_timestamp = datetime.strptime(expires_timestamp, '%y-%m-%d %H:%M:%S.%f')
    
    print("expires_in", os.environ.get("EXPIRES_IN"))
    today = datetime.now()
    print("today", today)
    print("expires_time", expires_time)
    if today >= expires_time:
        Get_New_Access_Token(client_id, client_secret, refresh_token)
    

    if os.environ.get("ACCESS_TOKEN"):
        pass
    else:
        Get_New_Access_Token(client_id, client_secret, refresh_token)
        print("access_token", os.environ.get("ACCESS_TOKEN"))


    # Add Access Tocken to the Header 
    headers = {"Authorization": "Bearer {0}".format(
        os.environ.get("ACCESS_TOKEN"))}
   
    


    return headers




def send_request(typ,url,payload=None):
    tries = 4
    
    
    # try: Execpt Error Handling
    
    # headers = get_headers()
    for x in range(tries):
        print("tries #", x)
        try:
            
            check_rate_limit(typ)
            headers = get_headers()
            if typ == "GET":
                responce = requests.request(typ, url, headers=headers)
                print("Response Code", responce.status_code)
            else:
                payload = json.dumps(payload)
                responce = requests.request(typ, url, headers=headers, data=payload)
                print("Response Code", responce.status_code)

             
        except requests.exceptions.HTTPError as err:
            print("***************************ERROR:", responce.text)
            if err.response.status_code == 401:
                print("******ERROR*******", err.response.status_code)
                Get_New_Access_Token(client_id, client_secret, refresh_token)
            elif err.response.status_code == 422:
                print("******ERROR*******", err.response.status_code)
            
        if x == tries:
            break


        # print(responce.text)
        bucket_limit = responce.headers["x-ls-api-bucket-level"]
        drip_rate = responce.headers["x-ls-api-drip-rate"]
        os.environ["BUCKET_LIMIT"] = str(bucket_limit)
        os.environ["DRIP_RATE"] = str(drip_rate)
        print("bucket_limit", bucket_limit)
        print("drip_rate", drip_rate)
        responce = json.loads(responce.text)
        return responce
   

    return False
    

    
def check_rate_limit(typ):
    bucket_limit = os.environ.get("BUCKET_LIMIT")
    drip_rate = os.environ.get("DRIP_RATE")
    if bucket_limit:
        pass
    else:
        bucket_limit = "1/60"

    if drip_rate:
        pass
    else:
        drip_rate = 1
    print("bucket_limit", bucket_limit)
    bucket_limit = bucket_limit.split("/")
    bucket_size = float(bucket_limit[1])
    bucket_level = float(bucket_limit[0])
    bucket_remaining = bucket_size - bucket_level

    print("bucket", bucket_size, bucket_level)
    cost = 10

    if typ == "POST" or typ == "PUT" or typ == "DELETE":
        cost = 10
    elif typ == "GET":
        cost = 1

    print("COST", cost)

    print(typ,bucket_limit,drip_rate)

    if bucket_remaining > cost:
        pass
    else:
        wait_time = (cost - bucket_remaining) / float(drip_rate)
        print("waiting", wait_time)
        sleep(wait_time)

    
    
    return




def Get_New_Access_Token(client_id, client_secret, rt):
    global expires_time
    payload = {
        'refresh_token': rt,
        'client_secret': client_secret,
        'client_id': client_id,
        'grant_type': 'refresh_token',
    }
    responce = requests.post(
        'https://cloud.lightspeedapp.com/oauth/access_token.php', data=payload).json()

    access_token = responce['access_token']
    expires_in = responce['expires_in']
    today = datetime.now()
    expires_time = today
    print("access_token = ", access_token)
    print("expires_in", expires_in)
    print("expires_time", expires_time)
    os.environ["ACCESS_TOKEN"] = str(access_token)
    os.environ["EXPIRES_IN"] = str(expires_in)
    seconds = int(expires_in)
    expires_time = expires_time + timedelta(seconds=seconds)
    # os.environ["EXPIRES_TIMESTAMP"] = str(expires_time)
    


    return 



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


# check_rate_limit("POST")

# Get_New_Access_Token(client_id, client_secret, refresh_token)
