#!/usr/bin/env python

import yaml
import os
from pathlib import Path

file_name = Path(os.path.join(os.path.dirname(__file__), "app.yml"))
image_tag = ":" + "4.2"

try:
    assert file_name.exists()
    print("located file")
except (IOError, AssertionError) as e:
    raise e

with open(file_name, 'r') as file:
    try:
        data = yaml.load(file, Loader=yaml.FullLoader)
    except yaml.YAMLError as e:
        raise e

data["spec"]["template"]["spec"]["containers"][0]["image"] += str(image_tag)
print("updated image tag")

with open(file_name, 'w') as file:
    try:
        data = yaml.dump(data, file, default_flow_style=False)
    except yaml.YAMLError as e:
        raise e
print("done")
