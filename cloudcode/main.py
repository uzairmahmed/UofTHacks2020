import os
import sys
import json
from google.cloud import storage
from google.cloud import firestore
import google.cloud.exceptions

from MathPix import handToMath as get_math
from handwriting import handWriting_OCR as get_writing

import firebase_admin
from firebase_admin import credentials, firestore

# GCS
OUTPUT_BUCKET = "ipad-notes-output"
client = storage.Client()
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"keys.json"

# FIREBASE
MAIN_COLLECTION=u'Documents'
#cred = credentials.Certificate("./serviceAccountKey.json")
#firebase_admin.initialize_app(cred)
db.firestore.client()

def hello_gcs(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    #Image in bytes
    image_bytes = read_image(event, context)

    #Image ran through math api
    math = math_pix(image_bytes)
    print("Math")
    print(math)

    #Image ran through OCR api
    #writing = hand_write(image_bytes)
    #print("Writing")
    #print(writing)

    write_to_db(data=math, mode="math")

    #OLD write_to_db
    #write_to_db(math, 'math.json')
    #write_to_db(writing, 'write.json')

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
    
#Old write_to_db with GCS
"""
def write_to_db(item, output_file_name):
    print("Items start writing")
    print("Item",item)
    string_item = json.dumps(item)
    print("String Item", string_item)

    bucket = client.get_bucket(OUTPUT_BUCKET)
    blob = bucket.blob(output_file_name)
    blob.upload_from_string(data=string_item)
    print("Items done writing")
"""

def write_to_db(data, mode):
    print("Writing to database")
    current_element = check_current_element()
    if mode == "math":
        pass

    #TODO later
    else:
        pass

#TODO: Finish this
def check_current_element():
    print("Checking current elements")
    documents = get_documents()
    print("Documents received")

    return 0

def get_documents():
    print("Checking documents")
    docs = db.collection(MAIN_COLLECTION).stream()
    print("Documents found")
    print(docs)
    return docs

def start_fire():
    from google.cloud import firestore
    db = firestore.Client()
    return db

sys.modules[__name__] = hello_gcs