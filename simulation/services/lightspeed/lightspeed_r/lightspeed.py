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
# access_token = os.environ.get("ACCESS_TOKEN")

# access_token = ""
header = ""
accountID = ""
expires_in = ""
my_timer = ""
Bucket_Limit = 0/60
Drip_Rate = float(00.00)



def get_headers():

    if os.environ.get("ACCESS_TOKEN"):
        pass
    else:
        Get_New_Access_Token(client_id, client_secret, refresh_token)
        print("access_token", os.environ.get("ACCESS_TOKEN"))



    headers = {"Authorization": "Bearer {0}".format(
        os.environ.get("ACCESS_TOKEN"))}
    print("Check Responce")
    


    return headers




def send_request(typ,url,payload=None):
    check_rate_limit(typ)

    headers = get_headers()
    
    
    # try: Execpt Error Handling
    
    try:
        if typ == "GET":
            responce = requests.request(typ, url, headers=headers)
        else:
            payload = json.dumps(payload)
            responce = requests.request(typ, url, headers=headers, data=payload)
    except:
        print("***************************ERROR:", responce.text)
        pass




    print(responce.text)
    bucket_limit = responce.headers["x-ls-api-bucket-level"]
    drip_rate = responce.headers["x-ls-api-drip-rate"]
    os.environ["BUCKET_LIMIT"] = str(bucket_limit)
    os.environ["DRIP_RATE"] = str(drip_rate)
    print("bucket_limit", bucket_limit)
    print("drip_rate", drip_rate)
    responce = json.loads(responce.text)
    return responce

    
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
        wait_time = (cost - bucket_remaining) / int(drip_rate)
        print("waiting", wait_time)
        sleep(wait_time)
    
    return




def Get_New_Access_Token(client_id, client_secret, rt):

    today = datetime.datetime.now()
    print("Today's date:", today)

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
    print("access_token = ", access_token)
    print("expires_in", expires_in)
    os.environ["ACCESS_TOKEN"] = str(access_token)
    os.environ["EXPIRES_IN"] = str(expires_in)

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
