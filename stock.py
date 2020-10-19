import requests
import alpha_vantage
import json
import sys
from prettytable import PrettyTable
x = PrettyTable()
x.field_names = ["Symbol", "High", "Low", "Price", "Previous Close", "Change Percent"]
y = PrettyTable()
y.field_names = ["Symbol", "Price"]


def get_stock(symbols):
    API_URL = "https://www.alphavantage.co/query"
    req = ['01. symbol', '03. high', '04. low', '05. price', '08. previous close', '10. change percent']
    for symbol in symbols:
        data = {"function": "GLOBAL_QUOTE",
                "symbol": symbol,
                "apikey": "YOURAPIKEY"}
        response = requests.get(API_URL, data)
        data = response.json()
        information = []
        for items in req:
            information.append(data["Global Quote"][items])
        x.add_row(information)
    print(x)


def get_crypto(currency):
    API_URL = "https://www.alphavantage.co/query"
    req = ["1. From_Currency Code", "5. Exchange Rate"]
    for crypto in currency:
        data = {"function": "CURRENCY_EXCHANGE_RATE",
                "from_currency": crypto,
                "to_currency": "USD",
                "apikey": "YOURAPIKEY"}
        response = requests.get(API_URL, data)
        data = response.json()
        information = []
        information.append(data['Realtime Currency Exchange Rate']['1. From_Currency Code'])
        information.append(round(float(data['Realtime Currency Exchange Rate']['5. Exchange Rate']), 2))
        y.add_row(information)
    print(y)


def main():
    if len(sys.argv) == 1:
        get_crypto(["BTC", "ETH", "XRP", "EOS"])
        print()
        get_stock(["AAPL", "GOLD"])
    elif sys.argv[1].lower() == "-s":
        if len(sys.argv) >= 3:
            l = sys.argv
            for i in range(2): l.pop(0)
            try:
                get_stock(l)
            except KeyError:
                print("please enter valid information")
        else:
            try:
                get_stock(["AAPL", "AMZN", "TSLA", "MSFT", "GOLD"])
            except KeyError:
                print("please wait for a few min before making a call")

    elif sys.argv[1].lower() == "-c":
        if len(sys.argv) >= 3:
            l = sys.argv
            for i in range(2): l.pop(0)
            try:
                get_crypto(l)
            except KeyError:
                print("please enter valid information")
        else:
            get_crypto(["BTC", "ETH", "XRP", "EOS"])
    else:
        print("please enter valid information")


if __name__ == "__main__":
    main()
