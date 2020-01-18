import os, io
from google.cloud import vision
from google.cloud.vision import types
import json

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "{type: service_account,project_id: ml-webapp-uzairmahmed,private_key_id: b177a316429150ad5423fb318df158369baff68c,private_key: -----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCz+CJRiz8gQKq9\npge545SlmW5BvHveXK4HEIaARfi+qE2cOMu7/8UJVqRgiSmSsESeV0NzEWqsWASZ\nRxJ087DWimEtQnVo/mIQHzY01taYay6uO+ET5KPkltWXF0ZN3r8oJ5bfomq/Mp6b\nDXnT5vjaST9q0vEI/5Vkxxvixjbf33DZuk6NwdI/omXygHoYdzIJ6qgmeSRT8Rfg\nMeq5PCIPdWRcWjDADchAIxgjswZN42wjbXIyGcuCm28XTYaMFv8SnhlPSs40hPUx\nlHyVKdMs2fmWjl44C99WbT7x4Q6uS5DKZqePu3jQWQ1lVgPhPz7INhCsemXeKXyA\nEvfF0Am/AgMBAAECggEARyJc7j5LxUPKOQvXIfKCXrI2kmUd0NZxMvmlMC54E2QS\nyRzp6nU+PGKytjWA6Soi9TMoxeKsd1KS/sLI2NE5pJMtteX+4nEp8ZVkp54DVFuJ\nJ/UjEendngzAf+gDMeRJSmXbjKl15/zqE/9PmCJDWoR5PJAEFbpwIlVRAGG4buQI\nqodgvLM8qJz0enwzoHZfVI455Z4bjqKBuyeb3aEq8XHXiLY5rNE4cLuGj8PPsngG\n4yhFpGL40qBEgYCayKdp5VZnBQ+9EgI+KA2fFb0r17aDbkTgnLT2jlkSMnWRu1JJ\ns7IAlPJw8lMisNhPuDLIC0ixX1czdf0YPYx+JUI/AQKBgQDgvQXctTynVv1yvs9p\nFi/a0GKDZol1NWVljj3KKnDNsyexwhJDmKqY+KyDQ3scUeH+UYazP1IwEashki+H\nFi8h7m6OXAOVfFkYDze41geZ+13/DWqP8mYZhnYlIj87iIQL4YZ4GHuc3SDy0p3k\nnnX7645AOv21BZp6jwp6+YZC+QKBgQDNAN/5oe3AiJGwFaRG9imdo6fxAXpYgCBT\n8bkUA60LH8ZBmVq4Jx8j4AMUhu9XV8xdlLdhX3uT9D+cFtr9oTWigpTvZx10yeNI\ntrkJmnx+4ICcuM+JoZ6f/QiloqYNfGQCt0SNAWsgXrO0s/lryXtN8xoC9oqT7/SK\nI0TuyXAodwKBgA54nXQEx48O7usAlmJx50rzuCQ16gv+EDVl31yxNupH6vprQLnR\njsqi2JjrM3YzX5X8sevA3A30VUyoGR9dslNBAyVvj1uE0kfWUwQ34+1qXjcaKg5y\n0Vg7bEgf2GqA89+/+eSpzuve4UxBe6FJAtfh5xsDsWqCndvechJRFvAhAoGBAMHo\nf/K6Lg8dnuB1uAu/MCIB+QrIIRexKeL9E9lQmM+a4IaQLfVeW+AtNfymnaF6VL53\nuvWJwXRzZe+Y1s9tOzRaW9IPMReVFz1iSKhCzlucs0qKrRQ8IbSnPRSfQn4jGN5Q\nx7CwlMnrigP08In57H4Q4pvG49GG+UHoln1fYI2FAoGATHgm8TRjoobYOZBNBp/T\nvloXNJFJTC145L22XuUaNdK62Rny2tTGk2xuqOsr8UYWz87PsKLfkWvgGOCp68r1\nH/R8hOkhtxRobn0mtxMAkQV/+3wbnMfVE2yflqa7hIQK5Z92VlQUl7cmbD8R/W8S\nJMtA/HtsY1O9F1wBqnHwGRQ=\n-----END PRIVATE KEY-----\n,client_email: ocr-uofthacks@ml-webapp-uzairmahmed.iam.gserviceaccount.com,client_id: 111164301071160630481,auth_uri: https://accounts.google.com/o/oauth2/auth,token_uri: https://oauth2.googleapis.com/token,auth_provider_x509_cert_url: https://www.googleapis.com/oauth2/v1/certs,client_x509_cert_url: https://www.googleapis.com/robot/v1/metadata/x509/ocr-uofthacks%40ml-webapp-uzairmahmed.iam.gserviceaccount.com}"

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
