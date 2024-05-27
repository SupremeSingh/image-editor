# Image Editing and Resizing

This project is designed to resize and edit images for a specific purpose. It is designed to be used as a base for other projects.

## Setup 

To run this project, simply clone the repository and run the `image_resizer.py` file.

```bash
git clone https://github.com/jonathansimpson/image-editing-and-resizing.git
cd image-editing-and-resizing
```

This project uses venv to manage the dependencies. To install the dependencies, run the following command:

```bash
python -m venv venv
source venv/bin/activate
pip install os
pip install Pillow
```

To run the program, finally, use 

```
python src/image_resizer.py
python test/test_image_resizer.py
```

