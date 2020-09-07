# simple test script making a GET Request to a url in this homework project I am using hubapi.
import json
import requests

request = requests.get("url", + parmeters, + )
request_text = request.text

data = json.loads(request_text)

# writes json data into a json file
data_serialized = json.dump(data, open('data.json', "w"), indent = 4)


# for loop to parse the key:value pairs of a json file. Modify as needed.

for d in data[object]:
    print(d[key])

#print(type(data))
