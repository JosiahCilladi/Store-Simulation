# Files
# from services.lightspeed.lightspeed_r import oauth
import os
import requests
from datetime import datetime, timezone
import json

from dotenv import load_dotenv
load_dotenv()

from services.lightspeed.lightspeed_r.lightspeed import *

def account_info():
    print("account_id")
    url = 'https://api.lightspeedapp.com/API/Account.json'

    response = send_request("GET", url)
    print(response.text)

def open_register():
    print("open_register")

    

    url = "https://api.lightspeedapp.com/API/V3/Account/295355/Register/1/open.json"


    payload = "{\n      \"amount\": \"1000\",\n    \t\"notes\": \"Register opened via API\",\n    \t\"employeeID\": \"1\",\n    \t\"paymentTypeID\": \"1\"\n    }"
    
    # response = requests.request("POST", url, headers=headers, data=payload)
    response = send_request("POST", url, payload)

    print(response.text)



def close_register():
    print("close_register")

    url = "https://api.lightspeedapp.com/API/V3/Account/295355/Register/1/close.json"


    payload = "{\n        \"notes\": \"Closed Register via the API\",\n        \"openTime\": \"2021-04-06\",\n        \"closeEmployeeID\": \"1\"\n    }"
    
    response = send_request("POST", url, payload)

    print(response.text)



def create_sale():
    print("create_sale")


    url = "https://api.lightspeedapp.com/API/V3/Account/295355/Sale.json"
    today = datetime.datetime.now(datetime.timezone.utc)
    now = str(today.isoformat())
    print(now)
    data = [{
        "discountPercent": "0",
        "completed": "true",
        "archived": "false",
        "voided": "false",
        "enablePromotions": "true",
        "isTaxInclusive": "false",
        "completeTime": now,
        "referenceNumber": "",
        "receiptPreference": "printed",
        "customerID": "0",
        "discountID": "0",
        "employeeID": "1",
        "tipEmployeeID": "0",
        "quoteID": "0",
        "registerID": "1",
        "shipToID": "0",
        "shopID": "1",
        "taxCategoryID": "0"
    }]
    payload = json.dumps(data)

    response = send_request("POST", url, payload)

    print(response.text)
        





def create_ecom_sale():
    print("create_ecom_sale")
    url = "https://api.lightspeedapp.com/API/V3/Account/295355/Sale.json"
    today = datetime.datetime.now(datetime.timezone.utc)
    now = str(today.isoformat())
    print(now)
    data = [{
        "discountPercent": "0",
        "completed": "true",
        "archived": "false",
        "voided": "false",
        "enablePromotions": "true",
        "isTaxInclusive": "false",
        "completeTime": now,
        "referenceNumber": "",
        "receiptPreference": "printed",
        "customerID": "0",
        "discountID": "0",
        "employeeID": "1",
        "tipEmployeeID": "0",
        "quoteID": "0",
        "registerID": "1",
        "shipToID": "0",
        "shopID": "1",
        "taxCategoryID": "0"
    }]
    payload = json.dumps(data)

    response = send_request("POST", url, payload)

    print(response.text)



account_info()
