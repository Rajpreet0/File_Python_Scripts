import os
import shutil

# Prompt the user to input the source folder containing PDF files
source_folder = input('Enter the file where PDF to distract from:  ')
# Prompt the user to input the destination folder path for moving PDF files
destination_folder = input('Enter the destination path for your PDFs: ')

# Create the destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Iterate over each file in the source folder
for filename in os.listdir(source_folder):
    if filename.endswith('.png'):  # Check if the file ends with '.png'
        shutil.move(os.path.join(source_folder, filename), destination_folder)  # Move the file to the destination folder using shutil.move()
    elif filename.endswith('.jpg'):
        shutil.move(os.path.join(source_folder, filename), destination_folder)
    elif filename.endswith('.webp'):
        shutil.move(os.path.join(source_folder, filename), destination_folder)