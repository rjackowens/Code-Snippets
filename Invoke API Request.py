from bs4 import BeautifulSoup
from requests_negotiate_sspi import HttpNegotiateAuth
import requests
import json

response = requests.get("xxxx:8080/tfs/xxxx/_apis/tfvc/items/?RecursionLevel=OneLevel&api-version=1.0", auth=HttpNegotiateAuth())
raw = response.json()

print(type(raw))

# for item in (raw["value"][0]):
#     for x in item:
#         print(x)

for i in (raw["value"][0]):
    print(i)
    for j in (raw["path"]):
        print(j)


# for x in raw.values():
#     for path in (x["path"][0]):
#         print(path)

# for x in raw.items():
#     print(type(x))
#     for y in (x["path"]):
#         print(y)