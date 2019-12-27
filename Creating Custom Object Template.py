import requests
import json
import re
import csv
import pandas as pd
from munch import munchify

octopusUrl = "http://xxx:8044/api/Spaces-1/projects?skip=0&take=xxx"
headers = {
    'X-Octopus-ApiKey': "xxx",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Host': "xxx:8044",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }
response = requests.get(octopusUrl, headers=headers)
raw = response.json() # Create dictionary
projectObject = munchify(raw) # Converting dictionary to object

for project in projectObject.Items:
    if ( re.match("False", str(project.IsDisabled)) and re.search(r'\Dev|QA|UAT|Prod\b', project.Name) and not re.match("ProjectGroups-xxx", project.ProjectGroupId) ):
        print(project.Name)
        print(project.IsDisabled)
        print(project.ProjectGroupId)
