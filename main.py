"""
main.py

Create a GIF (Graphics Interchange Format) by combining a list of photos. The only lines needed to change are the ones
under 'CONTROL'.
"""
from glob import glob

from PIL import Image

# --> CONTROL <-- #
file_format = 'png'  # Format of input images
gif_speed = 10  # Duration between each picture
image_path = 'img/example/'  # Path to folder in which images are saved
name = "example"  # Name to which the GIF is saved (in root folder)
slow_end = 0  # Number of times the last picture is repeated before re-starting the GIF
slow_start = 0  # Number of times the first picture is repeated before continuing to the following pictures

# --> CODE <-- #
# Load in the images
images = glob('{path}*.{format}'.format(path=image_path, format=file_format))

# Sort the images
images.sort()

# Enlarge beginning and end of the list to match the slow-start/-end
for _ in range(slow_start):
    images.insert(0, images[0])
for _ in range(slow_end):
    images.append(images[-1])

# Create GIF
img, images = images[0], images[1:]
im1 = Image.open(img)
img_list = [Image.open(i) for i in images]
im1.save("{}.gif".format(name),
         save_all=True,
         append_images=img_list,
         duration=gif_speed,
         loop=0)
