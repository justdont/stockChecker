import requests
import alpha_vantage
import json
API_URL = "https://www.alphavantage.co/query"
symbols = ['AAPL','AMZN']#add your own stocks for now, cap lock does not matter

for symbol in symbols:
        data = {"function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": "get ur own API at alphavantage"}
        response = requests.get(API_URL, data)
        data = response.json()
        print(symbol)
        req = ['02. open', '03. high', '04. low', '05. price', '09. change', '10. change percent']#you can add what you would like based on the example feedback from this website: https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey=demo
        for items in req:
            print('{0}: {1}'.format(items[4:], data['Global Quote'][items]))

