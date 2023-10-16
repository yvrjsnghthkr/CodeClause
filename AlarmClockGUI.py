import tkinter as tk
from tkinter import ttk
import time
import beepy

def SettingAlarm():
    alarm_time = InputAlarm.get()
    LocalTime = time.strftime("%H:%M:%S")
    
    while LocalTime != alarm_time:
        LocalTime = time.strftime("%H:%M:%S")
        currentTimeL.config(text=LocalTime)
        root.update()
        time.sleep(1)
    
    status.config(text="Alarm is ringing!")
    beepy.beep(sound=2)
    beepy.beep(sound="coin")

#Main Windowww (in Macc)
root = tk.Tk()
root.title("Alarm Clock")
root.geometry('400x280')
root.iconbitmap('../Alaram-Clock-UI/favicon.ico')

title = ttk.Label(root, text="Alarm Clock", font=('Aerial', 22) )
title.pack(pady=10)

alarmTimeL = ttk.Label(root, text="Set Alarm (HH:MM:SS)", foreground='red', font=('Aerial', 15))
alarmTimeL.pack(pady=20)

InputAlarm = ttk.Entry(root, justify='center', width=50, font=('Aerial', 10))
InputAlarm.pack(padx=20)

SetAlarm = ttk.Button(root, text="Set Alarm", command=SettingAlarm)
SetAlarm.pack(pady=10)

status = ttk.Label(root, text="", font=("Eras Bold ITC", 12))
status.pack(pady=10)

currentTimeL = ttk.Label(root, text="", font=("Eras Bold ITC", 12))
currentTimeL.pack()
root.mainloop()
