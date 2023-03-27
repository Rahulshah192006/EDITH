import os 
from playsound import playsound
import datetime

EXT = open("D:\\ULTRON\\EDITH\\Data.txt",'rt')
time = EXT.read()
Time = str(time)
DT = open("D:\\ULTRON\\EDITH\\Data.txt",'r+')
DT.truncate(0)
DT.close()

def ringNow(time):
    time_to_set = str(time)
    time_now = time_to_set.replace("edith","")
    time_now = time_now.replace("set alarm for ","")
    time_now = time_now.replace("set ","")
    time_now = time_now.replace("alarm ","")
    time_now = time_now.replace("for ","")
    time_now = time_now.replace(" and ",":")
    Alarm_Time = str(time_now)
    while True:
        CT = datetime.datetime.now().strftime("%H:%M")
        if CT == Alarm_Time:
            print("WAKE UP BOSS")
            playsound("D:\\ULTRON\\EDITH\\DataBase\\AlarmSound\\AlarmSound.mp3")
        elif CT>Alarm_Time:
            break
ringNow(Time)