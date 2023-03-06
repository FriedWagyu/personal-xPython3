import requests
import json
import time
import hmac
from requests import Request

# get data
raw = json.loads(requests.get(url = "https://api.sandbox.sardine.ai/v1/fiat-currencies").text)
data = raw["data"]

count = 0
country = []

for i in data:
    for j in i["supportingCountries"]:
        if j in country:
            contunue
        else:
            country.append(j)
            count += 1

print(country)
print(count)
