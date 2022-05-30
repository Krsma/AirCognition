from bs4 import BeautifulSoup

import requests
import urllib.request
import shutil
import random

# F35, F16, F15, F14, A10
# Su27, MiG31, Su25, Su35, Mig29
# Rafale, Typhon, Saab Gripen, Super Tucano
# Panavia Tornado, J10, Harier

# ubaci humani delay


#json structure
# plane : urlSceleton
# url sceleton



def sendImageRequest(url):
    UAS = ("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1", 
       "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
       "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
       )

    ua = UAS[random.randrange(len(UAS))]

    headers = {'user-agent': ua}
    response = requests.get(url, headers=headers)

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
    #response = requests.get(url)
    response = sendImageRequest(url)    # spoofin user agent to avoid bot protections
    soup = BeautifulSoup(response.text, "html.parser")
    aas = soup.find_all("a", class_='pgthumb')

    image_info = []

    for a in aas:
        image_tag = a.findChildren("img")
        
        image_info.append(("http://www.airfighters.com/"+image_tag[0]["src"], image_tag[0]["alt"]))
        print(f"Found image {image_info[-1]}")
    for i in range(0, len(image_info)):
        download_image(image_info[i])

