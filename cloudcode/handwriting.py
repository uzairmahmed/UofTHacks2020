import os, io
from google.cloud import vision
from google.cloud.vision import types
import json

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"keys.json"

client = vision.ImageAnnotatorClient()

def handWriting_OCR(file_info):
    """Detects document features in an image."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    image = vision.types.Image(content=file_info)

    response = client.document_text_detection(image=file_info)

    print(response)

    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            print('\nBlock confidence: {}\n'.format(block.confidence))

            for paragraph in block.paragraphs:
                print('Paragraph confidence: {}'.format(
                    paragraph.confidence))

                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    print('Word text: {} (confidence: {})'.format(
                        word_text, word.confidence))

                    for symbol in word.symbols:
                        print('\tSymbol: {} (confidence: {})'.format(
                            symbol.text, symbol.confidence))
    print (response.full_text_annotation)
