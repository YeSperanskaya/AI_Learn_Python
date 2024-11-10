# Используйте библиотеку `Pillow` или `opencv-python` для
# загрузки изображения в форматах jpg и png. Если загружен
# файл png, проверьте, содержит ли он прозрачные пиксели
# и если да, то сделайте такие пиксели белыми
# непрозрачными.

import PIL
from PIL import Image

def change_png():
    image_path = "../resources/image.png"
    image = Image.open(image_path)
    if image.format == 'PNG':
        if image.mode == 'RGBA':
            image = image.convert('RGB')
    image.save("../resources/processed_image.png")
    print("Файл успешно обработан!")

change_png()