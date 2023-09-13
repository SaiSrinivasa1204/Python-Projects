import datetime
from playsound import playsound

alarmHour = int(input("Please enter the hour: "))
alarmMin = int(input("PLease enter the minutes: "))
alarmAm = input("Please select am/pm: ")

if alarmAm == "pm":
    alarmHour += 12

while True:
    if alarmHour == datetime.datetime.now().hour and alarmMin == datetime.datetime.now().minute:
        print("Playing music")
        playsound("C:\\Users\\lenovo\\Music\\sample music.mp3")
        break
