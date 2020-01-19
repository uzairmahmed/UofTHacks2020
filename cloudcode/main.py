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
    #parsedMath = parse_for_db("math", math)

    #Image ran through OCR api
    writing = hand_write(image_bytes)
    print("Writing")
    print(writing)
    #parsedWrite = parse_for_db("write", writing)

    write_to_db(data=math["latex_normal"], mode="math")

    #write_to_db(parsedMath, 'math.json')
    #write_to_db(parsedWrite, 'write.json')

def parse_for_db(mode, payload):
    parsed = {}
    parsed["mode"] = mode
    parsed["payload"] = payload
    return parsed

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
<<<<<<< HEAD
    
=======

def write_to_db(item, output_file_name):
    print("Items start writing")
    print("Item",item)
    string_item = json.dumps(item)
    print("String Item", string_item)
>>>>>>> 9545e87dbddec0e4c93439b7e1fecd84c4d627d0

def write_to_db(data, mode):
    print("Writing to database")
    
    doc_name = 'demo'

    document = get_document_contents(doc_name)

    index = get_index(document)

    print(u"index:{}".format(index))

    write_to_fire(doc_name=doc_name, data=data, index=index+1)

def write_to_fire(doc_name, data, index):
    print(u"STUFF{}".format(doc_name))
    print(u"STUFF{}".format(data))
    print(u"STUFF{}".format(index))
    fire_data = {str(index): str(data)}
    db.collection(MAIN_COLLECTION).document(doc_name).update(fire_data)


def get_index(document):
    return len(list(document.keys()))

def get_document_contents(doc_name):
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
