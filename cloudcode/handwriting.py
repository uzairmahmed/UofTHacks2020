import os, io
from google.cloud import vision
from google.cloud.vision import types
import json

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"keys.json"

def handWriting_OCR(file_info):
    """Detects document features in an image."""
    print("Start Writing")

    client = vision.ImageAnnotatorClient()

    image = vision.types.Image(content=file_info)

    response = client.document_text_detection(image=image)

    print("End Writing")

    return response
