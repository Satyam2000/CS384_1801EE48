import csv
import os
import shutil
import re

def course():
    # Read csv and process
    pass


def country():
    # Read csv and process
    if(os.path.isdir(r'C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics')) :
        if(os.path.isdir(r'C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics/country')) :
            shutil.rmtree(r'C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics/country')

            path = r"C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics/country"
            os.mkdir(path)

        else :
            path = r"C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics/country"
            os.mkdir(path)

    else :
        os.makedirs(r"C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics/country")

    path = "C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics/country"

    with open('C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/studentinfo_cs384.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if(row[0] == 'id') :
                temp = row
            country_name = row[2] +'.csv'
            pa = os.path.join(path,country_name) 
            if(not row[0] =='id'):
                if(not os.path.isfile(pa)):
                    list1 = open(pa,'w',newline='')
                    with list1:
                        writer=csv.writer(list1) 
                        writer.writerow(temp)     
            if(not row[0] == 'id') :
                list1 = open(pa,'a',newline='')
                with list1:
                    writer = csv.writer(list1)
                    writer.writerow(row)
    pass

country()
def email_domain_extract():
    if(os.path.isdir(r'C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics')) :
        if(os.path.isdir(r'C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics/email_domain')) :
            shutil.rmtree(r'C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics/email_domain')

            path = r"C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics/email_domain"
            os.mkdir(path)

        else :
            path = r"C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics/email_domain"
            os.mkdir(path)

    else :
        os.makedirs(r"C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics/email_domain")

    # Read csv and process
    path = "C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics/email_domain"
    
    domain = re.compile(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.[a-zA-Z.]{2,18}$')

    with open('C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/studentinfo_cs384.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if(row[0] == 'id') :
                temp = row
            if(not row[0] =='id'):
                if(re.match(domain,row[3])):
                    result1 = row[3][row[3].index('@')+1:] 
                    result2=result1[:result1.index('.')]
                    pi=os.path.join(path,result2+'.csv')
                    if(not os.path.isfile(pi)):
                        list1 = open(pi, 'w',newline='')
                        with list1:
                            writer=csv.writer(list1)
                            writer.writerow(temp)
                    list1 = open(pi, 'a',newline='')
                    with list1:
                        writer=csv.writer(list1)
                        writer.writerow(row)
                else:
                    pi=os.path.join(path,'misc.csv')
                    if(not os.path.isfile(pi)):
                        list1 = open(pi, 'w',newline='')
                        with list1:
                            writer=csv.writer(list1)
                            writer.writerow(temp)
                    list1 = open(pi, 'a',newline='')
                    with list1:
                        writer=csv.writer(list1)
                        writer.writerow(row)      
            

    pass

email_domain_extract()
def gender():
    if(os.path.isdir(r'C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics')) :
        if(os.path.isdir(r'C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics/gender')) :
            shutil.rmtree(r'C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics/gender')

            path = r"C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics/gender"
            os.mkdir(path)

        else :
            path = r"C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics/gender"
            os.mkdir(path)
    else :
        path = r"C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics/gender"
        os.makedirs(path)
    
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


gender()

def dob():
    # Read csv and process
    pass


def state():
    if(os.path.isdir(r'C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics')) :
        if(os.path.isdir(r'C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics/state')) :
            shutil.rmtree(r'C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics/state')

            path = r"C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics/state"
            os.mkdir(path)

        else :
            path = r"C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics/state"
            os.mkdir(path)

    else :
        os.makedirs(r"C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics/state")

    # Read csv and process
    path = "C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics/state"
    
    with open('C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/studentinfo_cs384.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if(row[0] == 'id') :
                temp = row
            state_name = row[7] +'.csv'
            pa = os.path.join(path,state_name) 
            if(not row[0] =='id'):
                if(not os.path.isfile(pa)):
                    list1 = open(pa,'w',newline='')
                    with list1:
                        writer=csv.writer(list1) 
                        writer.writerow(temp)     
            if(not row[0] == 'id') :
                list1 = open(pa,'a',newline='')
                with list1:
                    writer = csv.writer(list1)
                    writer.writerow(row)
    pass

state()
def blood_group():
    if(os.path.isdir(r'C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics')) :
        if(os.path.isdir(r'C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics/blood_group')) :
            shutil.rmtree(r'C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics/blood_group')

            path = r"C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics/blood_group"
            os.mkdir(path)

        else :
            path = r"C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics/blood_group"
            os.mkdir(path)

    else :
        os.makedirs(r"C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics/blood_group")

    # Read csv and process
    path = "C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/analytics/blood_group"
    
    with open('C:/Users/satyam kumar/Desktop/CS384/CS384_1801EE48/Assignment3/studentinfo_cs384.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if(row[0] == 'id') :
                temp = row
            blood_group_name = row[6] +'.csv'
            pa = os.path.join(path,blood_group_name) 
            if(not row[0] =='id'):
                if(not os.path.isfile(pa)):
                    list1 = open(pa,'w',newline='')
                    with list1:
                        writer=csv.writer(list1) 
                        writer.writerow(temp)     
            if(not row[0] == 'id') :
                list1 = open(pa,'a',newline='')
                with list1:
                    writer = csv.writer(list1)
                    writer.writerow(row)

    pass

blood_group()
# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    pass
