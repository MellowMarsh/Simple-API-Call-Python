# simple test script making a GET Request to a url.
import json
import requests

request = requests.get("url", + "parmeters", + "API  Key" )
request_text = request.text

data = json.loads(request_text)

# writes json data into a json file
data_serialized = json.dump(data, open('data.json', "w"), indent = 4)


# for loop to parse the key:value pairs of a json file. Modify as needed.

for d in data["results"]:
    print(d["properties"])

#print(type(data))
