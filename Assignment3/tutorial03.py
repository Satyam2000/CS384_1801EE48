#Satyam Kumar_1801EE48
import csv
import os
import datetime
import shutil
import re
#Python command to clear the terminal
os.system('cls')
#The code starts here.
def del_create_analytics_folder():
    # del the analytics folder including subfolder
    # make directory using mkdir for the analytics folder (only mkdir)
    if(os.path.isdir(r'./analytics')):
        shutil.rmtree('./analytics')
    os.makedirs('./analytics')
    pass


def course():
    # Read csv and process
    pass


def country():
    # Read csv and process
    if(os.path.isdir(r'./analytics')) :
        if(os.path.isdir(r'./analytics/country')) :
            shutil.rmtree('./analytics/country')

            path = "./analytics/country"
            os.mkdir(path)

        else :
            path = "./analytics/country"
            os.mkdir(path)

    else :
        os.makedirs("./analytics/country")

    path = "./analytics/country"

    with open('./studentinfo_cs384.csv', 'r') as file:
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
    if(os.path.isdir(r'./analytics')) :
        if(os.path.isdir(r'./analytics/email_domain')) :
            shutil.rmtree('./analytics/email_domain')

            path = "./analytics/email_domain"
            os.mkdir(path)

        else :
            path = "./analytics/email_domain"
            os.mkdir(path)

    else :
        os.makedirs("./analytics/email_domain")

    # Read csv and process
    path = "./analytics/email_domain"
    
    domain = re.compile(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.[a-zA-Z.]{2,18}$')

    with open('./studentinfo_cs384.csv', 'r') as file:
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
    if(os.path.isdir(r'./analytics')) :
        if(os.path.isdir(r'./analytics/gender')) :
            shutil.rmtree('./analytics/gender')

            path = "./analytics/gender"
            os.mkdir(path)

        else :
            path = "./analytics/gender"
            os.mkdir(path)
    else :
        path = "./analytics/gender"
        os.makedirs(path)
    
    # Read csv and process
    with open('./studentinfo_cs384.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[4] == "Female" :
                with open('./analytics/gender/female.csv', 'a',newline='') as female:
                    writer = csv.writer(female)
                    writer.writerow(row)
            elif row[4] == "Male" :
                with open('./analytics/gender/male.csv', 'a',newline='') as male:
                    writer = csv.writer(male)
                    writer.writerow(row)
    pass


gender()
#program to check whether dob is valid.
def date_validation(day, month, year): 
      
    isValidDate = True
    try : 
        datetime.datetime(int(year),  
                          int(month), int(day)) 
          
    except ValueError : 
        isValidDate = False
    if((int(year))<1995 or (int(year))>2020):
        isValidDate = False
    return isValidDate

def dob():
    if(os.path.isdir(r'./analytics')):
        if(os.path.isdir(r'./analytics/dob')):
            shutil.rmtree('./analytics/dob')

            path = "./analytics/dob"
            os.mkdir(path)
        else:
            path = "./analytics/dob"
            os.mkdir(path)
    else:
        os.makedirs('./analytics/dob')
    
    # Read csv and process    
    
    path='./analytics/dob'

    category_a='./analytics/dob/bday_1995_1999.csv'
    category_b='./analytics/dob/bday_2000_2004.csv'
    category_c='./analytics/dob/bday_2005_2009.csv'
    category_d='./analytics/dob/bday_2010_2014.csv'
    category_e='./analytics/dob/bday_2015_2020.csv'
    category_f='./analytics/dob/misc.csv'
     
    with open('./studentinfo_cs384.csv', 'r') as file:
        reader=csv.reader(file)
        for row in reader:
            if(row[0]=='id'):
                m1=open(category_a,'w',newline='')
                with m1:
                        writer=csv.writer(m1)
                        writer.writerow(row)
                m2=open(category_b,'w',newline='')
                with m2:
                        writer=csv.writer(m2)
                        writer.writerow(row)
                m3=open(category_c,'w',newline='')
                with m3:
                        writer=csv.writer(m3)
                        writer.writerow(row)
                m4=open(category_d,'w',newline='')
                with m4:
                        writer=csv.writer(m4)
                        writer.writerow(row)
                m5=open(category_e,'w',newline='')
                with m5:
                        writer=csv.writer(m5)
                        writer.writerow(row)
                m6=open(category_f,'w',newline='')
                with m6:
                        writer=csv.writer(m6)
                        writer.writerow(row)
            else:
                res = row[5].split('-')
                if(not date_validation(res[0],res[1],res[2])):
                    m6=open(category_f,'a',newline='')
                    with m6:
                        writer=csv.writer(m6)
                        writer.writerow(row)
                elif((int(res[2]))>=1995 and (int(res[2]))<=1999):
                    m1=open(category_a,'a',newline='')
                    with m1:
                        writer=csv.writer(m1)
                        writer.writerow(row)
                elif((int(res[2]))>=2000 and (int(res[2]))<=2004):
                    m2=open(category_b,'a',newline='')
                    with m2:
                        writer=csv.writer(m2)
                        writer.writerow(row)
                elif((int(res[2]))>=2005 and (int(res[2]))<=2009):
                    m3=open(category_c,'a',newline='')
                    with m3:
                        writer=csv.writer(m3)
                        writer.writerow(row)
                elif((int(res[2]))>=2010 and (int(res[2]))<=2014):
                    m4=open(category_d,'a',newline='')
                    with m4:
                        writer=csv.writer(m4)
                        writer.writerow(row)
                elif((int(res[2]))>=2015 and (int(res[2]))<=2020):
                    m5=open(category_e,'a',newline='')
                    with m5:
                        writer=csv.writer(m5)
                        writer.writerow(row)
    
    pass

dob()

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
