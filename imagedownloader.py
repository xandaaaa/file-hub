import requests
import shutil
import os

def download_image(url, image_name, folder):

    # Extract type of file
    _, filetype = os.path.splitext(url)

    if not os.path.splitext(image_name)[1]:
        image_name += filetype

    # save img to folder
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

    # save img
    path = os.path.join(folder, image_name)
    res = requests.get(url, stream=True)

    if res.status_code == 200:
        with open(path,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image sucessfully Downloaded:', path)
    else:
        print('Image Couldn\'t be retrieved')