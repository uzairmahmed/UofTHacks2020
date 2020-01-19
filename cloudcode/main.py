import sys
import json
from google.cloud import storage

from MathPix import handToMath as get_math
from handwriting import handWriting_OCR as get_writing

OUTPUT_BUCKET = "ipad-notes-output"
client = storage.Client()

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

    #writing = hand_write(image_bytes)
    #print("Writing")
    #print(writing)

    write_to_db(math, 'math.json')

def read_image(event, context):
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
    
def write_to_db(item, output_file_name):
    print("Items start writing")
    print("Item",item)
    string_item = json.dumps(item)
    print("String Item", string_item)

    bucket = client.get_bucket(OUTPUT_BUCKET)
    blob = bucket.get_blob(output_file_name)
    blob.upload_from_string(string_item, content_type="json")
    print("Items done writing")


sys.modules[__name__] = hello_gcs