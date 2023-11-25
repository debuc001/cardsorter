# Copyright 2022 Kennet Belenky
#
# This file is part of OpenSorts.
#
# OpenSorts is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# OpenSorts is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# OpenSorts. If not, see <https://www.gnu.org/licenses/>.

import json
import pickle
import platform
import sys
import time

from picamera2 import Picamera2, Preview

import tensorflow as tf
import tensorflow.keras.applications as applications
import tensorflow_addons as tfa
import cv2

import transform
import card_recognizer
import common

#config = common.load_config()
#transform_vector = transform.keypoints_to_transform(640, 448,
#                                                    *config.camera_keypoints)

print('Loading catalog')
json_file = open("card_catalog.json", "r", encoding="utf-8")
catalog = json.load(json_file)
card_lookup = dict()
for card in catalog:
    id = card['id']
    face_index = card['face_index']
    card_id = f'{id}_{face_index}'
    card_lookup[card_id] = card

print('Initializing recognizer.')
recognizer = card_recognizer.Recognizer(catalog)

print('Creating camera.')
picam = Picamera2()
config = picam.create_preview_configuration()
picam.configure(config)

previous_card_id = ''

print('capture image')
picam.start_preview(Preview.QTGL)
picam.start()
time.sleep(2)
picam.capture_file("./tmp/test-python.jpg")
picam.close()

image = cv2.cvtColor("./tmp/test-python.jpg", cv2.COLOR_BGR2RGB)

cv2.imshow("test-python", image)
cv2.waitKey(0)


'''
    image = tfa.image.transform(frame,
                                transform_vector,
                                interpolation='bilinear',
                                fill_value=255,
                                output_shape=(448, 640))
    image, _, _ = transform.automatic_brightness_and_contrast(
        tf.image.convert_image_dtype(image, tf.uint8).numpy())
    image = tf.image.convert_image_dtype(image, tf.float32)
    image = tf.image.rot90(image, k=1)
    card_id, distance = recognizer.recognize(image)

    if card_id != previous_card_id:
        previous_card_id = card_id

        if card_id == 'Unknown':
            print(f'Unknown : {distance}')
        else:
            card = card_lookup[card_id]
            card_name = card['name']
            set_code = card['set']
            print(f'{distance} : {card_name} [{set_code}] : {card_id}')

print('Shutting down.')
'''