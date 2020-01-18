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
#!/usr/bin/env python
import sys
import base64
import requests
import json

# put desired file path here
file_path = 'limit.jpg'
image_uri = "data:image/jpg;base64," + base64.b64encode(open(file_path, "rb").read()).decode()
r = requests.post("https://api.mathpix.com/v3/latex",
    data=json.dumps({'src': image_uri, 'formats': ['latex_normal']}),
    headers={"app_id": "YOUR_APP_ID", "app_key": "YOUR_APP_KEY",
             "Content-type": "application/json"})
print(json.dumps(json.loads(r.text), indent=4, sort_keys=True))