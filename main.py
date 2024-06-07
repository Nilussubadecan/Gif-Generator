import imageio.v2 as imageio
import numpy as np
from PIL import Image
import os

def create_gif(image_files, gif_filename, frame_duration):
    images = []
    for filename in image_files:
        if not os.path.exists(filename):
            print(f"File not found: {filename}")
            continue

        image = imageio.imread(filename)
        images.append(image)

    if not images:
        print("No images to process.")
        return

    # Ensure all images have the same shape
    shapes = [img.shape for img in images]
    if len(set(shapes)) != 1:
        # Resize images to the smallest shape
        min_shape = min(shapes, key=lambda x: (x[0], x[1]))
        resized_images = []
        for img in images:
            resized_img = np.array(Image.fromarray(img).resize((min_shape[1], min_shape[0])))
            resized_images.append(resized_img)
        images = resized_images

    imageio.mimsave(gif_filename, images, duration=frame_duration, format='GIF')

def get_image_paths():
    image_files = []
    while True:
        path = input("Please enter the path of an image file (or 'done' to finish): ")
        if path.lower() == 'done':
            break
        # Remove leading and trailing quotes if present
        path = path.strip('\'"')
        if os.path.exists(path):
            image_files.append(path)
        else:
            print(f"File not found: {path}")
    return image_files

def get_frame_duration():
    while True:
        try:
            duration = float(input("Please enter the frame duration (in seconds): "))
            if duration > 0:
                return duration
            else:
                print("Duration must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Get image paths from the user
image_files = get_image_paths()

# Get frame duration from the user
frame_duration = get_frame_duration()

gif_filename = 'output.gif'

if image_files:
    create_gif(image_files, gif_filename, frame_duration)
else:
    print("No valid image files were provided.")
