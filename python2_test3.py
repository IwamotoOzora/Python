def image_aspect_ratio(image):
    width, height = image.size
    print("横:{}, 縦:{}".format(width, height))

    x = width % height
    a = width // x
    b = height // x
    aspect_ratio = "{}:{}".format(a, b)
    print("アスペクト比は{}".format(aspect_ratio))

from PIL import Image

image = Image.open("coffee.jpg")
image_aspect_ratio(image) 