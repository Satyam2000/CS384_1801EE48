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

def show_user_data(user_data, skipped):
    os.system('cls' if os.name =='nt'else 'clear')
    print(f"Roll: {user_data[1]}\nName: {user_data[0]}")
    if skipped:
    	print(f"The Unattempted Questions: ", skipped_questions)
    else:
    	print(f"Unattempted Questions: ")
    print("Goto Question: Press Ctrl+Alt+G")
    print("Final Submit: Press Ctrl+Alt+F")
    print("Export Database into CSV: Press Ctrl+Alt+E")
    print()

def store_marks_in_database(roll_no, quiz_no, marks):
    os.chdir(current_path)
    db_connection = sqlite3.connect('project1 quiz cs384.db')
    curs = db_connection.cursor()

    try:
        curs.execute(
            """CREATE TABLE project1_marks
	    	         (roll text, quiz_no integer(2), marks integer(3))"""
        )
    except:
        pass

    if not type(marks) == int:
    	mark = marks.item()
    else:
    	mark = marks
    data = (roll_no, quiz_no)
    curs.execute("DELETE FROM project1_marks WHERE roll=? AND quiz_no=?", data)
    curs.execute("INSERT INTO project1_marks VALUES (?,?,?)",
              (roll_no, quiz_no, mark))
    db_connection.commit()
    db_connection.close()



def pressed_hotkeys():
    tmp = ''
    while is_keypress:
        try:
            if keyboard.is_pressed('ctrl+alt+u') or keyboard.is_pressed('ctrl+alt+U'):
                tmp = 'skip_question'
                return tmp
            elif keyboard.is_pressed('ctrl+alt+e') or keyboard.is_pressed('ctrl+alt+E'):
                tmp = 'export_to_csv'
                return tmp
            elif keyboard.is_pressed('ctrl+alt+g') or keyboard.is_pressed('ctrl+alt+G'):
                tmp = 'goto_question'
                return tmp
            elif keyboard.is_pressed('ctrl+alt+f') or keyboard.is_pressed('ctrl+alt+F'):
                end_timer = True
                tmp = 'final_submit'
                return tmp
            elif keyboard.is_pressed('1'):
            	tmp = '1'
            	print("1")
            	return tmp
            elif keyboard.is_pressed('2'):
            	tmp = '2'
            	print("2")
            	return tmp
            elif keyboard.is_pressed('3'):
            	tmp = '3'
            	print("3")
            	return tmp
            elif keyboard.is_pressed('4'):
            	tmp = '4'
            	print("4")
            	return tmp
            elif keyboard.is_pressed('ctrl+q') or keyboard.is_pressed('ctrl+Q'):
            	tmp = 'q'
            	return tmp
            elif keyboard.is_pressed('s') or keyboard.is_pressed('S'):
            	tmp = 's'
            	print("s")
            	return tmp
        except:
            print("an error occured")
            break

def export_to_csv():
	for i in range(1,4):
		fileName = f"quiz{i}.csv"
		db_link = sqlite3.connect('project1 quiz cs384.db')
		c = db_link.cursor()
		data_to_write = []
		for row in c.execute("SELECT * FROM project1_marks WHERE quiz_no=?", (i,)):
			data_to_write.append(row)
		if not data_to_write == []:
			with open(os.path.join(current_path,"quiz_wise_responses",fileName),mode= "w") as file:
				writer = csv.writer(file)
                # Writing the descriptive header
				writer.writerow(["Roll No.", "Quiz No.", "Marks"])
				writer.writerows(data_to_write)

def start_quiz(quiz, user):
    questions_folder = os.path.join(current_path, "quiz_wise_questions")
    roll_no = user[1]
    quiz_no = quiz
    quiz_number_str=str(quiz_no)
    csv_to_open = "q"+quiz_number_str+".csv"
    os.chdir(questions_folder)
    df_quiz = pd.read_csv(csv_to_open)
    my_choice = 0 
    tmp = ''
    global skipped_questions
    marks_quiz, skipped_questions, responses_for_csv = [], [], []
    no_of_skipped_questions, correct, wrong, total_marks = 0, 0, 0, 0
    show_skipped = False

    while my_choice < df_quiz.shape[0]:
        my_choice += 1
        marks_gained = 0
        show_user_data(user, show_skipped)
        print(f"Question {my_choice}) {df_quiz.question[my_choice-1]}")
        print(f"Option 1) {df_quiz.option1[my_choice-1]}")
        print(f"Option 2) {df_quiz.option2[my_choice-1]}")
        print(f"Option 3) {df_quiz.option3[my_choice-1]}")
        print(f"Option 4) {df_quiz.option4[my_choice-1]}")
        print()
        print(
            f" Marks/Credits if Correct Choice: {df_quiz.marks_correct_ans[my_choice-1]}")
        print(f"Penalty(For the Negative Marking): {df_quiz.marks_wrong_ans[my_choice-1]}")
        iscompulsion_pool = {'n': "No", 'y': "Yes"}
        print(
            f"Is compulsory: {iscompulsion_pool[df_quiz.compulsory[my_choice-1]]}")
        print()

        if iscompulsion_pool[df_quiz.compulsory[my_choice-1]] == "Yes":
            print("Enter Choice (1, 2, 3, 4):  ")
            tmp = pressed_hotkeys()
        else:
            print("Enter Choice (1, 2, 3, 4, S):  ")
            tmp = pressed_hotkeys()
        time.sleep(0.7)

        if tmp == str(df_quiz.correct_option[my_choice-1]):
            marks_gained = df_quiz.marks_correct_ans[my_choice-1]
            correct += 1
        elif tmp == 's':
            # print(tmp)
            skipped_questions.append(my_choice)
            no_of_skipped_questions += 1
            marks_gained = 0
        elif tmp == 'export_to_csv':
        	my_choice -= 1
        	export_to_csv()
        	marks_gained = 0
        elif tmp == 'skip_question':
        	my_choice -= 1
        	show_skipped = True
        elif tmp == 'goto_question':
            my_choice = int(input("Enter the question no. you want to go to :"))
            my_choice -= 1
            continue
        elif tmp == 'final_submit':
        	my_choice -= 1
        	break
        else:
            marks_gained = df_quiz.marks_wrong_ans[my_choice-1]
            wrong += 1
            
        marks_quiz.append(marks_gained)
        if (not my_choice<1) and tmp in ['1','2','3','4','s']:
	        total_marks += df_quiz.marks_correct_ans[my_choice-1]
	        extra = [tmp]
	        responses_for_csv.append(list(df_quiz.loc[my_choice-1][0:-1]))
	        responses_for_csv[my_choice-1] += extra

    header_responses = df_quiz.columns.values
    header_responses = list(header_responses)[:-1]

    additional_header = ['marked choice']
    header_responses = header_responses + additional_header
    # --------------------Changing the path to the individual Response----------------
    os.chdir(current_path)
    os.chdir(os.path.join(current_path, "individual_responses"))
    # --------------------------------------------------------
    total_marks_obtained = my_choice(marks_quiz)
    additional_col = {
        "Total": [correct, wrong, no_of_skipped_questions, total_marks_obtained, total_marks],
        "Legend": ["Correct Choices", "Wrong Choices", "Unattempted", "Marks Obtained", "Total Quiz Marks"]
    }

    new_df = pd.DataFrame(additional_col)
    responses_df = pd.DataFrame(responses_for_csv, columns=header_responses)
    header_responses += ["Total", "Legend"]
    responses_df = pd.concat([responses_df, new_df], axis=1)

    responses_csv_name = "q" + str(quiz_no) + "_" + roll_no + ".csv"
    responses_df.to_csv(responses_csv_name, index=False)

    store_marks_in_database(roll_no, quiz_no, total_marks_obtained)

    show_user_data(user, show_skipped)
    # Summary of the Quiz to the students.
    print(f"Total Quiz Questions: {my_choice}")
    print(f"Total Quiz Questions Attempted: {my_choice - no_of_skipped_questions}")
    print(f"Total Correct Questions: {correct}")
    print(f"Total Wrong Questions: {wrong}")
    print(f"Total Marks Questions: {total_marks_obtained}/{total_marks}\n")