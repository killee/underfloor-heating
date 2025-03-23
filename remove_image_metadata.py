import os
from PIL import Image

def remove_metadata(image_path):
    image = Image.open(image_path)
    data = list(image.getdata())
    image_without_metadata = Image.new(image.mode, image.size)
    image_without_metadata.putdata(data)
    image_without_metadata.save(image_path)

def resize_image(image_path, max_size=(1024, 1024)):
    image = Image.open(image_path)
    image.thumbnail(max_size)
    image.save(image_path)

def process_images(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(directory, filename)
            remove_metadata(image_path)
            resize_image(image_path)
            print(f"Processed {filename}")

if __name__ == "__main__":
    images_directory = os.path.join(os.path.dirname(__file__), 'images')
    process_images(images_directory)
