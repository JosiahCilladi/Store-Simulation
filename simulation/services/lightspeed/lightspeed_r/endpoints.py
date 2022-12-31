# Files
# from services.lightspeed.lightspeed_r import oauth


import json
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv
load_dotenv()

from services.lightspeed.lightspeed_r.lightspeed_r_auth import *

# creation datetime
today = datetime.utcnow()
now = str(today.isoformat())



def account_info():
    print("account_id")
    url = 'https://api.lightspeedapp.com/API/Account.json'

    response = send_request("GET", url)
  

    print(json.dumps(response, indent=1))
    


def open_register():
    print("open_register")

    url = "https://api.lightspeedapp.com/API/V3/Account/295355/Register/1/open.json"

    payload = [{
        "amount": "1000",
       	"notes": "Register opened via API",
    	"employeeID": "1",
    	"paymentTypeID": "1"
    }]

   
    # response = requests.request("POST", url, headers=headers, data=payload)
    response = send_request("POST", url, payload)

    reg_withdraw_id = response["RegisterWithdraw"]["registerWithdrawID"]
    amount = response["RegisterWithdraw"]["amount"]
    print("------------Register #1 Open ------------ ", "ID: ",
          reg_withdraw_id, "Cash: ", amount)
    print("--------------------------------------------------------------")
    # print(json.dumps(response, indent=1))


def close_register():
    print("close_register")

    url = "https://api.lightspeedapp.com/API/V3/Account/295355/Register/1/close.json"

    payload = [{
        "notes": "Closed Register via the API",
        "openTime": "2021-04-06",
        "closeEmployeeID": "1"
    }]
    response = send_request("POST", url, payload)
    
    reg_withdraw_id = response["RegisterCount"]["registerCountID"]
    calculated = response["RegisterCount"]["RegisterCountAmounts"]["RegisterCountAmount"][0]["calculated"]
    actual = response["RegisterCount"]["RegisterCountAmounts"]["RegisterCountAmount"][0]["actual"]
    print("------------Register #1 Close -- ",
          "ID: ", reg_withdraw_id, "Cash Calculated: ",calculated,"Cash Actual", actual)
    print("--------------------------------------------------------------")
    # print(json.dumps(response, indent=1))




def create_sale():
    print("create_sale")

    url = "https://api.lightspeedapp.com/API/V3/Account/295355/Sale.json"

    payload = [{
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

    response = send_request("POST", url, payload)

    sale_id = response["Sale"]["saleID"]
    calcSubtotal = response["Sale"]["calcSubtotal"]

    print("------------Sale------------ ID:",
          sale_id, "calcSubtotal:", calcSubtotal)
    print("--------------------------------------------------------------")
    # print(json.dumps(response, indent=1))



def create_ecom_sale():
    print("create_ecom_sale")
    url = "https://api.lightspeedapp.com/API/V3/Account/295355/Sale.json"
    
    payload = [{
        "discountPercent": "0",
        "completed": "true",
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
        "taxCategoryID": "0",
        "SaleLines": {
            "SaleLine": {
                    "itemID": 1,
                    "note": "Store Credit",
                    "unitQuantity": 1,
                    "unitPrice": 50,
                    "taxClassID": 0,
                    "avgCost": 0,
                    "fifoCost": 0
            }
        },
        "SalePayments": {
            "SalePayment": {
                "amount": 107,
              		"paymentTypeID": 1,
                "creditAccountID": 1
            }
        }
    }]

    response = send_request("POST", url, payload)

    
    sale_id = response["Sale"]["saleID"]
    calcSubtotal = response["Sale"]["calcSubtotal"]
    print("------------eCom Order------------ ID:",
          sale_id, "calcSubtotal:", calcSubtotal)
    print("--------------------------------------------------------------")
    # print(json.dumps(response, indent=1))




# def create_sale_line(sale_id):
#     print("create_sale_line")

#     url = (
#         f"https://api.lightspeedapp.com/API/V3/Account/295355/Sale/{sale_id}/SaleLine.json")

#     payload = [{
#         "employeeID": "1",
#         "itemID": "1",
#         "shopID": "1",
#         "saleID": sale_id,
#         "createTime": now
#     }]

#     response = send_request("POST", url, payload)

#     print(json.dumps(response, indent=1))


# def complete_sale(sale_id):
#     print("complete_sale")

#     url = (
#         f"https://api.lightspeedapp.com/API/V3/Account/295355/Sale/{sale_id}.json")

#     payload = [{
#         "discountPercent": "0",
#         "completed": "true",
#         "completeTime": now,
#         "enablePromotions": "true",
#         "isTaxInclusive": "false",
#         "receiptPreference": "printed",
#         "customerID": "1",
#         "discountID": "0",
#         "employeeID": "1",
#         "quoteID": "0",
#         "registerID": "1",
#         "shipToID": "0",
#         "shopID": "1",
#         "taxCategoryID": "1"
#     }]

#     response = send_request("PUT", url, payload)
#     print(json.dumps(response, indent=1))

# # account_info()
