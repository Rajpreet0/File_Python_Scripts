import os, sys
from PIL import Image

# List of image files to be converted
images = ['test.png']

# Loop through each image file in the list
for infile in images:
    # Split the file name and extension
    f, e = os.path.splitext(infile)
    # Define the output file name by changing the extension
    outfile = f + '.jpg'
    if infile != outfile:
        try:
            with Image.open(infile) as image:
                in_rgb = image.convert('RGB')  # Convert the image to RGB mode
                in_rgb.save(outfile, 'JPEG')   # Save the converted image as a JPEG file with the output file name
        except OSError:
            print('Conversion failed for', infile)