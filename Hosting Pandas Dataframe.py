import requests
import re
import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

globalHeaders = {
    'X-Octopus-ApiKey': "xxx",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    }

projectRequest = "http://xxx:8044/api/Spaces-1/projects?skip=0&take=xxx"
projectResponse = requests.get(projectRequest, headers=globalHeaders)
projectRaw = projectResponse.json()  # Create dictionary

name = []
id = []
isDisabled = []
projectGroupId = []

for project in (projectRaw["Items"]):
    if (re.match("False", str(project["IsDisabled"])) and re.search(r'\Dev|QA|UAT|Prod\b', project["Name"]) and not re.match("ProjectGroups-xxx", project["ProjectGroupId"])):
        name.append(project["Name"])
        id.append(project["Id"])
        isDisabled.append(project["IsDisabled"])
        projectGroupId.append(project["ProjectGroupId"])

df_Filtered = pd.DataFrame(
    {
        "Project": name,
        "ProjectId": id,
        "ProjectGroupId": projectGroupId,
        "IsDisabled": isDisabled
    }
)

@app.route('/')
def default_page():
    return render_template("dataframe.html", name="Filtered Projects", data=df_Filtered.to_html())

if __name__ == '__main__':
    app.run(host="localhost")
