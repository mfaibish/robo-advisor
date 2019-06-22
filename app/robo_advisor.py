# app/robo_advisor.py

import json 
import datetime
import csv
import os

import requests
from dotenv import load_dotenv

load_dotenv()

# convert to usd formatting
def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

if __name__ == "__main__":
 
#
# INFO INPUTS
#
    api_key = os.environ.get("ALPHAVANTAGE_API_KEY", "demo")

    while True:
        symbol = input("Please input a stock symbol (i.e. 'MSFT'): ").upper()
        #symbols = [s for s in input("Please input a one or more stock symbols separated by a ',' (i.e. 'MSFT'): ").split(',')]
        if len(symbol) < 6 and symbol.isalpha():
            break
        else:
            print("OOPS, YOU'VE ENTERED AN INVALID SYMBOL. TRY AGAIN.")
            next
        #for s in symbols:

    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    try:
       parsed_response['Time Series (Daily)']
    except:
       print("OOPS, stock symbol is invalid. Try again. ")
       exit()
    
    last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
    request_at = datetime.datetime.today().strftime("%Y-%m-%d %I:%M %p")
    tsd = parsed_response["Time Series (Daily)"]
    dates = sorted(list(tsd.keys()), reverse = True)  #> sorting reference https://www.programiz.com/python-programming/methods/list/sort
    latest_day = dates[0]
    latest_close = tsd[latest_day]["4. close"]#> $1,000.00
    
    # maximum of all high prices
    high_prices = []
    low_prices = []
    

    for date in dates:
        high_price = tsd[date]["2. high"]
        high_prices.append(float(high_price))
        low_price = tsd[date]["3. low"]
        low_prices.append(float(low_price))
    recent_high = max(high_prices)
    recent_low = min(low_prices)
    
    if float(latest_close) < float(recent_low * 1.2):
        recommend = "BUY!"
        reco_reason = "This stock is less than 20% above the recent low."
    else:
        recommend = "PASS"
        reco_reason = "This stock is too high to buy right now."
#
# INFO OUTPUTS
#
    csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv") # a relative filepath
    csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]
    with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
        writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
        writer.writeheader() # uses fieldnames set above
        for date in dates:
            daily_prices = tsd[date]
            writer.writerow({
                "timestamp": date , 
                "open": to_usd(float(daily_prices["1. open"])), 
                "high": to_usd(float(daily_prices["2. high"])), 
                "low": to_usd(float(daily_prices["3. low"])), 
                "close": to_usd(float(daily_prices["4. close"])), 
                "volume": daily_prices["5. volume"]   
            })

    print("-------------------------")
    print(f"SELECTED SYMBOL: {symbol}")
    print("-------------------------")
    print("REQUESTING STOCK MARKET DATA")
    print(f"REQUEST AT: {request_at}")
    print("-------------------------")
    print(f"LATEST DAY: {last_refreshed}")
    print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
    print(f"RECENT HIGH: {to_usd(float(recent_high))}")
    print(f"RECENT LOW: {to_usd(float(recent_low))}")
    print("-------------------------")
    print(f"RECOMMENDATION: {recommend}")
    print(f"RECOMMENDATION REASON: {reco_reason}")
    print("-------------------------")
    print(f"WRITING DATA TO CSV {csv_file_path}...")
    print("-------------------------")
    print("HAPPY INVESTING!")
    print("-------------------------")

