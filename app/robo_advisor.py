# app/robo_advisor.py

import json 
import datetime
import csv
import os

import requests


# convert to usd formatting
def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

#
# INFO INPUTS
#




request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo"

response = requests.get(request_url)


parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

request_at = datetime.datetime.today().strftime("%Y-%m-%d %I:%M %p")

tsd = parsed_response["Time Series (Daily)"]
dates = list(tsd.keys()) # SORT DATES
latest_day = dates[0]
latest_close = tsd[latest_day]["4. close"]#> $1,000.00

# maximum of all high prices

high_prices = []
low_prices = []

# check latest 100?
for date in dates:
    high_price = tsd[date]["2. high"]
    high_prices.append(float(high_price))
    low_price = tsd[date]["3. low"]
    low_prices.append(float(low_price))

recent_high = max(high_prices)
recent_low = min(low_prices)
#
# INFO OUTPUTS
#

csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv") # a relative filepath

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above
    
    #looping
    writer.writerow({
        "timestamp": "TODO", 
        "open": "TODO", 
        "high": "TODO", 
        "low": "TODO", 
        "close": "TODO", 
        "volume": "TODO"   
    })
    writer.writerow({
        "timestamp": "TODO", 
        "open": "TODO", 
        "high": "TODO", 
        "low": "TODO", 
        "close": "TODO", 
        "volume": "TODO"   
    })
print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA")
print(f"REQUEST AT: {request_at}")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print(f"WRITING DATA TO CSV {csv_file_path}...")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")

