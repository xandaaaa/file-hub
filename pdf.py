import os
from pypdf import PdfWriter, PdfMerger

# Removes images from PDF file
def remove_img(file, name):

    original_size = os.path.getsize(file)

    new_file = name + ".pdf"

    writer = PdfWriter(clone_from=file)
    writer.remove_images()

    with open(new_file, "wb") as f:
        writer.write(f)

    new_size = os.path.getsize(new_file)

    print(f"Original file size: {original_size / (1024 * 1024):.2f} MB")
    print(f"Compressed file size: {new_size / (1024 * 1024):.2f} MB")
    print("PDF successfully compressed to: ", new_file)

# Reduces image quality
def reduce_quality_img(file, name, quality):

    original_size = os.path.getsize(file)

    new_file = name + ".pdf"

    writer = PdfWriter(clone_from=file)

    for page in writer.pages:
        for img in page.images:
            img.replace(img.image, quality=quality)

    with open(new_file, "wb") as f:
        writer.write(f)

    new_size = os.path.getsize(new_file)

    print(f"Original file size: {original_size / (1024 * 1024):.2f} MB")
    print(f"Compressed file size: {new_size / (1024 * 1024):.2f} MB")
    print("PDF successfully compressed to: ", new_file)

# Lossless compression
def compress(file, name):

    original_size = os.path.getsize(file)

    new_file = name + ".pdf"

    writer = PdfWriter(clone_from=file)

    for page in writer.pages:
        page.compress_content_streams()

    with open(new_file, "wb") as f:
        writer.write(f)

    new_size = os.path.getsize(new_file)

    print(f"Original file size: {original_size / (1024 * 1024):.2f} MB")
    print(f"Compressed file size: {new_size / (1024 * 1024):.2f} MB")
    print("PDF successfully compressed to: ", new_file)

# Merge PDF files
def merge_pdf(array_of_files, name):

    merger = PdfWriter()

    new_file = name + ".pdf"

    for pdf in array_of_files:
        merger.append(pdf)

    merger.write(new_file)
    merger.close()