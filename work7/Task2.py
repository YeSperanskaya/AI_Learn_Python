from PIL import Image

from skimage.filters import gaussian
from skimage import io
import numpy as np
def resize_image(image_path, new_width, new_height):
    image = Image.open(image_path)
    resized_image = image.resize((new_width, new_height), Image.LANCZOS)
    resized_image.save("../resources/resized_image.png")

def convert_to_black_white(image_path):
    image = Image.open(image_path)
    image = image.convert('1')
    image.save("../resources/black_white_image.png")

def blur_image(image_path):
    image = io.imread(image_path)
    blur = gaussian(image, sigma=2, multichannel=True)
    blur = blur.astype(np.uint8)
    io.imsave('../resources/blurred_image.png', blur, check_contrast=False)


image_path = "../resources/processed_image.png"
new_width = 300
new_height = 200

resize_image(image_path, new_width, new_height)
convert_to_black_white(image_path)
blur_image(image_path)
