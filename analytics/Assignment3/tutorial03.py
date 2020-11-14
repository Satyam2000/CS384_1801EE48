#Satyam Kumar_1801EE48
import csv
import os
import datetime
import operator
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
    cd = '.'
    
    with open('studentinfo_cs384.csv','r') as file:
        student_data = csv.DictReader(file)
        misc_course=[]
        header=['id','full_name','country','email','gender','dob','blood_group','state']
        course_code={'01' : "btech",'11' : "mtech",'12' : "msc",'21' : "phd"}
        roll_number_pattern = re.compile(r'^[0-9]{2}[0-2]{2}[a-zA-Z]{2}[0-9]{2}$')    
        cd+=r'\analytics'
        if(not os.path.isdir(cd)):
            os.mkdir(cd)
        cd+=r'\course'
        if(not os.path.isdir(cd)):
            os.mkdir(cd)
        for row in student_data:
            roll_no = row['id']
            if(not re.match(roll_number_pattern , roll_no)):
                misc_course.append(row)
            else:
                year = roll_no[0:2]
                course = course_code[roll_no[2:4]]
                branch = (roll_no[4:6]).lower()
                cd1=cd
                cd1+="\\"+branch
                if not os.path.isdir(cd1):
                    os.mkdir(cd1)
                cd1+="\\"+course
                if not os.path.isdir(cd1):
                    os.mkdir(cd1)
                info_file = cd1 + "\\" + year + '_' + branch + '_' + course + ".csv"
                if(not os.path.isfile(info_file)):
                    file=open(info_file,'w',newline='')
                    with file:
                        writer = csv.DictWriter(file,fieldnames=header)
                        writer.writeheader()
                file=open(info_file,'a+',newline='')
                with file:
                    writer = csv.DictWriter(file,fieldnames=header)
                    writer.writerow(row)
        cd+=r'\misc.csv'
        file=open(cd,'w',newline='')
        with file:
            data = csv.DictWriter(file,fieldnames=header)
            data.writeheader()
            data.writerows(misc_course)
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

            else:
                misc= open('./analytics/gender/misc.csv','a',newline='')
                with misc:
                    writer=csv.writer(misc)
                    writer.writerow(row)  
    pass



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



def state():
    if(os.path.isdir(r'./analytics')) :
        if(os.path.isdir(r'./analytics/state')) :
            shutil.rmtree('./analytics/state')

            path = "./analytics/state"
            os.mkdir(path)

        else :
            path = "./analytics/state"
            os.mkdir(path)

    else :
        os.makedirs("./analytics/state")

    # Read csv and process
    path = "./analytics/state"
    
    with open('./studentinfo_cs384.csv', 'r') as file:
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


def blood_group():
    if(os.path.isdir(r'./analytics')) :
        if(os.path.isdir(r'./analytics/blood_group')) :
            shutil.rmtree('./analytics/blood_group')

            path = "./analytics/blood_group"
            os.mkdir(path)

        else :
            path = "./analytics/blood_group"
            os.mkdir(path)

    else :
        os.makedirs("./analytics/blood_group")

    # Read csv and process
    path = "./analytics/blood_group"
    
    with open('./studentinfo_cs384.csv', 'r') as file:
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


# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    if(not os.path.isdir(r'./analytics')):
        os.makedirs('./analytics')
    temp=['id','first name','last name','country','email','gender','dob','blood group','state']
    header =temp
    open('./analytics/studentinfo_cs384_names_split.csv','a',newline='')
    with open('./analytics/studentinfo_cs384_names_split.csv','a',newline='') as file:
        writer=csv.writer(file)
        writer.writerow(temp)
    
    with open('./studentinfo_cs384.csv', 'r') as file:
        reader=csv.reader(file)
        for row in reader:
            if(row[0] != 'id'):
                name_split = row[1].split(' ')
                first_name = name_split[0]
                last_name = name_split[1:]
                last=''
                for i in last_name:
                    last=last+i+' '
                temp = [row[0], first_name, last, row[2],
                        row[3], row[4], row[5], row[6], row[7]]
                new_file=open('./analytics/studentinfo_cs384_names_split.csv', 'a',newline='')
                with new_file:
                    writer=csv.writer(new_file)
                    writer.writerow(temp) 

    new_fil=open('./analytics/studentinfo_cs384_names_split.csv','r')
    list1=[]
    with new_fil:
        reader=csv.reader(new_fil)
        for row in reader:
            if(row[0]!='id'):
                list1.append(row)
    f=open('./analytics/studentinfo_cs384_names_split_sorted_first_name.csv', 'a',newline='')
    with f:
        writer = csv.writer(f)
        writer.writerow(header)
    sort_list1=sorted(list1,key=lambda l:l[1])
    f=open('./analytics/studentinfo_cs384_names_split_sorted_first_name.csv', 'a',newline='')
    with f:
        writer = csv.writer(f)
        for row in sort_list1:
            writer.writerow(row)

    pass
