import json
import jsonschema
import os
import urllib.request

SCHEMA_URL = "https://planecommand.com/schema/aircraft_profile_v3.1.json"

g = urllib.request.urlopen(SCHEMA_URL)

schema_text = g.read().decode()
schema = json.loads(schema_text)
print("Schema downloaded")

files = [filename for filename in os.listdir('.') if os.path.isfile(filename) and os.path.splitext(filename)[1] == ".json"]

for filename in files:
    print(f"File: {filename}")
    with open(filename, "r") as f:
        json_str = f.read()
    try:
        # Read in the JSON document
        datum = json.loads(json_str)
        # And validate the result
        jsonschema.validate(datum, schema)
    except jsonschema.exceptions.ValidationError as e:
        print("well-formed but invalid JSON:", e)
    except json.decoder.JSONDecodeError as e:
        print("poorly-formed text, not JSON:", e)

    
    with open(filename, "w") as f:
        f.write(json.dumps(datum, indent=4))
