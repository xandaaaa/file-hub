from imagedownloader import download_image
from videodownloader import download_youtube_video
from convert import jpg_to_png, png_to_jpg, heic_to_png, heic_to_jpg, mp4_to_mp3

if __name__ == "__main__":

    print("Welcome! Please choose an option:\n")
    print("1 - Download an Image")
    print("2 - Download a Youtube Video")
    print("3 - Convert an Image (Filetype)\n")

    task = input("Enter the number of your choice: ")

    if task not in ["1", "2", "3"]:
        print("Invalid choice, try again.")
        
    # Download Image
    if task == "1":
        url = input("Enter URL: ")
        image_name = input("Save image as (filename): ")
        folder = input('Enter the folder path, if you wish to save it in the same folder (here) type "here": ')

        download_image(url, image_name, folder)

    # Download Youtube Video
    if task == "2":
        url = input("Enter URL: ")
        folder = input('Enter the folder path, if you wish to save it in the same folder (here) type "here": ')
        print("Please choose an option:\n")
        print(" 1 - Full video\n 2 - Specific section\n")

        choice = input("Enter the number of your choice: ")
        if choice == "1":
            download_youtube_video(url, folder, start=None, end=None)
        if choice == "2":
            start = int(input("Please specify the starting point (s): "))
            end = int(input("Please specify the ending point (s): "))
            download_youtube_video(url, folder, start, end)

        if choice not in ["1", "2"]:
            print("Invalid Choice, please try again.")

    # Converts Image (JPG <-> PNG, HEIC -> PNG or JPG, MP4 -> MP3)
    if task == "3":

        file = input("enter file you want to convert: ")
        print("Please choose an option:\n")
        print(" 1 - JPG to PNG\n 2 - PNG to JPG\n 3 - HEIC to PNG\n 4 - HEIC to JPG\n 5 - MP4 to MP3\n")

        convtype = input("Enter the number of your choice: ")
        if convtype == "1":
            jpg_to_png(file)
        if convtype == "2":
            png_to_jpg(file)
        if convtype == "3":
            heic_to_png(file)
        if convtype == "4":
            heic_to_jpg(file)
        if convtype == "5":
            mp4_to_mp3(file)

        if convtype not in ["1", "2", "3", "4", "5"]:
            print("Invalid Choice, please try again.")
