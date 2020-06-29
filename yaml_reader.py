import yaml
import os
import logging
import sys
from pathlib import Path

log = logging.getLogger(__name__)

# Verify YAML File Exists in Current Directory
try:
    assert Path(os.path.join(os.path.dirname(__file__), "example.yml")).exists()
    log.debug("File exists.")
except (IOError, AssertionError) as e:
    log.error(e, exc_info=True)
    raise

with open(os.path.join(os.path.dirname(__file__), "example.yml"), "r") as stream:
    global_vars = yaml.safe_load(stream)

def setVar(key, value):
    print(f"##vso[task.setvariable variable={key};isOutput=false]{value}")

# Getting Specific Value
print(global_vars["test"].get("value1"))

# Getting Key Value Pairs and Setting Env Variables
for key, value in global_vars["test"].items():
    print(key, value)
    setVar(key, value)

# Setting Example Pipeline Env Variable
print("##vso[task.setvariable variable=ThisIsATest2;issecret=false]value")