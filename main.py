import sys

from MathPix import handToMath
import cloudstorage

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

    file_name = '/' + event['bucket'] + '/' + event['name']

    gcs_file = cloudstorage.open(file_name)
    contents = gcs_file.read()
    gcs_file.close()

    file_info = send_file(io.BytesIO(contents),
                   mimetype='image/png')

    print(file_info)

    return file_info


sys.modules[__name__] = hello_gcs