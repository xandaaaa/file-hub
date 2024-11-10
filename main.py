from imagedownloader import download_image

if __name__ == "__main__":

    task = input("Enter what you want to do:\n Download an Image: press 1 ")
    
    if task == "1":
        url = input('Enter URL: ')
        image_name = input('Save image as (filename): ')
        folder = input('Enter the folder path, if you wish to save it in the same folder (here) type "here": ')

        download_image(url, image_name, folder)