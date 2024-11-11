import requests
import shutil
import os
from urllib.parse import urlparse

def download_image(url, image_name, folder):
    """
    Downloads an Image using its URL
    
    Parameters:
        url (str): Link to image address
        image_name (str): New image name
        folder (str, optional): Which folder to download to or create a new one

    """
    # Extracts path part of the URL (includes filetype at the end which is used)
    parsed_url = urlparse(url)
    base_url = parsed_url.path
    new_image_name = os.path.basename(base_url)

    # Extract filetype from the path above
    _, filetype = os.path.splitext(new_image_name)

    # If given name does not specify a filetype, parse it
    if not os.path.splitext(image_name)[1]:
        image_name += filetype

    # Error handler, when URL is invalid return Error
    try:
        res = requests.get(url, stream=True)
        res.raise_for_status() 
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")
        return

    # Save image to this folder
    if folder == "here":
        res = requests.get(url, stream=True)

        with open(image_name,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image sucessfully Downloaded:', image_name)
        return
    
    # Creates a new Folder if folder does not exist
    if not os.path.exists(folder):
        print("creating folder:", folder)
        os.makedirs(folder)

    # saves image to specified folder
    path = os.path.join(folder, image_name)
    res = requests.get(url, stream=True)

    with open(path,'wb') as f:
        shutil.copyfileobj(res.raw, f)
    print('Image sucessfully Downloaded to:', folder)
