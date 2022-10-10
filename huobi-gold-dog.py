import requests
import json
from openpyxl import workbook

# get huobi data
rawHuobi = json.loads(requests.get(url = "https://api.huobi.pro/market/tickers").text)
rawHuobiData = rawHuobi["data"]

# variables
totalSymbol = 0
totalUSDT = 0
totalUSDC = 0
totalBTC = 0

# symbol count
for i in rawHuobiData:
    totalSymbol = totalSymbol + 1
    if i["symbol"][-4:0] = "usdt":
        totalUSDT = totalUSDT + 1
    else
    
print(rawHuobiData)


print("ok")
