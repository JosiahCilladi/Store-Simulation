# Files
# from services.lightspeed.lightspeed_r import oauth

from datetime import datetime
import json

from dotenv import load_dotenv
load_dotenv()

from services.lightspeed.lightspeed_r.lightspeed import *

# creation datetime
today = datetime.datetime.now(datetime.timezone.utc)
now = str(today.isoformat())



def account_info():
    print("account_id")
    url = 'https://api.lightspeedapp.com/API/Account.json'

    response = send_request("GET", url)
    json_response = json.loads(response.text)

    print(json.dumps(json_response, indent=1))



def open_register():
    print("open_register")

    url = "https://api.lightspeedapp.com/API/V3/Account/295355/Register/1/open.json"

    data = [{
        "amount": "1000",
       	"notes": "Register opened via API",
    	"employeeID": "1",
    	"paymentTypeID": "1"
    }]

    payload = json.dumps(data)
    # response = requests.request("POST", url, headers=headers, data=payload)
    response = send_request("POST", url, payload)

    json_response = json.loads(response.text)

    print(json.dumps(json_response, indent=1))



def close_register():
    print("close_register")

    url = "https://api.lightspeedapp.com/API/V3/Account/295355/Register/1/close.json"

    data = [{
        "notes": "Closed Register via the API",
        "openTime": "2021-04-06",
        "closeEmployeeID": "1"
    }]
    payload = json.dumps(data)
    response = send_request("POST", url, payload)

    json_response = json.loads(response.text)

    print(json.dumps(json_response, indent=1))



def create_sale1():
    print("create_sale")


    url = "https://api.lightspeedapp.com/API/V3/Account/295355/Sale.json"

  
    data = [{
        "discountPercent": "0",
        "completed": "false",
        "archived": "false",
        "voided": "false",
        "enablePromotions": "true",
        "isTaxInclusive": "false",
        "referenceNumber": "",
        "receiptPreference": "printed",
        "customerID": "1",
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
    json_response = json.loads(response.text)
    print(json.dumps(json_response, indent=1))
        
    sale_id = json_response["Sale"]["saleID"]
    create_sale_line(sale_id)
    complete_sale(sale_id)




def create_ecom_sale():
    print("create_ecom_sale")
    url = "https://api.lightspeedapp.com/API/V3/Account/295355/Sale.json"
    
    data = [{
        "discountPercent": "0",
        "completed": "false",
        "archived": "false",
        "voided": "false",
        "enablePromotions": "true",
        "isTaxInclusive": "false",
        "referenceNumberSource":"ecom",
        "referenceNumber": "1",
        "receiptPreference": "printed",
        "customerID": "1",
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

    json_response = json.loads(response.text)
    sale_id = json_response["Sale"]["saleID"]
    print(json.dumps(json_response, indent=1))
    create_sale_line(sale_id)
    complete_sale(sale_id)



def create_sale_line(sale_id):
    print("create_sale_line")

    url = (f"https://api.lightspeedapp.com/API/V3/Account/295355/Sale/{sale_id}/SaleLine.json")

    data = [{
        "employeeID": "1",
        "itemID": "1",
        "shopID": "1",
        "saleID": sale_id,
        "createTime": now
    }]

    payload = json.dumps(data)

    response = send_request("POST", url, payload)

    json_response = json.loads(response.text)

    print(json.dumps(json_response, indent=1))

    
def complete_sale(sale_id):
    print("complete_sale")

    url = (
        f"https://api.lightspeedapp.com/API/V3/Account/295355/Sale/{sale_id}.json")

    data = [{
        "discountPercent": "0",
        "completed": "true",
        "completeTime": now,
        "enablePromotions": "true",
        "isTaxInclusive": "false",
        "receiptPreference": "printed",
        "customerID": "1",
        "discountID": "0",
        "employeeID": "1",
        "quoteID": "0",
        "registerID": "1",
        "shipToID": "0",
        "shopID": "1",
        "taxCategoryID": "1"
    }]

    payload = json.dumps(data)

    response = send_request("PUT", url, payload)

    json_response = json.loads(response.text)

    print(json.dumps(json_response, indent=1))


def create_sale():
    print("create_sale")

    url = "https://api.lightspeedapp.com/API/V3/Account/295355/Sale.json"

    data = [{
        "discountPercent": "0",
        "completed": "true",
        "archived": "false",
        "voided": "false",
        "enablePromotions": "true",
        "isTaxInclusive": "false",
        "referenceNumber": "",
        "receiptPreference": "printed",
        "customerID": "1",
        "discountID": "0",
        "employeeID": "1",
        "tipEmployeeID": "0",
        "quoteID": "0",
        "registerID": "1",
        "shipToID": "0",
        "shopID": "1",
        "taxCategoryID": "0",
            "SaleLines": {
                "SaleLine": {
                    "itemID": 1,
                    "note": "Store Credit",
                    "unitQuantity": 1,
                    "unitPrice": 100,
                    "taxClassID": 0,
                    "avgCost": 0,
                    "fifoCost": 0
                }
            },
            "SalePayments": {
                "SalePayment": {
                    "amount": 110,
          		"paymentTypeID": 1,
                    "creditAccountID": 1
                }
            }

    }]
    payload = json.dumps(data)
    response = send_request("POST", url, payload)
    json_response = json.loads(response.text)
    print(json.dumps(json_response, indent=1))






account_info()
