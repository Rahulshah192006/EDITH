from os import name, startfile
from time import sleep
from cv2 import solveP3P
from keyboard import press,write
from keyboard import press_and_release
import pyautogui as pa
import webbrowser
import os
import subprocess


def speak(text):
    subprocess.call(['espeak', '-ven', 'mb-us1', text])

searchBar = pa.locateCenterOnScreen('D:\\EDITH\\E.D.I.T.H\\DataBase\\PyAutoGui\\Whatsapp\\BAR.png')
Videocall = pa.locateCenterOnScreen('D:\\EDITH\\E.D.I.T.H\\DataBase\\PyAutoGui\\Whatsapp\\VideoCall.png')
messageBar = pa.locateCenterOnScreen('D:\\EDITH\\E.D.I.T.H\\DataBase\\PyAutoGui\\Whatsapp\\messageBar.png')
call = pa.locateCenterOnScreen('D:\\EDITH\\E.D.I.T.H\\DataBase\\PyAutoGui\\Whatsapp\\Call.png')


def Whatsapp(name,message):
    startfile("C:\\Users\\rahul\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(1)
    pa.moveTo(searchBar)
    pa.click()
    write(name)
    press('enter')
    sleep(1)
    pa.moveTo(messageBar)
    pa.click()
    sleep(1)
    write(message)
    press('enter')


def whatsappVCall(name):
    startfile("C:\\Users\\rahul\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(1)
    pa.moveTo(searchBar)
    pa.click()
    write(name)
    press('enter')
    sleep(0.5)
    pa.moveTo(Videocall)
    pa.click()
    speak("Done Boss video call is on")


def whatsappCall(name):
    name = name.replace("call","")
    startfile("C:\\Users\\rahul\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    rr = open('D:\\ULTRON\\EDITH\\call.log','a')
    rr.write(name)
    rr.close()
    pa.moveTo(searchBar)
    pa.click()
    sleep(0.5)
    write(name)
    press('enter')
    sleep(0.5)
    pa.moveTo(call)
    pa.click()
    speak(f'voice call to {name} has been initiatived')
