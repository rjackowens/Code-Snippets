import random

dictionary = [{'id': 'RQ_65', 'type': 'matches', 'disabled': True, 'properties': {'count': 2, 'property': [{'name': 'property-name', 'value': 'system.agent.name'}, {'name': 'property-value', 'value': 'xxx'}]}}]
for x in dictionary:
    print(x.get("id"))

values= []
for y in range(101):
    result = y * random.randint(1, 50)
    values.append(result)

for count, z in enumerate(values):
    print("Processing", count + 1, "of", len(values))