# -*- coding: utf-8 -*-

from PIL import Image

def crop(image_path, coords, saved_location):
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)
    cropped_image.show()


if __name__ == '__main__':
    img=input('enter image file name')
    image = img
    left = int(input('left'))
    top = int(input('top'))
    right = int(input('right'))
    bottom = int(input('bottom'))
    crop(image, (left, top, right, bottom), 'cropped.jpg')