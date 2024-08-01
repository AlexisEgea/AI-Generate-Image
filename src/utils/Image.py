from PIL import Image
import requests
import os
from io import BytesIO


class ImageGeneration:
    def __init__(self, url):
        self.url = url
        self.image = requests.get(self.url)
        self.file_path = os.getcwd() + "/../data/image/"

    def display_image(self):
        image_data = Image.open(BytesIO(self.image.content))
        image_data.show()
        print("image displayed")

    def save_image(self, file_name):
        file_path = self.file_path + file_name + ".jpg"
        image_data = Image.open(BytesIO(self.image.content))
        image_data.save(file_path)
        print("image saved")
