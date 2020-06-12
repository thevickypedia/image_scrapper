from bs4 import *
import requests as r
import os

request = r.get('https://www.akc.org/expert-advice/lifestyle/35-perfect-pictures-of-dogs/')
soup = BeautifulSoup(request.text, "html.parser")

links = []

x = soup.select('img[src^="http://cdn.akc.org/content/article-body-image/"]')

for img in x:
    links.append(img['src'])

os.mkdir('photos')
i = 1

print('Retrieving your images')

for index, img_link in enumerate(links):
    if i <= 10:
        img_data = r.get(img_link).content
        with open("photos/" + str(index + 1) + '.jpg', 'wb+') as f:
            f.write(img_data)
        i += 1
    else:
        f.close()
        break