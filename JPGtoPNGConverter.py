'''
A Python script that converts JPG images to PNG

usage: python JPGtoPNGConverter.py <from_this_folder_path> <to_this_folder_path>
'''

# pylint: disable=invalid-name

import sys
import os
from PIL import Image

# Grab first and second arguments
IMAGE_FOLDER = sys.argv[1]
OUTPUT_FOLDER = sys.argv[2]

# Check if new/exists, if not create it
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

# Loop through 'Pokedex'
for filename in os.listdir(IMAGE_FOLDER):
    clean_filename = os.path.splitext(filename)

    img = Image.open(f'{IMAGE_FOLDER}{filename}')

    # Convert images to PNG and save to a new folder
    img.save(f'{OUTPUT_FOLDER}{clean_filename[0]}.png', 'png')
    print(f'{filename} converted...')
