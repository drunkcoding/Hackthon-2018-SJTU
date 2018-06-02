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

print(classifiers)

food_classes = classifiers[0]['name']
simple_classes = classifiers[1]['classes']

food_type = simple_type = None
nList = None

max_t = 0
for element in food_classes:
    if (element['score'] > max_t):
        max_t = element['score']
        food_type = element['class']

max_t = 0
for element in simple_classes:
    if (element['score'] > max_t):
        max_t = element['score']
        simple_type = element['class']


if (food_type == 'non-food'):
    print(simple_type)
else:
    nList = scrap_nutrition(food_type)

print(nList)

print(food_type)
print(simple_type)
