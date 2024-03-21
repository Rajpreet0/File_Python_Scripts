import os
import shutil

# Prompt the user to input the source folder containing PDF files
source_folder = input('Enter the file where PDF to distract from:  ')
# Prompt the user to input the destination folder path for moving PDF files
destination_folder = input('Enter the destination path for your PDFs: ')

# Create a folder if there isn't a destination folder
os.makedirs(destination_folder, exist_ok=True)

# Iterate over each file in the source folder
for filename in os.listdir(source_folder):
    if filename.endswith('.pdf'):
        shutil.move(os.path.join(source_folder, filename), destination_folder)