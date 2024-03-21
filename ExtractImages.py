import os
import shutil

source_folder = input('Enter the file where PDF to distract from:  ')
destination_folder = input('Enter the destination path for your PDFs: ')

os.makedirs(destination_folder, exist_ok=True)

for filename in os.listdir(source_folder):
    if filename.endswith('.png'):
        shutil.move(os.path.join(source_folder, filename), destination_folder)
    elif filename.endswith('.jpg'):
        shutil.move(os.path.join(source_folder, filename), destination_folder)
    elif filename.endswith('.webp'):
        shutil.move(os.path.join(source_folder, filename), destination_folder)