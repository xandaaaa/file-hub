from yt_dlp import YoutubeDL
from yt_dlp.utils import download_range_func
import os
import requests

def download_youtube_video(url, folder, start, end):

    # Error handler in case URL is not valid
    try:
        res = requests.head(url, allow_redirects=True)
        res.raise_for_status() 
    except requests.RequestException as e:
        print(f"Error accessing URL: {e}")
        return

    # Saves video to current folder
    if folder == "here":

        # Downloads FULL video to current folder
        if start == None and end == None:
            yt_opts = {
                'outtmpl': f"%(title)s.%(ext)s",
                'format': 'best',
            }

            print("Downloading...")
            YoutubeDL(yt_opts).download([url])
            print("Download complete!")
            return

        # Downloads a section of the video to current folder
        yt_opts = {
            'outtmpl': f"%(title)s.%(ext)s",
            'format': 'best',
            'download_ranges': download_range_func(None, [(start, end)])
        }

        print("Downloading...")
        YoutubeDL(yt_opts).download([url])
        print("Download complete!")
        return
    
    # Creates folder to save the video to in case it does not exist yet
    if not os.path.exists(folder):
        print("creating folder:", folder)
        os.makedirs(folder)

    # Downloads FULL video to specified folder
    if start == None and end == None:
        yt_opts = {
            'outtmpl': f"{folder}/%(title)s.%(ext)s",
            'format': 'best',
        }

        print("Downloading...")
        YoutubeDL(yt_opts).download([url])
        print("Download complete!")
        return
    
    # Downloads a section of the video to specified folder
    yt_opts = {
    'outtmpl': f"{folder}/%(title)s.%(ext)s",
    'format': 'best',
    'download_ranges': download_range_func(None, [(start, end)])
    }

    print("Downloading...")
    YoutubeDL(yt_opts).download([url])
    print("Download complete!")
    return