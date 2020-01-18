import sys

from MathPix import handToMath as get_math
from handwriting import handWriting_OCR as get_writing
from google.cloud import storage

def hello_gcs(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    image_bytes = read_image(event, context)

    math = math_pix(image_bytes)
    print("Math")
    print(math)

    writing = hand_write(image_bytes)
    print("Writing")
    print(writing)

    return writing

def read_image(event, context):
    client = storage.Client()

    # Get the file that has been uploaded to GCS
    bucket = client.get_bucket(event['bucket'])
    blob = bucket.get_blob(event['name'])
    imagedata = blob.download_as_string()

    return imagedata

def math_pix(imagedata):
    image_info = get_math(imagedata)
    return image_info

def hand_write(imagedata):
    image_info = get_writing(imagedata)
    return image_info

sys.modules[__name__] = hello_gcs