from PIL import Image
import os

"""
Split each photo in a folder into horizontal halves
"""

DIR = '/Users/samhollenbach/Downloads/5489sam_002318/Export JPG 16Base'

os.mkdir(os.path.join(DIR, 'cropped'))


for file in os.listdir(DIR):
    if not file.endswith('.JPG'):
        continue

    path = os.path.join(DIR, file)

    with Image.open(path) as im:
        width, height = im.size

        (left, upper, right, lower) = (0, 0, int(width/2), height)
        im_crop = im.crop((left, upper, right, lower))
        im_crop.save(os.path.join(DIR, 'cropped', f'left_{file}'))

        (left, upper, right, lower) = (int(width / 2) + 1, 0, width, height)
        im_crop = im.crop((left, upper, right, lower))
        im_crop.save(os.path.join(DIR, 'cropped', f'right_{file}'))