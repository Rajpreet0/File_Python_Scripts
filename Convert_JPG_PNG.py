import os, sys
from PIL import Image

images = ['test.png']

for infile in images:
    f, e = os.path.splitext(infile)
    outfile = f + '.jpg'
    if infile != outfile:
        try:
            with Image.open(infile) as image:
                in_rgb = image.convert('RGB')
                in_rgb.save(outfile, 'JPEG')
        except OSError:
            print('Conversion failed for', infile)