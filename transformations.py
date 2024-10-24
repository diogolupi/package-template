# image_processing/transformations.py
from PIL import Image

def resize_image(image_path, size):
    img = Image.open(image_path)
    img = img.resize(size)
    img.show()
    return img

def rotate_image(image_path, degrees):
    img = Image.open(image_path)
    img = img.rotate(degrees)
    img.show()
    return img
