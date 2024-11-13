from PIL import Image
import pillow_heif
import os
from moviepy.editor import *

# JPG to PNG
def jpg_to_png(file, name):

    image = Image.open(file)
    image = image.convert("RGB")
    
    new_file = name + ".png"
    
    image.save(new_file, "PNG")
    
    print(f"Image successfully converted to: {new_file}")
    return new_file

# PNG to JPG
def png_to_jpg(file, name):

    image = Image.open(file)
    image = image.convert("RGB")
    
    new_file = name + ".jpg"
    
    image.save(new_file, "JPEG")
    
    print("Image successfully converted to:", new_file)
    return new_file

# HEIC to PNG
def heic_to_png(file, name):

    heif_image = pillow_heif.read_heif(file)
    
    image = Image.frombytes(heif_image.mode, heif_image.size, heif_image.data, "raw")

    new_file = name + ".png"
    
    image.save(new_file, "PNG")
    
    print("Image successfully converted to:", new_file)
    return new_file

# HEIC to JPG
def heic_to_jpg(file, name):

    heif_image = pillow_heif.read_heif(file)
    
    image = Image.frombytes(heif_image.mode, heif_image.size, heif_image.data, "raw")

    new_file = name + ".jpg"
    
    image.save(new_file, "JPEG")
    
    print("Video successfully converted to:", new_file)
    return new_file

# MP4 to MP3
def mp4_to_mp3(mp4, mp3_name):

    dir = os.path.dirname(mp4)

    mp3 = os.path.join(dir, f"{mp3_name}.mp3")

    audio = AudioFileClip(mp4)
    audio.write_audiofile(mp3)
    audio.close()

# PNG to PDF
def png_to_pdf(array_of_files, name):

    images = []

    for file in array_of_files:

        img = Image.open(file).convert("RGB")
        aspect_ratio = img.height / img.width
        size = (800, int(800 * aspect_ratio))

        images.append(img.resize(size))

    new_file = name + ".pdf"

    if images:
        images[0].save(new_file, "PDF", resolution=100.0, save_all=True, append_images=images[1:])
        print("Image/s successfully converted to:", new_file)
    
    return new_file

# JPG to PDF
def jpg_to_pdf(array_of_files, name):

    images = []

    for file in array_of_files:

        img = Image.open(file).convert("RGB")
        aspect_ratio = img.height / img.width
        size = (800, int(800 * aspect_ratio))

        images.append(img.resize(size))

    new_file = name + ".pdf"

    if images:
        images[0].save(new_file, "PDF", resolution=100.0, save_all=True, append_images=images[1:])
        print("Image/s successfully converted to:", new_file)
    
    return new_file

#HEIC to PDF
def heic_to_pdf(array_of_files, name):
    
    images = []

    for file in array_of_files:

        heif_image = pillow_heif.read_heif(file)
    
        img = Image.frombytes(heif_image.mode, heif_image.size, heif_image.data, "raw").convert("RGB")
        aspect_ratio = img.height / img.width
        size = (800, int(800 * aspect_ratio))

        images.append(img.resize(size))
    
    new_file = name + ".pdf"

    if images:
        images[0].save(new_file, "PDF", resolution=100.0, save_all=True, append_images=images[1:])
        print("Image/s successfully converted to:", new_file)

        return new_file