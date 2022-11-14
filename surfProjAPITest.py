import requests
import json

url = "https://yh-finance.p.rapidapi.com/stock/v2/get-summary"

querystring = {"symbol":"AAPL","region":"US"}

headers = {
	"X-RapidAPI-Key": "6520434f99mshb47aa5f323c8a54p16f385jsn176f39a1c3c6",
	"X-RapidAPI-Host": "yh-finance.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
#print(response.text)


information = response.json()
print(type(information))
#print(information.keys())
priceDict = information.get('price')


high = priceDict.get('regularMarketDayHigh')
low = priceDict.get('regularMarketDayLow')

lowRaw = low.get('raw')
highRaw = high.get('raw')

print(type(high))
print("highest daily price " + json.dumps(highRaw))
print("lowest daily price " + json.dumps(lowRaw))



