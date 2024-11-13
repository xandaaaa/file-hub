from imagedownloader import download_image
from videodownloader import download_youtube_video
from convert import *
from pdf import *

if __name__ == "__main__":

    print("Welcome! Please choose an option:\n")
    print("1 - Download an Image")
    print("2 - Download a Youtube Video")
    print("3 - Convert an Image (Filetype)")
    print("4 - Convert a MP4 file to MP3")
    print("5 - Compress a PDF file")
    print("6 - Merge PDF files\n")

    task = input("Enter the number of your choice: ")

    if task not in ["1", "2", "3", "4", "5", "6"]:
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

    # Converts Image (JPG <-> PNG, HEIC -> PNG or JPG, PNG, JPG, HEIC -> PDF)
    if task == "3":

        print("Please choose an option:\n")
        print(" 1 - JPG to PNG\n 2 - PNG to JPG\n 3 - HEIC to PNG\n 4 - HEIC to JPG\n 5 - PNG to PDF\n 6 - JPG to PDF\n 7 - HEIC to PDF\n")

        convtype = input("Enter the number of your choice: ")
        if convtype == "1":
            file = input("Enter file you want to convert: ")
            name = input("Please enter the desired name for the file: ")
            jpg_to_png(file, name)
        if convtype == "2":
            file = input("Enter file you want to convert: ")
            name = input("Please enter the desired name for the file: ")
            png_to_jpg(file, name)
        if convtype == "3":
            file = input("Enter file you want to convert: ")
            name = input("Please enter the desired name for the file: ")
            heic_to_png(file, name)
        if convtype == "4":
            file = input("Enter file you want to convert: ")
            name = input("Please enter the desired name for the file: ")
            heic_to_jpg(file, name)
            
        if convtype == "5":
            array_of_png_files = []
            check = "YES"
            while check == "YES":
                file = input("Input the image you want to convert: ")
                array_of_png_files.append(file)
                check = input('Enter "YES" if you wish to convert more files into the PDF if not press enter: ')
            name = input("Please enter the desired name for the file: ")
            png_to_pdf(array_of_png_files, name)

        if convtype == "6":
            array_of_jpg_files = []
            check = "YES"
            while check == "YES":
                file = input("Input the image you want to convert: ")
                array_of_jpg_files.append(file)
                check = input('Enter "YES" if you wish to convert more files into the PDF if not press enter: ')
            name = input("Please enter the desired name for the file: ")
            jpg_to_pdf(array_of_jpg_files, name)

        if convtype == "7":
            array_of_heic_files = []
            check = "YES"
            while check == "YES":
                file = input("Input the image you want to convert: ")
                array_of_heic_files.append(file)
                check = input('Enter "YES" if you wish to convert more files into the PDF if not press enter: ')
            name = input("Please enter the desired name for the file: ")
            heic_to_pdf(array_of_heic_files, name)

        if convtype not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("Invalid Choice, please try again.")
    
    # Converts video (MP4 file) to audio (MP3 file)
    if task == "4":
        mp4 = input("Please enter the path of the video you want to convert: ")
        mp3 = input("Please enter desired name of the MP3 file: ")
        mp4_to_mp3(mp4, mp3)

    # Compress a PDF file
    if task == "5":
        print("Please choose an option:\n")
        print(" 1 - Remove images\n 2 - Reduce image quality\n 3 - Compress without visible changes\n")

        comptype = input("Enter the number of your choice: ")
        if comptype == "1":
            file = input("Input the PDF file you want to compress: ")
            name = input("Please enter the desired name for the file: ")
            remove_img(file, name)
        if comptype == "2":
            file = input("Input the PDF file you want to compress: ")
            name = input("Please enter the desired name for the file: ")
            quality = int(input("Input the desired Quality of the images in the PDF file (0-100): "))
            reduce_quality_img(file, name, quality)
        if comptype == "3":
            file = input("Input the PDF file you want to compress: ")
            name = input("Please enter the desired name for the file: ")
            compress(file, name)
        
        if comptype not in ["1", "2", "3"]:
            print("Invalid Choice, please try again.")
    
    # Merge PDF files
    if task == "6":
            array_of_pdf_files = []
            check = "YES"
            file = input("Input the first PDF file: ")
            array_of_pdf_files.append(file)
            while check == "YES":
                file = input("Input the next PDF file: ")
                array_of_pdf_files.append(file)
                check = input('Enter "YES" if you wish to add more PDF files if not press enter: ')
            name = input("Please enter the desired name for the merged file: ")
            merge_pdf(array_of_pdf_files, name)