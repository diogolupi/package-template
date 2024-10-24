# image_processing/filters.py
from PIL import Image, ImageFilter

def apply_filter(image_path, filter_type):
    img = Image.open(image_path)
    if filter_type == 'BLUR':
        img = img.filter(ImageFilter.BLUR)
    elif filter_type == 'CONTOUR':
        img = img.filter(ImageFilter.CONTOUR)
    img.show()
    return img
