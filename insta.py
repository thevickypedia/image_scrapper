import urllib.request
from bs4 import BeautifulSoup as bs


def extract_dp():
    url = f'https://www.instagram.com/{user_name}/'
    print(f'Connecting to profile {url}')
    response = urllib.request.urlopen(url).read()
    soup = bs(response, 'html.parser')
    meta = soup.find_all('meta', {'property': 'og:image'})
    img_src = meta[0]['content']
    # imgURL = imgURL.replace('s150x150', 's720x720')
    name = url.split('/')[-2]
    img_name = f'{name}.jpg'
    urllib.request.urlretrieve(img_src, img_name)
    print(f'Downloaded image has been saved as {img_name}')


if __name__ == '__main__':
    user_name = input('Enter the username:\n')
    extract_dp()
