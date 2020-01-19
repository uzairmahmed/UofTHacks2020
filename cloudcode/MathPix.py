from io import StringIO

{
  "src": "data:image/jpeg;base64,...",
  "ocr": ["math","text"],
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


#!/usr/bin/env python
import sys
import base64
import requests
import json
import os

API_ID = os.getenv('API_ID')
API_KEY = os.getenv('API_KEY')

#file_info is the equivalent of writing open(file_name, 'rb').read()

def handToMath(file_info):
    image_uri = "data:image/jpg;base64," + base64.b64encode(file_info).decode()
    r = requests.post("https://api.mathpix.com/v3/latex",
        data=json.dumps({'src': image_uri, 'formats': ['latex_normal']}),
        headers={"app_id": API_ID, "app_key": API_KEY,
                 "Content-type": "application/json"})

    dump = json.dumps(json.loads(r.text), indent=4, sort_keys=True)
    loaded = json.loads(dump)

    return(loaded)
