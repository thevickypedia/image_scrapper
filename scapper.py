import os

import requests as r
from bs4 import BeautifulSoup
from datetime import datetime

request = r.get('https://www.akc.org/expert-advice/lifestyle/35-perfect-pictures-of-dogs/')
soup = BeautifulSoup(request.text, "html.parser")

x = soup.select('img[src^="http://cdn.akc.org/content/article-body-image/"]')

links = []
for img in x:
    links.append(img['src'])

path = 'photos'
isDir = os.path.isdir(path)
if isDir:
    print('Required directory is already available. Skipping folder creation..\n')
else:
    print('Creating a directory\n')
    os.mkdir('photos')

now = datetime.now()
dt_string = now.strftime("%B_%d_%Y_%I:%M:%S_%p")

i = 1
for index, img_link in enumerate(links):
    if i <= 10:
        print(f'Generating file {i}.jpg')
        img_data = r.get(img_link).content
        with open("photos/" + str(index + 1) + '_' + dt_string + '.jpg', 'wb+') as f:
            f.write(img_data)
        i += 1
    else:
        break
