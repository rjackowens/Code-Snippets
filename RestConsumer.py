import json

class RestConsumer:
    def serialize_to_json(self, x)
    payload = {
        "Name": x.Name,
        "ID": x.id,
        "Disabled": x.IsDisabled,
        "Group ID": x.ProjectGroupId
    }
    return json.dumps(payload)
    