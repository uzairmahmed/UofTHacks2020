import os, io
from google.cloud import vision
from google.cloud.vision import types
from google.protobuf.json_format import MessageToJson
import json

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"keys.json"
client = vision.ImageAnnotatorClient()

file_name = 'test.png'


def handWriting_OCR(file_path):
    with io.open(file_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.document_text_detection(image=image)

    dump = json.dumps(json.loads(MessageToJson(response.full_text_annotation)), indent=4, sort_keys=True)
    loaded = json.loads(dump)
    return loaded["text"]

def parse_for_db(mode, payload):
    parsed = {}
    parsed["mode"] = mode
    parsed["payload"] = payload
    return parsed


output = handWriting_OCR(file_name)
print(output)
print(parse_for_db(0,output))

