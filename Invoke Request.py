import requests
import json
from requests_negotiate_sspi import HttpNegotiateAuth
from collections import namedtuple
from types import SimpleNamespace

def invokeRequest(url):
    response = requests.get(url, auth=HttpNegotiateAuth())
    return response

# Using Dictionaries to Parse JSON.
json_object = invokeRequest("http://httpbin.org/json").json() # Creates dictionary

for x in json_object["slideshow"]["slides"]:
    print(x["title"])


# Using Namedtuple to Create Object and Iterate JSON
response = invokeRequest("http://httpbin.org/json").content # Creates raw JSON formatted as bytes
namedtuple_object = json.loads(response, object_hook=lambda d: namedtuple('attribute', d.keys())(*d.values()))

for x in namedtuple_object.slideshow.slides:
    print(x.title)


# Using SimpleNamespace to Create Object and Iterate JSON
response = invokeRequest("http://httpbin.org/json").content # Creates raw JSON formatted as bytes
namespace_object = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))

for x in namespace_object.slideshow.slides:
    print(x.title)

# Creating Custom Class and Assigning Values to Class in Loop
class CustomObject:
    def __init__(self, title, type, *args, **kwargs):
        self.title = title
        self.type = type
        self.other = args


for x in json_object["slideshow"]["slides"]:
    u = CustomObject(
        x["title"],
        x["type"]
        )

print(u.title)

