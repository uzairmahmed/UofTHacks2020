import sys

from MathPix import handToMath as get_math
from google.cloud import storage

def hello_gcs(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    print('Event ID: {}'.format(context.event_id))
    print('Event type: {}'.format(context.event_type))
    print('Bucket: {}'.format(event['bucket']))
    print('File: {}'.format(event['name']))
    print('Metageneration: {}'.format(event['metageneration']))
    print('Created: {}'.format(event['timeCreated']))
    print('Updated: {}'.format(event['updated']))

    client = storage.Client()

    # Get the file that has been uploaded to GCS
    bucket = client.get_bucket(event['bucket'])
    print("bucket success")
    blob = bucket.get_blob(event['name'])
    print("blob success")
    imagedata = blob.download_as_string()
    print ("imagedata success")

    print(imagedata)

    latex_info = get_math(imagedata)
    return imagedata


sys.modules[__name__] = hello_gcs