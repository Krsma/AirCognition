from bs4 import BeautifulSoup

import requests
import urllib.request
import shutil


# F35, F16, F15, F14, A10
# Su27, MiG31, Su25, Su35, Mig29
# Rafale, Typhon, Saab Gripen, Super Tucano
# Panavia Tornado, J10, Harier

# ubaci humani delay








def download_image(image):
    response = requests.get(image[0], stream=True)
    realname = ''.join(e for e in image[1] if e.isalnum())
    print(f"Saving image {realname}")
    file = open("../dataset/rafale/{}.jpg".format(realname), 'wb')
    response.raw.decode_content = True
    shutil.copyfileobj(response.raw, file)
    del response

if __name__ == "__main__":
    url = "https://www.airfighters.com/photosearch.php?cra=823&lim=5&dis=tiles"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    aas = soup.find_all("a", class_='pgthumb')

    image_info = []

    for a in aas:
        image_tag = a.findChildren("img")
        
        image_info.append(("http://www.airfighters.com/"+image_tag[0]["src"], image_tag[0]["alt"]))
        print(f"Found image {image_info[-1]}")
    for i in range(0, len(image_info)):
        download_image(image_info[i])

