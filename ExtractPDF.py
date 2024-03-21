import os
import shutil

source_folder = input('Enter the file where PDF to distract from:  ')
destination_folder = input('Enter the destination path for your PDFs: ')

# Create a folder if there isn't a destination folder
os.makedirs(destination_folder, exist_ok=True)

for filename in os.listdir(source_folder):
    if filename.endswith('.pdf'):
        shutil.move(os.path.join(source_folder, filename), destination_folder)