import os
import time
import sqlite3
import csv
import bcrypt
import time
import getpass as gp
import pandas as pd
from tkinter import *

global path
path = os.getcwd()

def create_load_reg_data():
    users_data = []
    filename = sqlite3.connect("project1 quiz cs384.db")
    c = filename.cursor()

    try:
        c.execute(
            """CREATE TABLE project1_registration
	    	         (name text, roll text, password text, contact integer(10))"""
        )
    except:
        pass

    for row in c.execute("SELECT * FROM project1_registration"):
        users_data.append(row)
    filename.close()

    return users_data


# print(users_data)
# exit()

# currPath = os.getcwd()


def timer(t):
	root = Tk()
	root.geometry("300x80")
	root.title("Time Counter")

	minute = StringVar()
	second = StringVar()

	minute.set("00")
	second.set("00")

	minuteEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=minute)
	minuteEntry.place(x=100, y=20)

	secondEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=second)
	secondEntry.place(x=150, y=20)

	while t > -1:
	    mins, secs = divmod(t, 60)
	    minute.set("{0:2d}".format(mins))
	    second.set("{0:2d}".format(secs))
	    root.update()
	    time.sleep(1)
	    t -= 1


def register_login():

    reg_users = create_load_reg_data()
    reg_roll_no = []
    for r in reg_users:
        reg_roll_no.append(r[1])

    name = ""
    roll_no = ""
    password = ""
    contact_no = 0

    username = input("Username: ")
    if username in reg_roll_no:
        # print("Password: ")
        password = gp.getpass("Password:")
        # print(hashed_pw)

        if bcrypt.checkpw(password, reg_users[reg_roll_no.index(username)][2]):
            print("Succesfully logged in!")
            return reg_users[reg_roll_no.index(username)]
        else:
            print("Wrong Password")
    else:
        print("User is not registered. Kindly register.")
        name = input("Name: ")
        roll_no = input("Roll No.: ")
        contact_no = int(input("Contact No.: "))
        password = gp.getpass("Password:")
        hashable_pw = bytes(password, encoding="utf-8")
        hashed_pw = bcrypt.hashpw(hashable_pw, bcrypt.gensalt())
        conn = sqlite3.connect("project1 quiz cs384.db")
        c = conn.cursor()
        c.execute(
            "INSERT INTO project1_registration VALUES (?,?,?,?)",
            (name, roll_no, hashed_pw, contact_no),
        )
        conn.commit()
        conn.close()
        print("Successfully registered!")
        return (name, roll_no, hashed_pw, contact_no)
        

def print_user_data(user_data):
	uanttempted_ques = []
	os.system('clear')
	print(f"Roll: {user_data[1]}\nName: {user_data[0]}")
	print(f"Unattempted Questions: ", uanttempted_ques)
	print("Goto Question: Press Ctrl+Alt+G")
	print("Final Submit: Press Ctrl+Alt+F")
	print("Export Database into CSV: Press Ctrl+Alt+E")
	print()


def save_marks_in_database(roll_no, quiz_no, marks):
	os.chdir(path)
	# print("MARKS: ", type(marks.item()))
	conn = sqlite3.connect('project1 quiz cs384.db')
	c = conn.cursor()

	try:
		c.execute(
            """CREATE TABLE project1_marks
	    	         (roll text, quiz_no integer(2), marks integer(3))"""
        )
	except:
		pass

	data = (roll_no, quiz_no)
	c.execute("DELETE FROM project1_marks WHERE roll=? AND quiz_no=?", data)
	c.execute("INSERT INTO project1_marks VALUES (?,?,?)", (roll_no, quiz_no, marks.item()))
	conn.commit()
	conn.close()


def print_marks_from_database(roll_no):
	os.chdir(path)
	conn = sqlite3.connect('project1 quiz cs384.db')
	c = conn.cursor()

	users_data = []

	roll = (roll_no,)
	for row in c.execute("SELECT * FROM project1_marks WHERE roll=?", roll):
		users_data.append(row)

	print(users_data)


def start_quiz(quiz, user):
	questions_folder = os.path.join(path, "quiz_wise_questions")
	responses_folder = os.path.join(path, "quiz_wise_responses")
	individual_folder = os.path.join(path, "individual_responses")

	roll_no = user[1]
	quiz_no = quiz

	csv_to_open = "q"+str(quiz_no)+".csv"
	os.chdir(questions_folder)
	df_quiz = pd.read_csv(csv_to_open)
	count = 0
	marks_quiz, skipped_questions, responses_for_csv = [], [], []
	no_of_skipped_questions, correct, wrong, total_marks = 0, 0, 0, 0

	for rows in df_quiz.itertuples():
	    # os.system('clear')
	    count += 1
	    print_user_data(user)
	    print(f"    Question {count}) {df_quiz.question[count-1]}")
	    print(f"Option 1) {df_quiz.option1[count-1]}")
	    print(f"Option 2) {df_quiz.option2[count-1]}")
	    print(f"Option 3) {df_quiz.option3[count-1]}")
	    print(f"Option 4) {df_quiz.option4[count-1]}")
	    print()
	    print(
	        f"    Credits if Correct Option: {df_quiz.marks_correct_ans[count-1]}")
	    print(f"Negative Marking: {df_quiz.marks_wrong_ans[count-1]}")
	    compulsion_map = {'n': "No", 'y': "Yes"}
	    print(
	        f"Is compulsory: {compulsion_map[df_quiz.compulsory[count-1]]}")
	    print()

	    if compulsion_map[df_quiz.compulsory[count-1]] == "Yes":
	        tmp = str(input("   Enter Choice (1, 2, 3, 4): "))
	    else:
	        tmp = str(input("   Enter Choice (1, 2, 3, 4, S): "))

	    # print(f"You Answered: Option {tmp}")
	    # print(f"Correct Ansswer: {df_quiz.correct_option[count-1]}")

	    if tmp == str(df_quiz.correct_option[count-1]):
	        marks_gained = df_quiz.marks_correct_ans[count-1]
	        correct += 1
	    elif tmp == 'S':
	        skipped_questions.append(count)
	        no_of_skipped_questions += 1
	        marks_gained = 0
	    else:
	        marks_gained = df_quiz.marks_wrong_ans[count-1]
	        wrong += 1
	    # print(f"Marks gained : {marks_gained}")
	    marks_quiz.append(marks_gained)
	    total_marks += df_quiz.marks_correct_ans[count-1]
	    extra = [tmp]
	    responses_for_csv.append(list(rows[1:-1]))
	    responses_for_csv[count-1] += extra

	# ----------------------------------Responses csv files-------------------------------------
	header_responses = df_quiz.columns.values
	header_responses = list(header_responses)[:-1]

	additional_header = ['marked choice']
	header_responses = header_responses + additional_header
	# --------------------Change of path----------------
	os.chdir(path)
	os.chdir(os.path.join(path, "individual_responses"))
	# --------------------------------------------------------
	total_marks_obtained = sum(marks_quiz)
	additional_col = {
	    "Total": [correct, wrong, no_of_skipped_questions, total_marks_obtained, total_marks],
	    "Legend": ["Correct Choices", "Wrong Choices", "Unattempted", "Marks Obtained", "Total Quiz Marks"]
	}

	# print(header_responses)
	new_df = pd.DataFrame(additional_col)
	# print(responses_for_csv)
	responses_df = pd.DataFrame(responses_for_csv, columns=header_responses)
	header_responses += ["Total", "Legend"]
	responses_df = pd.concat([responses_df, new_df], axis=1)

	responses_csv_name = "q" + str(quiz_no) + "_" + roll_no + ".csv"
	responses_df.to_csv(responses_csv_name, index=False)

	save_marks_in_database(roll_no, quiz_no, total_marks_obtained)

	print_user_data(user)
	print(f"Total Quiz Questions: {count}")
	print(f"Total Quiz Questions Attempted: {count - no_of_skipped_questions}")
	print(f"Total Correct Questions: {correct}")
	print(f"Total Wrong Questions: {wrong}")
	print(f"Total Marks Questions: {total_marks_obtained}/{total_marks}\n")

	# print_marks_from_database(roll_no)


user = register_login()
# print("User details: ", user)

if not user == []:
    quiz = int(input("Which quiz do you want to attend ? (1/2/3): "))
    start_quiz(quiz, user)
# print("Registered Users:")
# print(reg_names)
