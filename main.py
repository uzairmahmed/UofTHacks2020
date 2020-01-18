import sys

from MathPix import handToMath
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

    """
    # Create a new image object and resample it
    newimage = Image(blob=imagedata)
    newimage.sample(200,200)

    # Upload the resampled image to the other bucket
    bucket = client.get_bucket(THUMBNAIL_BUCKET)
    newblob = bucket.blob('thumbnail-' + data['name'])     
    newblob.upload_from_string(newimage.make_blob())
    """
    return imagedata


sys.modules[__name__] = hello_gcs