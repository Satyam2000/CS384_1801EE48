#CS384 2020 Assignment 4 - Academic Result Generator
# Deadline:14th November 2020
#Satyam Kumar
#1801EE48

import csv
import os
import shutil
import re
import datetime

pattern_roll=re.compile(r'^[0-9]{4}[A-Za-z]{2}[0-9]{2}$')
pattern_sem_credit=re.compile(r'^[0-9]+$')

pattern=re.compile(r'^[A-Z]{2}[0-9]{3}$',re.I)
pattern_credit=re.compile(r'AA|AB|BC|BB|CC|CD|DD|I|F',re.I)
if(os.path.isdir(r'./grades')):
    shutil.rmtree('./grades')
os.makedirs('./grades')

roll_list=[]
header=['sl','roll','sem','year','sub_code','total_credits','credit_obtained','timestamp','sub_type']

#program to separate rollno_individual 
with open('./grades/misc.csv','a',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(header)

with open('./acad_res_stud_grades.csv','r') as file:
        reader=csv.reader(file)

        for row in reader:
            if(not row[0]=='sl'):
                if(not (re.fullmatch(pattern_roll,row[1]) and re.fullmatch(pattern_sem_credit,row[2]) and re.fullmatch(pattern_sem_credit,row[5]) and re.fullmatch(pattern,row[4]) and re.fullmatch(pattern_credit,row[6]))):
                    
                    with open('./grades/misc.csv','a',newline='') as file:
                        writer=csv.writer(file)
                        writer.writerow(row)
                    continue

                roll_no1=row[1]+'_individual.csv'
                if(not os.path.isfile('./grades/'+roll_no1)):
                    roll_list.append(row[1])
                    
                    with open('./grades/'+roll_no1, 'a',newline='') as file:
                        writer=csv.writer(file)
                        writer.writerow(['Roll: '+row[1]])
                        writer.writerow(['Semester Wise Details'])
                        writer.writerow(['Subject','Credits','Type','Grade','Sem'])
                list1=[row[4],row[5],row[8],row[6],row[2]]
                
                with  open('./grades/'+roll_no1, 'a',newline='') as file:
                    writer=csv.writer(file)
                    writer.writerow(list1)
list2=[]
for roll in roll_list:
    file=open('./grades/'+roll+'_individual.csv','r')
    with file:
        reader=csv.reader(file)
        for row in reader:
            if(re.fullmatch(pattern,row[0])):
                list2.append(row)
    sorted_list=sorted(list2,key=lambda l:l[4])
    list2.clear()


    with open('./grades/'+roll+'_overall.csv', 'a',newline='') as file:
        writer=csv.writer(file)
        writer.writerow(['Roll: '+roll])
        writer.writerow(['Semester','Semester Credits','Semester Credits Cleared','SPI','Total Credits','Total Credits Cleared','CPI'])
    grades = {'AA':10,'AB':9,'BB':8,'BC':7,'CC':6,'CD':5,'DD':4,'F':0,'I':0}
    current_total=0
    current_total_cleared=0
    overall_total=0
    overall_total_cleared=0
    current_sem='W'
    spi1_into_credits=0
    cpi_into_credits=0
    for row in sorted_list:
        if(current_sem=='W'):
            current_sem=row[4]
        if(current_sem==row[4]):
            current_total+=int(row[1])
            if(grades[row[3]]>0):
                current_total_cleared+=int(row[1])
                overall_total_cleared+=int(row[1])
            spi1_into_credits+=(grades[row[3]]*int(row[1]))
            overall_total+=int(row[1])
        else:
            cpi_into_credits+=spi1_into_credits
            list_3=[current_sem,current_total,current_total_cleared,spi1_into_credits/current_total,overall_total,overall_total_cleared,cpi_into_credits/overall_total]
            
            with  open('./grades/'+roll+'_overall.csv', 'a',newline='') as file:
                writer=csv.writer(file)
                writer.writerow(list_3)
            current_sem=row[4]
            current_total=int(row[1])
            if(grades[row[3]]>0):
                current_total_cleared=int(row[1])
                overall_total_cleared+=int(row[1])
            spi1_into_credits=(grades[row[3]]*int(row[1]))
            overall_total+=int(row[1])
            
    cpi_into_credits+=spi1_into_credits
    list_3=[current_sem,current_total,current_total_cleared,spi1_into_credits/current_total,overall_total,overall_total_cleared,cpi_into_credits/overall_total]
     
    with open('./grades/'+roll+'_overall.csv', 'a',newline='') as file:
        writer=csv.writer(file)
        writer.writerow(list_3)