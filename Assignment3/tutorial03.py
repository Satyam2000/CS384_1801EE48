import csv
import os

def course():
    # Read csv and process
    pass


def country():
    # Read csv and process
    pass


def email_domain_extract():
    # Read csv and process
    pass


def gender():
    open('C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics/gender/female.csv', 'w').close()
    open('C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics/gender/male.csv', 'w').close()
    # Read csv and process
    with open('C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/studentinfo_cs384.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[4] == "Female" :
                with open('C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics/gender/female.csv', 'a',newline='') as female:
                    writer = csv.writer(female)
                    writer.writerow(row)
            elif row[4] == "Male" :
                with open('C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics/gender/male.csv', 'a',newline='') as male:
                    writer = csv.writer(male)
                    writer.writerow(row)
    pass



def dob():
    # Read csv and process
    pass


def state():
    # Read csv and process
    pass


def blood_group():
    # Read csv and process
    pass


# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    pass
