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
client = storage.Client()
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"keys.json"

# FIREBASE
MAIN_COLLECTION=u'Documents'
cred = credentials.Certificate("keys.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

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
    writing = hand_write(image_bytes)
    print("Writing")
    print(writing)

    write_to_db(data=math, mode="math")

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
    

def write_to_db(data, mode):
    print("Writing to database")
    document = get_document_contents()
    if mode == "math":
        pass

    #TODO later
    else:
        pass


def get_document_contents():
    doc_name = 'demo'
    doc_contents = None
    documents = get_document(doc_name)

    try:
        doc_contents = documents.get().to_dict()
        print(u'Contents:{}'.format(doc_contents))
        print(u'Contents Type:{}'.format(type(doc_contents)))
    except:
        print(u'Can\'t find document')

    return doc_contents

def get_document(doc_name):
    docs = db.collection(MAIN_COLLECTION).document(doc_name)
    return docs

def start_fire():
    from google.cloud import firestore
    db = firestore.Client()
    return db

sys.modules[__name__] = hello_gcs