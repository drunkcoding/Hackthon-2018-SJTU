from watson_developer_cloud import VisualRecognitionV3
import json

visual_recognition = VisualRecognitionV3(
    version='2018-06-02',
    url='https://gateway.watsonplatform.net/visual-recognition/api',
    iam_api_key='LZeswBjOVIRsjkvYDIlJaYU6kYrb59eAQh6_7FmTTSTV')  # Optional

with open('./pp.jpg', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        threshold='0.6',
        classifier_ids='food')
    print(json.dumps(classes, indent=2))
