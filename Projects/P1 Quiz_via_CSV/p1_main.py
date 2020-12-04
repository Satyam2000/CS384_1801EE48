#A python project on building a quiz portal for students.
#Project group Members:-
                  # Satyam Kumar (1801EE48)
                  #Kishan Kumar singh (1801EE22)

import os
import csv
import sqlite3
import pandas as pd
import time
import re
import keyboard
import bcrypt
import threading
import getpass as gp
import numpy as np
from tkinter import *
from numpy.core.numeric import roll

global current_path
current_path = os.getcwd() #returns current working directory of a of the system.
global is_keypress
global end_timer
end_timer = False
is_keypress = True

global uanttempted_questions
uanttempted_questions = []

db_connection = sqlite3.connect('project1 quiz cs384.db')
curs = db_connection.cursor()

def timer(quiz):

    time_limit = 0
    access = open(os.path.join(current_path, "quiz_wise_questions", f"q{quiz}.csv"), mode ="r")
    data_frame= pd.read_csv(access)
    data_header = data_frame.columns
    time_limit = str(data_header[10])
    #print("TimeLimit:::::::::::",time_limit)
    pattern = re.compile('\d+')
    time_duration = re.findall(pattern, time_limit)
    root = Tk()
    root.geometry("300x80")
    root.title("Timer")

    minute = StringVar()
    second = StringVar()

    minute.set("00")
    second.set("00")

    minuteEntry = Entry(root, width=3, font=(
        "Arial", 18, ""), textvariable=minute)
    minuteEntry.place(x=100, y=20)

    secondEntry = Entry(root, width=3, font=(
        "Arial", 18, ""), textvariable=second)
    secondEntry.place(x=150, y=20)
    
    duration = (int(time_duration[0]))*60   #Conversion into seconds
    
    while duration > -1:
        mins, secs = divmod(duration, 60)
        if end_timer==True:
        	root.destroy()
        	break
        minute.set("{0:2d}".format(mins))   #formatting the time in 2 decimals
        second.set("{0:2d}".format(secs))
        root.update()
        time.sleep(1)
        duration -= 1