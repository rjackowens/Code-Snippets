import requests
import re
import pandas as pd

octopusUrl = "http://xxx:8044/api/Spaces-1/xxx"
headers = {
    'X-Octopus-ApiKey': "xxx",
    'Accept': "*/*",
    'Host': "xxx",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    }
response = requests.get(octopusUrl, headers=headers)
raw = response.json()  # Create dictionary

# for project in (raw["Items"]):
#     if (re.match("False", str(project["IsDisabled"])) and re.search(r'\Dev|QA|UAT|Prod\b', project["Name"]) and not re.match("ProjectGroups-xxx", project["ProjectGroupId"])):
#         # name.append(project["Name"])

# Need to find a way to add the conditional if statement above to list comprehensions
name = [project["Name"] for project in (raw["Items"])]
isDisabled = [project["IsDisabled"] for project in (raw["Items"])]
projectGroupId = [project["ProjectGroupId"] for project in (raw["Items"])]

df = pd.DataFrame(
    {
        "NAME": name,
        "GROUP ID": projectGroupId,
        "DISABLED": isDisabled
    }
)

df.to_csv(r"name.csv", index=None, header=True)
