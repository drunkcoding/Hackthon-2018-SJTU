from watson_developer_cloud import VisualRecognitionV3
import json

from nutrition.nutrition import scrap_nutrition

visual_recognition = VisualRecognitionV3(
    version='2018-06-02',
    url='https://gateway.watsonplatform.net/visual-recognition/api',
    iam_api_key='LZeswBjOVIRsjkvYDIlJaYU6kYrb59eAQh6_7FmTTSTV')  # Optional

with open('./kettle.jpg', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        threshold='0.55',
        classifier_ids=['food', 'sample_2129989401'])

classifiers = classes['images'][0]['classifiers']

food_classes = classifiers[0]['classes']
simple_classes = classifiers[1]['classes']


max = 0
for dict in food_classes:
    if (dict['score'] > max):
        max = dict['score']
        food_type = dict['class']

max = 0
for dict in simple_classes:
    if (dict['score'] > max):
        max = dict['score']
        simple_type = dict['class']

if (food_type == 'non-food'):
    print(simple_type)
else:
    nList = scrap_nutrition(food_type)

print(nList)

print(food_type)
print(simple_type)
