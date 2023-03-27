from matplotlib import *
import requests
import os
from PIL import Image
import pyttsx3
import random
from datetime import date
import math
#from cartopy.crs import PlateCarree
import matplotlib.pyplot as plt
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-2].id)
engine.setProperty('rate',170)


def speak(text):
    subprocess.call(['espeak', '-ven', 'mb-us1', text])

path = open('D:\\EDITH\\E.D.I.T.H\\DataBase\\API KEYS\\Nasa_Api.txt')
api_key = path.readline()
def Nasa(Date):
    speak('Boss extracting information from Nasa Datebase')
    speak('Extraction is Done Boss I found this')
    url = 'https://api.nasa.gov/planetary/apod?api_key=' + str(api_key)
    parameter = {'date':str(Date)}
    req = requests.get(url,params=parameter)
    Date = req.json()
    exp = Date['explanation']
    title = Date['title']
    copyright = Date['copyright']
    imageHD = Date['hdurl']
    image_r = requests.get(imageHD)
    filename = str(title) + '.jpg'
    with open(filename,'wb') as f:
        f.write(image_r.content)
    default_path = "D:\\ULTRON\\EDITH"
    main_path = "D:\\ULTRON\\EDITH\\DataBase\\Nasa\\Images"
    os.rename(default_path,main_path)
    img = Image.open(main_path)
    img.show()
    speak(f"Boss title is : {title}")
    speak(f"Boss According to Nasa : {exp}")
    speak(f"Boss the image is copyright by : {copyright}")
def MarsImage():
    name = 'curiosity'
    date = '2020-12-3'
    Api = str("pBtGINuCxatsYb2qzYCddXbf0DtaMwV4mi9E2nCH")
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{name}/photos?earth_date={date}&api_key={Api}"
    r = requests.get(url)
    data = r.json()
    Photos = data['photos'][:20]
    try:
        for index,photo in enumerate(Photos):
            Camera = photo['camera']
            rover = photo['rover']
            rover_name = rover['name']
            camera_name = Camera['name']
            full_camera_name = Camera['full_name']
            date_of_photo = photo['earth_date']
            imaage_url = photo['img_src']
            pro = requests.get(imaage_url)
            img = f'{index}.jpg'
            with open(img,'wb') as file:
                file.write(pro.content)
            path_1 = "D:\\EDITH\\E.D.I.T.H\\DataBase\\Nasa\\" + str(img)
            path_2 = "D:\\EDITH\\E.D.I.T.H\\DataBase\\Nasa\\Mars\\" + str(img)
            os.rename(path_1,path_2)
            os.startfile(path_2)
        print(f"This Image Was Captured With : {full_camera_name}")
        print(f"This Image Was Captured On : {date_of_photo}")

    except:
        speak("Something Went wrong")
MarsImage()
def ISSTracker():
    url = "http://api.open-notify.org/iss-now.json"

    r = requests.get(url)

    Data = r.json()

    dt = Data['timestamp']

    lat = Data['iss_position']['latitude']

    lon = Data['iss_position']['longitude']

    print(f"Time And Date : {dt}")
    print(f"Latitude : {lat}")
    print(f"Longitude : {lon}")

    plt.figure(figsize=(10,8))

    ax = plt.axes(projection =PlateCarree())

    ax.stock_img()

    plt.scatter(float(lon),float(lat),color = 'blue' , marker= 'o')

    plt.show()

def AstroidEarth(start_date,end_data):
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_data}&api_key={api_key}"
    r = requests.get(url)
    data = r.json()
    elemen = data['element_count']
    speak('Boss As per Nasa Data : ')
    speak(f'Total objects near earth from {start_date} to {end_data} are {elemen}')
def infobodies():
    url = "https://api.le-system-solaire.net/rest/bodies"
    r = requests.get(url)
    Data = r.json()
    print(Data)
