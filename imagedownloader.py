import requests
import shutil
import os

def download_image(url, image_name, folder):

    if folder == "here":

        res = requests.get(url, stream=True)

        if res.status_code == 200:
            with open(image_name,'wb') as f:
                shutil.copyfileobj(res.raw, f)
            print('Image sucessfully Downloaded: ',image_name)
        else:
            print('Image Couldn\'t be retrieved')
        return
    
    if not os.path.exists(folder):
        print("creating folder...")
        os.makedirs(folder)

    path = os.path.join(folder, image_name)

    res = requests.get(url, stream=True)

    if res.status_code == 200:
        with open(path,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image sucessfully Downloaded: ',path)
    else:
        print('Image Couldn\'t be retrieved')

if __name__ == "__main__":

    url = input('Enter URL: ')
    image_name = input('Save image as (filename and type): ')
    folder = input('Enter the folder path, if you wish to save it in the same folder (here) type "here": ')

    download_image(url, image_name, folder)