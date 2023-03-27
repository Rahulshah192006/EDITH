import imp
import sys
from Auto import Whatsapp,whatsappCall,whatsappVCall
from time import sleep
from NASA import ISSTracker, Nasa , MarsImage,AstroidEarth
import pyttsx3
import speech_recognition as sr
from DataBase.ExtraPro.start import GoogleImage
from Features import Calculator, InternetSpeed, Temp, YoutubeAudio, YoutubeSearch,GoogleSearch,DownloadYouTube,Alarm
from Features import DateConverter
import os
from keyboard import press
from keyboard import press_and_release
import webbrowser
from NASA import Nasa
from lighton import lighton
from lightoff import lightoff
from Features import youtubeInfo
import subprocess


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-2].id)
engine.setProperty('rate',170)
def speak(text):
    subprocess.call(['espeak', '-ven', 'mb-us1', text])

def Takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(": Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print(": Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"Your Command : {query}\n")
    except:
        return ""
    return query.lower()

def Takecommand_Hindi():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(": Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print(": Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"Your Command : {query}\n")
    except:
        return ""
    return query.lower()
speak("Hello boss")
speak("Just checking the drive are working")
speak("calibrating")
speak("Now i am ready boss")
def TaskExe():
    while True:
        query = Takecommand()
        if 'google search' in query:
            GoogleSearch(query)
            GoogleImage()
        elif 'youtube search' in query:
            YoutubeSearch(query)
        elif 'set alarm' in query:
            Alarm(query)
        elif 'download' in query:
            DownloadYouTube()
        elif 'check speed' in query:
            InternetSpeed()
        elif 'temperature' in query:
            Temp(query)
        elif 'calculate' in query:
            Calculator(query)
        elif 'whatsapp message' in query:
            name = query.replace("whatsapp message","")
            name = name.replace("send ","")
            name = name.replace("to ","")
            speak("tell the name boss")
            Name = Takecommand()
            speak(f"Whats The Message For {Name}")
            MSG = Takecommand()
            Whatsapp(Name,MSG)
        elif 'whatsapp call' in query:
            name = query.replace("call ","")
            name = name.replace("edith","")
            Name = Takecommand()
            whatsappCall(Name)
        elif 'whatsapp video call' in query:
            name = query.replace("whatsapp video call ","")
            name = name.replace("edith","")
            speak("Boss tell the name to video call")
            Name = Takecommand()
            whatsappVCall(Name)
        if 'new tab' in query:
            press_and_release('ctrl + t')
        elif 'close tab' in query:
            press_and_release('ctrl + w')
        elif 'source' in query:
            press_and_release('ctrl + u')
        elif 'print out' in query:
            press_and_release('ctrl + p')
        elif 'bookmark' in query:
            press_and_release('ctrl + d')
            press('enter')
        elif 'history' in query:
            press_and_release('ctrl + h')
        elif 'download' in query:
            press_and_release('ctrl + j')
        elif 'new chrome ' in query:
            press_and_release('ctrl + n')
        elif 'previous tab' in query:
            press_and_release('ctrl + shift + t')
        elif 'incognito' in query:
            press_and_release('ctrl + shift + n')
        elif 'switch tab' in query:

            tab = query.replace("switch tab ", "")
            Tab = tab.replace("to","")
            
            num = Tab

            bb = f'ctrl + {num}'

            press_and_release(bb)
        elif 'open' in query:

            name = query.replace("open","")

            NameA = str(name)

            if 'youtube' in NameA:

                webbrowser,open("https://www.youtube.com/")

            elif 'instagram' in NameA:

                webbrowser.open("https://www.instagram.com/")

            else:

                string = "https://www." + NameA + ".com"

                string_2 = string.replace(" ","")

                webbrowser.open(string_2)

        elif 'space news' in query:
            speak("boss Give date to find information for you")
            Date = Takecommand()
            NewDate = DateConverter(Date)
            Nasa(NewDate)
        elif 'mars planet news' in query:
            speak("Boss extracting information from Nasa")
            speak("Extracting from curiosity rover")
            MarsImage()
        elif 'download audio' in query:
            YoutubeAudio()
        elif 'track iss' in query:
            ISSTracker()
        elif 'astroid near me' in query:
            speak("ok boss")
            speak("give me start date and end date for information")
            sDate = input("Enter Start Date : ")
            eDate = input("Enter End Date : ")
            speak("Ok boss")
            AstroidEarth(sDate,eDate)
        elif 'light on' in query:
            speak("Turning Light on")
            lighton()
        elif 'light off' in query:
            speak("Turning Light off")
            lightoff()
        elif 'Youtube information' in query:
            youtubeInfo()


        else:
            speak("Sorry Sir Can't understand")


TaskExe()
