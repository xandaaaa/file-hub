from PIL import Image
import pillow_heif
import os
import ffmpeg

# JPG to PNG
def jpg_to_png(file):

    image = Image.open(file)
    
    new_file = os.path.splitext(file)[0] + ".jpg"
    
    image.save(new_file, "PNG")
    
    print(f"Image successfully converted to: {new_file}")
    return new_file

# PNG to JPG
def png_to_jpg(file):

    image = Image.open(file)
    image = image.convert("RGB")
    
    new_file = os.path.splitext(file)[0] + ".jpg"
    
    image.save(new_file, "JPEG")
    
    print("Video successfully converted to:", new_file)
    return new_file

# HEIC to PNG
def heic_to_png(file):

    heif_image = pillow_heif.read_heif(file)
    
    image = Image.frombytes(heif_image.mode, heif_image.size, heif_image.data, "raw")

    new_file = os.path.splitext(file)[0] + ".png"
    
    image.save(new_file, "PNG")
    
    print("Video successfully converted to:", new_file)
    return new_file

# HEIC to JPG
def heic_to_jpg(file):

    heif_image = pillow_heif.read_heif(file)
    
    image = Image.frombytes(heif_image.mode, heif_image.size, heif_image.data, "raw")

    new_file = os.path.splitext(file)[0] + ".jpg"
    
    image.save(new_file, "JPEG")
    
    print("Video successfully converted to:", new_file)
    return new_file

# MP4 to MP3
def mp4_to_mp3(file):

    new_file = os.path.splitext(file)[0] + ".mp3"

    ffmpeg.input("video.mp4").output("audio.mp3").run()

    print("Video successfully converted to:", new_file)
    return new_file