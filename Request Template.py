import requests

octopusUrl = "http://xxx:8044/api/Spaces-1/xxx"

querystring = {"skip":"0","take":"xxx"}

headers = {
    'X-Octopus-ApiKey': "xxx",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Host': "xxx:8044",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.get(octopusUrl, headers=headers, params=querystring)

with open("query.txt", "a") as exportFile:
    exportFile.write(response.text)