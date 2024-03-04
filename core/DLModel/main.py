import numpy as np
from PIL import Image, ImageFilter
import io
import base64

def blur_image_and_encode(image,radius):
    # Convert image to PIL Image
    image_pil = Image.open(io.BytesIO(image))

    # Convert image to grayscale
    image_gray = image_pil

    # Apply box blur filter to the grayscale image
    blurred_image = image_gray.filter(ImageFilter.BoxBlur(radius=int(radius)))  # You can adjust the radius as needed

    # Convert the blurred image to BytesIO object
    buffered = io.BytesIO()
    blurred_image.save(buffered, format="JPEG")

    # Encode the image as base64 string
    blurred_image_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

    return blurred_image_base64
