import os, sys
from PIL import Image
import tkinter as tk
from tkinter import filedialog, Text, Label, Entry, Button, Scrollbar, Frame, messagebox, ttk
# import cairosvg
from fpdf import FPDF
from pdf2image import convert_from_path

# Functio to Select files
def select_file():
    global file_paths
    file_paths = filedialog.askopenfilenames(title="Select Files")
    selected_files = ", ".join([os.path.basename(path) for path in file_paths])
    file_label.config(text=f"Selected: {selected_files}")

# Function to Convert the Files to specifc Format
def convert_file():
    for file_path in file_paths:
        try:
            fromFormat = from_var.get().lower()
            toFormat = to_var.get().lower()
            base_file_name = file_path.rsplit('.', 1)[0]

            if fromFormat == 'svg' and toFormat in ['jpg', 'png', 'webp']:
                
                outputFile = file_path.rsplit('.', 1)[0] + '.' + toFormat
                # cairosvg.svg2png(url=file_path, write_to=outputFile)
            elif fromFormat in ['jpg', 'png', 'webp'] and toFormat == 'svg':
                raise ValueError("Converting to SVG is not supported in this example.")
            elif fromFormat == 'pdf' and toFormat in ['jpg', 'png', 'webp']:
                pages = convert_from_path(file_path, 300)
                for i, page in enumerate(pages):
                    outputFile = f"{base_file_name}_page_{i}.{toFormat}"
                    page.save(outputFile, toFormat.upper())
            elif toFormat == 'pdf':
                img = Image.open(file_path)
                pdf = FPDF()
                pdf.add_page()
                pdf.image(file_path, 0, 0, 210, img.height * 210 / img.width)
                outputFile = base_file_name + '.pdf'
                pdf.output(outputFile)
            else:
                with Image.open(file_path) as img:
                    if img.mode == 'RGBA' and toFormat == 'jpg':
                        img = img.convert('RGB')
                    outputFile = file_path.rsplit('.', 1)[0] + '.' + toFormat
                    img.save(outputFile)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to convert file: {os.path.basename(file_path)}: {e}")

    messagebox.showinfo("Success", "All selected files have been converted")
    




root = tk.Tk()
root.title("File Converter")
root.geometry("400x400")

file_paths = []

# File
file_button = Button(root, text="Select File", command=select_file)
file_button.pack()
file_label = Label(root, text="No file selected")
file_label.pack()

# File Converter From Selection
from_label = Label(root, text="From:")
from_label.pack()
from_var = tk.StringVar()
from_dropdown = ttk.Combobox(root, textvariable=from_var, state="readonly")
from_dropdown['values'] = ('JPG', 'PNG', 'SVG', 'WEBP', 'PDF')
from_dropdown.pack()

# File Converter To Selection
to_label = Label(root, text="To:")
to_label.pack()
to_var = tk.StringVar()
to_dropdown = ttk.Combobox(root, textvariable=to_var, state="readonly")
to_dropdown['values'] = ('JPG', 'PNG', 'SVG', 'WEBP', 'PDF')
to_dropdown.pack()

# Converter Button
convert_btn = Button(root, text="Convert File", command=convert_file)
convert_btn.pack()

root.mainloop()