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
        
def load_reg_data():
    users_data = []
    db_connection = sqlite3.connect("project1 quiz cs384.db")
    curs = db_connection.cursor()

    try:
        curs.execute(
            """CREATE TABLE project1_registration
	    	         (name text, roll text, password text, contact integer(10))"""
        )
    except:
        pass

    for data in curs.execute("SELECT * FROM project1_registration"):
        users_data.append(data)
    db_connection.close()

    return users_data


def getusr_check():

    reg_users = load_reg_data()
    reg_roll_nos = []
    for data in reg_users:
        reg_roll_nos.append(data[1])

    username = input("Registered Username: ")
    if username in reg_roll_nos:
        password = gp.getpass("Password: ")
        if bcrypt.checkpw(password.encode('utf-8'), reg_users[reg_roll_nos.index(username)][2]):
            print("Succesfully logged in!")
            return reg_users[reg_roll_nos.index(username)]
        else:
            print("Wrong Password")
    else:
        print("\n The above username is not registered : Redirecting to the Registration portal")
        usr_detail = register_user()
        return usr_detail

def give_option():
    my_option = input("Please press 1 to Register(For First time user):\nPress 2 to login:")
    if my_option =='2':
        return getusr_check()
    elif my_option == '1':
        return register_user()

def register_user():
    print("The User Name is not Registered: ")
    reg_users = load_reg_data()
    reg_roll_nos = []
    for data in reg_users:
        reg_roll_nos.append(data[1])

    username = input("Registered Username: ")
    if username in reg_roll_nos:
        print("Username Already Exist: Redireecting to the Login portal:")
        return getusr_check()

    name = input("Enter Name: ")
    roll_no = input("Enter Roll No.: ")
    contact_no = int(input("Contact No/WhatsApp Number: "))
    password = gp.getpass("Password: ")
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    db_connection = sqlite3.connect("project1 quiz cs384.db")
    curs = db_connection.cursor()
    curs.execute(
        "INSERT INTO project1_registration VALUES (?,?,?,?)",
        (name, roll_no, hashed_pw, contact_no),
    )
    db_connection.commit()
    db_connection.close()
    print("You have Successfully registered!")
    return (name, roll_no, hashed_pw, contact_no)
