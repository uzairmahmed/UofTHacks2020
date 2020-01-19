from io import StringIO

{
    "src": "data:image/jpeg;base64,...",
    "ocr": ["math", "text"],
    "skip_recrop": "true",
    "formats": [
        "text",
        "latex_simplified",
        "latex_styled",
        "mathml",
        "asciimath",
        "latex_list"
    ]
}

# !/usr/bin/env python
import sys
import base64
import requests
import json

with open('keys.json') as json_file:
    data = json.load(json_file)
    API_ID = data['APP_ID']
    API_KEY = data['APP_KEY']

file_name = 'test.png'


def handToMath(file_path):
    image_uri = "data:image/jpg;base64," + base64.b64encode(open(file_path, "rb").read()).decode()
    r = requests.post("https://api.mathpix.com/v3/latex",
                      data=json.dumps({'src': image_uri, 'formats': ['latex_normal']}),
                      headers={"app_id": API_ID, "app_key": API_KEY,
                               "Content-type": "application/json"})

    dump = json.dumps(json.loads(r.text), indent=4, sort_keys=True)
    loaded = json.loads(dump)
    return loaded["latex_normal"]

def parse_for_db(mode, payload):
    parsed = {}
    parsed["mode"] = mode
    parsed["payload"] = payload
    return parsed

output = handToMath(file_name)
print(output)
print(parse_for_db(1,output))