import requests
import json
from openpyxl import Workbook
import time
import hmac
from requests import Request

# get huobi data
rawHuobi = json.loads(requests.get(url = "https://api.huobi.pro/market/tickers").text)
rawHuobiData = rawHuobi["data"]

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
        
# get binance data
rawBinance = json.loads(requests.get(url = "https://api.binance.com/api/v3/exchangeInfo").text)
rawBinanceData = rawBinance["symbols"]

# variables
totalSymbol = 0
totalUSDT = 0
totalUSDC = 0
totalBUSD = 0
totalUSDD = 0
totalBTC = 0
totalETH = 0
listAllSymbol = []

# symbol count
for i in rawBinanceData:
    totalSymbol = totalSymbol + 1
    if i["symbol"][-4:] == "USDT":
        totalUSDT = totalUSDT + 1
        listAllSymbol.append(i["symbol"][:-4])
    elif i["symbol"][-4:] == "USDC":
        totalUSDC = totalUSDC + 1
        listAllSymbol.append(i["symbol"][:-4])
    elif i["symbol"][-4:] == "BUSD":
        totalBUSD = totalBUSD + 1
        listAllSymbol.append(i["symbol"][:-4])
    elif i["symbol"][-4:] == "USDD":
        totalUSDD = totalUSDD + 1
        listAllSymbol.append(i["symbol"][:-4])
    elif i["symbol"][-3:] == "BTC":
        totalBTC = totalBTC + 1
        listAllSymbol.append(i["symbol"][:-3])
    elif i["symbol"][-3:] == "ETH":
        totalETH = totalETH + 1
        listAllSymbol.append(i["symbol"][:-3])

# remove duplicate
listAllBinanceSymbolSimple = []

for i in listAllSymbol:
    if i not in listAllBinanceSymbolSimple:
        listAllBinanceSymbolSimple.append(i.lower())

# simplify huobi
listAllSymbolSimpleRemove = []

for i in listAllSymbolSimple:
    if i not in listAllBinanceSymbolSimple:
        listAllSymbolSimpleRemove.append(i)
        
# get ftx data
ts = int(time.time() * 1000)
request = Request('GET', 'https://ftx.com/api')
prepared = request.prepare()
signature_payload = f'{ts}{prepared.method}{prepared.path_url}'.encode()
signature = hmac.new('KP9qvt2y8W8rDDJEHdZ7nuYfG-X7Hr8w__9aNPiO'.encode(), signature_payload, 'sha256').hexdigest()

prepared.headers['FTX-KEY'] = 'b8KQGAHYfOGvZOxvPsujqsofKtNdTqNRgArIu2dd'
prepared.headers['FTX-SIGN'] = signature
prepared.headers['FTX-TS'] = str(ts)

rawFTX = json.loads(requests.get(url = "https://ftx.com/api/markets").text)
rawFTXData = rawFTX["result"]

# variables
totalSymbol = 0
totalUSDT = 0
totalUSDC = 0
totalBTC = 0
totalETH = 0
listAllSymbol = []

# symbol count
for i in rawFTXData:
    totalSymbol = totalSymbol + 1
    if i['name'][-5:] == "/USDT":
        totalUSDT = totalUSDT + 1
        listAllSymbol.append(i['name'][:-5])
    elif i['name'][-4:] == "/USD":
        totalUSDC = totalUSDC + 1
        listAllSymbol.append(i['name'][:-4])
    elif i['name'][-4:] == "/BTC":
        totalBTC = totalBTC + 1
        listAllSymbol.append(i['name'][:-4])
    elif i['name'][-4:] == "/ETH":
        totalETH = totalETH + 1
        listAllSymbol.append(i['name'][:-4])
        
# remove duplicate
listAllFTXSymbolSimple = []

for i in listAllSymbol:
    if i not in listAllFTXSymbolSimple:
        listAllFTXSymbolSimple.append(i.lower())

# simplify huobi
listAllSymbolSimpleRemoveBF = []

for i in listAllSymbolSimpleRemove:
    if i not in listAllFTXSymbolSimple:
        listAllSymbolSimpleRemoveBF.append(i)
        
# get okx data
rawOKX = json.loads(requests.get(url = "https://www.okx.com/api/v5/market/tickers?instType=SPOT").text)
rawOKXData = rawOKX["data"]

# variables
totalSymbol = 0
totalUSDT = 0
totalUSDC = 0
totalBTC = 0
totalETH = 0
listAllSymbol = []

# symbol count
for i in rawOKXData:
    totalSymbol = totalSymbol + 1
    if i['instId'][-5:] == "-USDT":
        totalUSDT = totalUSDT + 1
        listAllSymbol.append(i['instId'][:-5])
    elif i['instId'][-5:] == "-USDC":
        totalUSDC = totalUSDC + 1
        listAllSymbol.append(i['instId'][:-5])
    elif i['instId'][-4:] == "-BTC":
        totalBTC = totalBTC + 1
        listAllSymbol.append(i['instId'][:-4])
    elif i['instId'][-4:] == "-ETH":
        totalETH = totalETH + 1
        listAllSymbol.append(i['instId'][:-4])

# remove duplicate
listAllOKXSymbolSimple = []

for i in listAllSymbol:
    if i not in listAllOKXSymbolSimple:
        listAllOKXSymbolSimple.append(i.lower())
        
# simplify huobi
listAllSymbolSimpleRemoveBFO = []

for i in listAllSymbolSimpleRemoveBF:
    if i not in listAllOKXSymbolSimple:
        listAllSymbolSimpleRemoveBFO.append(i)
        
# get gate data
rawGATE = json.loads(requests.get(url = "https://api.gateio.ws/api/v4/spot/currencies").text)

# symbol count
listAllSymbol = []
for i in rawGATE:
    listAllSymbol.append(i["currency"].lower())
    
# simplify huobi
listAllSymbolSimpleRemoveBFOG = []

for i in listAllSymbolSimpleRemoveBFO:
    if i not in listAllSymbol:
        listAllSymbolSimpleRemoveBFOG.append(i)

# open work book
wb = Workbook()
ws = wb.active

for i in listAllSymbolSimpleRemoveBFOG:
    usdtVol = 0
    usdcVol = 0
    usddVol = 0
    btcVol = 0
    ethVol = 0
    usdtDepth = 0
    usdcDepth = 0
    usddDepth = 0
    btcDepth = 0
    ethDepth = 0
    for j in rawHuobiData:
        if i + "usdt" == j["symbol"]:
            usdtVol = float(j["vol"])
            usdtDepth = float(j["bidSize"]) + float(j["askSize"])
    for j in rawHuobiData:
        if i + "usdc" == j["symbol"]:
            usdcVol = float(j["vol"])
            usdcDepth = float(j["bidSize"]) + float(j["askSize"])
    for j in rawHuobiData:
        if i + "usdd" == j["symbol"]:
            usddVol = float(j["vol"])
            usddDepth = float(j["bidSize"]) + float(j["askSize"])
    for j in rawHuobiData:
        if i + "btc" == j["symbol"]:
            btcVol = float(j["vol"])
            btcDepth = float(j["bidSize"]) + float(j["askSize"])
    for j in rawHuobiData:
        if i + "eth" == j["symbol"]:
            ethVol = float(j["vol"])
            ethDepth = float(j["bidSize"]) + float(j["askSize"])
    totalVol = usdtVol + usdcVol + usddVol + btcVol * 20000 + ethVol * 1300
    totalDepth = usdtDepth + usdcDepth + usddDepth + btcDepth * 20000 + ethDepth * 1300
    ws.append([i, totalVol, totalDepth])

wb.save("test.xlsx")

#print(listAllSymbolSimpleRemoveBFOG)

#print(len(listAllSymbolSimpleRemoveBFOG), len(listAllSymbolSimpleRemoveBFO))
