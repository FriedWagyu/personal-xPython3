import requests
import json
from openpyxl import workbook

# get huobi data
rawHuobi = json.loads(requests.get(url = "https://api.huobi.pro/market/tickers").text)
rawHuobiData = rawHuobi["data"]

# get binance data
rawBinance = json.loads(requests.get(url = "https://api.binance.com/api/v3/exchangeInfo").text)
print(rawBinance)
#rawBinanceData = rawBinance



# variables
totalSymbol = 0
totalUSDT = 0
totalUSDC = 0
totalUSDD = 0
totalBTC = 0
totalETH = 0
totalHT = 0
listAllSymbol = []

# symbol count
for i in rawHuobiData:
    totalSymbol = totalSymbol + 1
    if i["symbol"][-4:] == "usdt":
        totalUSDT = totalUSDT + 1
        listAllSymbol.append(i["symbol"][:-4])
    elif i["symbol"][-4:] == "usdc":
        totalUSDC = totalUSDC + 1
        listAllSymbol.append(i["symbol"][:-4])
    elif i["symbol"][-4:] == "usdd":
        totalUSDD = totalUSDD + 1
        listAllSymbol.append(i["symbol"][:-4])
    elif i["symbol"][-3:] == "btc":
        totalBTC = totalBTC + 1
        listAllSymbol.append(i["symbol"][:-3])
    elif i["symbol"][-3:] == "eth":
        totalETH = totalETH + 1
        listAllSymbol.append(i["symbol"][:-3])
    elif i["symbol"][-2:] == "ht":
        totalHT = totalHT + 1
        listAllSymbol.append(i["symbol"][:-2])

# remove duplicate
listAllSymbolSimple = []

for i in listAllSymbol:
    if i not in listAllSymbolSimple:
        listAllSymbolSimple.append(i)
        


if len(listAllSymbolSimple) != totalUSDC + totalUSDT + totalUSDD + totalBTC + totalETH + totalHT:
    print("ok")
