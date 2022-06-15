from ast import Try
from bs4 import BeautifulSoup
from random import choice
from string import ascii_uppercase
from threading import Thread

import os
import requests
import urllib.request
import shutil
import random
import time
import cv2
import timeit



# json structure
# plane : urlSceleton
# url sceleton

inputPlanes = [ ("Hawker Siddeley Harrier", "https://www.airfighters.com/photosearch.php?cra=2459&lim=5&dis=tiles&pag=", 2),
                ("Dassault Rafale", "https://www.airfighters.com/photosearch.php?cra=823&lim=5&dis=tiles&pag=", 17),
                ("Saab JS-39 Grippen", "https://www.airfighters.com/photosearch.php?cra=2022&lim=5&dis=tiles&pag=", 19),
                ("Lockheed Martin F35 Lightning II", "https://www.airfighters.com/photosearch.php?cra=2992&lim=5&dis=tiles&pag=", 14),
                ("Boeing FA-18 Hornet", "https://www.airfighters.com/photosearch.php?cra=710&lim=5&dis=tiles&pag=",34),
                ("General Dynamics F-16 Fighting Falcon", "https://www.airfighters.com/photosearch.php?cra=954&lim=5&dis=tiles&pag=", 50),
                ("Grumman F-14 Tomcat", "https://www.airfighters.com/photosearch.php?cra=978&lim=5&dis=tiles&pag=", 18),
                ("Fairchild A-10 Thunderbolt II", "https://www.airfighters.com/photosearch.php?cra=1470&lim=5&dis=tiles&pag=", 18),
                ("Embraer  EMB314 Super Tucano", "https://www.airfighters.com/photosearch.php?cra=6980&lim=5&dis=tiles&pag=", 2),
                ("Eurofighter EF2000 Typhon", "https://www.airfighters.com/photosearch.php?cra=2167&lim=5&dis=tiles&pag=", 77),
                ("Panavia Tornado", "https://www.airfighters.com/photosearch.php?cra=1477&lim=5&dis=tiles&pag=", 50),
                ("Sukhoi Su-25", "https://www.airfighters.com/photosearch.php?cra=1344&lim=5&dis=tiles&pag=", 2),
                ("Sukhoi Su-27", "https://www.airfighters.com/photosearch.php?cra=1346&lim=5&dis=tiles&pag=", 8),
                ("Mikoyan-Gurevich MiG-29", "https://www.airfighters.com/photosearch.php?cra=1175&lim=5&dis=tiles&pag=", 20),
                ("Sukhoi Su-34 Fullback", "https://www.airfighters.com/photosearch.php?cra=1460&lim=5&dis=tiles&pag=", 1),
                ("Mikoyan-Gurevich MiG-31", "https://www.airfighters.com/photosearch.php?cra=2136&lim=5&dis=tiles&pag=", 1)
                ]

def generateRandomString():
    return ''.join(choice(ascii_uppercase) for i in range(16))
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
    return response

def downloadImage(image, planeID):
    response = requests.get(image[0], stream=True)
    realname = ''.join(e for e in image[1] if e.isalnum()).split("by")[0]
    fileName = realname + generateRandomString() + planeID +".jpg"
    print(f"Saving image {fileName}")
    path = os.path.join("D:\\", "Fakultet", "VI projekat", "AirCognition", "dataset", planeID, fileName)
    file = open(path, 'wb')
    response.raw.decode_content = True
    shutil.copyfileobj(response.raw, file)
    #time.sleep(0.05)
    time.sleep(0.05) # potential issue with file moving 
    # try:
    #     img = cv2.imread(path)
    #     cv2.resize(img, (512,512), interpolation = cv2.INTER_AREA)
    # except:
    #      os.remove(path)
    del response

def getPlaneImages(planeData):
    planeId, url, numberOfPages = planeData
    #response = requests.get(url)
    response = sendImageRequest(url)    # spoofin user agent to avoid bot protections
    soup = BeautifulSoup(response.text, "html.parser")
    aas = soup.find_all("a", class_='pgthumb')
    image_info = []
    for i in range(1, numberOfPages+1):
        for a in aas:
            image_tag = a.findChildren("img")
            image_info.append(("http://www.airfighters.com/"+image_tag[0]["src"], image_tag[0]["alt"]))
            print(f"Found image {image_info[-1]}")
    for i in range(0, len(image_info)):
        downloadImage(image_info[i], planeId)
def getPlanesFolders():
    for plane in inputPlanes:
        planeID, url, numberOfPlanes = plane
        if(not os.path.exists(os.path.join("D:\\", "Fakultet", "VI projekat", "AirCognition", "dataset", planeID))):
            os.mkdir(os.path.join("D:\\", "Fakultet", "VI projekat", "AirCognition", "dataset", planeID))
def downloadAllPlanes():
    for plane in inputPlanes:
        planeID, url, numberOfPlanes = plane
        getPlaneImages((planeID, url, numberOfPlanes))

    
if __name__ == "__main__":
    getPlanesFolders()
    startTimer = timeit.default_timer()
    downloadAllPlanes()
    print(f"Time to get all Images: {timeit.default_timer() - startTimer}")
    # url = "https://www.airfighters.com/photosearch.php?cra=823&lim=5&dis=tiles"
    # #response = requests.get(url)
    # response = sendImageRequest(url)    # spoofin user agent to avoid bot protections
    # soup = BeautifulSoup(response.text, "html.parser")
    # aas = soup.find_all("a", class_='pgthumb')

    # image_info = []

    # for a in aas:
    #     image_tag = a.findChildren("img")
        
    #     image_info.append(("http://www.airfighters.com/"+image_tag[0]["src"], image_tag[0]["alt"]))
    #     print(f"Found image {image_info[-1]}")
    # for i in range(0, len(image_info)):
    #     downloadImage(image_info[i])

