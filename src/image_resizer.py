import os
from PIL import Image

INPUT_FOLDER = 'img_input'
OUTPUT_FOLDER = 'img_output'

def crop_to_center(img, target_size):
    """Crop the image to the specified dimensions centered on the original image."""
    width, height = img.size
    if width == height:
        return img  # Already square, no need to crop
    elif width > height:
        left = (width - height) / 2
        right = (width + height) / 2
        top = 0
        bottom = height
    else:
        top = (height - width) / 2
        bottom = (height + width) / 2
        left = 0
        right = width

    return img.crop((left, top, right, bottom))

def resize_and_process_images():
    # Ensure output directory exists
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    # Process each image in the input directory
    for filename in os.listdir(INPUT_FOLDER):
        input_path = os.path.join(INPUT_FOLDER, filename)
        output_path = os.path.join(OUTPUT_FOLDER, filename)

        try:
            # Open the image
            with Image.open(input_path) as img:
                # Crop to square if necessary
                img_cropped = crop_to_center(img, min(img.size))
                # Resize to 1080x1080
                img_resized = img_cropped.resize((1080, 1080))
                img_resized.save(output_path)
        except Exception as e:
            print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    resize_and_process_images()

