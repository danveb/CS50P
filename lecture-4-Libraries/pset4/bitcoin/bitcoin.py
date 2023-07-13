# Implement a Python program that expects a user to specify as command-line argument the number of Bitcoins "N" they'd like to buy
# If argument cannot be converted to a "float", program exits with error msg

import sys
import requests
import json

# JSON
# {'time': {'updated': 'Jul 13, 2023 18:20:00 UTC', 'updatedISO': '2023-07-13T18:20:00+00:00', 'updateduk': 'Jul 13, 2023 at 19:20 BST'}, 'disclaimer': 'This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org', 'chartName': 'Bitcoin', 'bpi': {'USD': {'code': 'USD', 'symbol': '&#36;', 'rate': '31,251.7558', 'description': 'United States Dollar', 'rate_float': 31251.7558}, 'GBP': {'code': 'GBP', 'symbol': '&pound;', 'rate': '26,113.7171', 'description': 'British Pound Sterling', 'rate_float': 26113.7171}, 'EUR': {'code': 'EUR', 'symbol': '&euro;', 'rate': '30,443.7729', 'description': 'Euro', 'rate_float': 30443.7729}}}

# JSON DUMP
# {
#   "time": {
#     "updated": "Jul 13, 2023 18:22:00 UTC",
#     "updatedISO": "2023-07-13T18:22:00+00:00",
#     "updateduk": "Jul 13, 2023 at 19:22 BST"
#   },
#   "disclaimer": "This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
#   "chartName": "Bitcoin",
#   "bpi": {
#     "USD": {
#       "code": "USD",
#       "symbol": "&#36;",
#       "rate": "31,253.1674",
#       "description": "United States Dollar",
#       "rate_float": 31253.1674
#     },
#     "GBP": {
#       "code": "GBP",
#       "symbol": "&pound;",
#       "rate": "26,114.8966",
#       "description": "British Pound Sterling",
#       "rate_float": 26114.8966
#     },
#     "EUR": {
#       "code": "EUR",
#       "symbol": "&euro;",
#       "rate": "30,445.1480",
#       "description": "Euro",
#       "rate_float": 30445.148
#     }
#   }
# }

try:
    API_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"
    # check: if length of argument NOT 2
    if len(sys.argv) != 2:
        # exit system with error message
        sys.exit("Missing command-line argument")
    # else: sys.argv[1]
    else:
        response = requests.get(API_URL)
        # print(response.json())
        # print(json.dumps(response.json(), indent=2))
        data = response.json()
        price = data["bpi"]["USD"]["rate_float"]
        amount = float(sys.argv[1])
        calculation = price * amount
        print(f"${calculation:,.4f}")

except requests.RequestException:
    ...