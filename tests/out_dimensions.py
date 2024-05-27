from PIL import Image
import os

def check_images(directory):
    first_dimensions = None
    all_square = True
    all_same_dimensions = True

    for filename in os.listdir(directory):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_path = os.path.join(directory, filename)
            with Image.open(image_path) as img:
                width, height = img.size

                # Check if the image is square
                if width != height:
                    all_square = False
                    print(f"{filename} is not square.")

                # Check if all images have the same dimensions
                if first_dimensions is None:
                    first_dimensions = (width, height)
                elif (width, height) != first_dimensions:
                    all_same_dimensions = False
                    print(f"{filename} does not match the dimensions of the first image.")

    return all_square, all_same_dimensions

# Directory containing the images
image_directory = 'img_output'

# Perform the checks
square, same_dimensions = check_images(image_directory)
print(f"All images square: {square}")
print(f"All images have the same dimensions: {same_dimensions}")

