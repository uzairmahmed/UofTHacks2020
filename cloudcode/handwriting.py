import os, io
from google.cloud import vision
from google.cloud.vision import types
from google.protobuf.json_format import MessageToJson
import json

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"keys.json"

def handWriting_OCR(file_info):
    """Detects document features in an image."""
    print("Start Writing")

    client = vision.ImageAnnotatorClient()
    image = vision.types.Image(content=file_info)

    response = client.document_text_detection(image=image)

    dump = json.dumps(json.loads(MessageToJson(response.full_text_annotation)), indent=4, sort_keys=True)
    loaded = json.loads(dump)
    return loaded["text"]
