import requests
import shutil

url = input('enter url: ')

file_name = input('save image as (filename and type): ')

res = requests.get(url, stream=True)

if res.status_code == 200:
    with open(file_name,'wb') as f:
        shutil.copyfileobj(res.raw, f)
    print('Image sucessfully Downloaded: ',file_name)
else:
    print('Image Couldn\'t be retrieved')