#Satyam Kumar
#1801EE48

from math import floor
import csv
import pandas as pd
import os

#End Sem Assignment
#Assignment Given on 28th Nov 2020, 1730 hrs
#Assignment Deadline on 30th Nov 2020, 1730 hrs



def group_allocation(filename, groups_no):
    # Entire Logic
    # You can add more functions, but in the test case, we will only call the group_allocation() method,

    with open(r'./'+filename, 'r') as file:
        all_the_entries = csv.reader(file)
        list_1 = []
        map = {}
        for row in all_the_entries:
            if list_1 == []:
                list_1 = row
            else:
                branch_code = row[0][4:6]
                branch_code = branch_code.upper()
                if map.get(branch_code) == None:
                    if os.path.isfile(r'./'+branch_code+'.csv'):
                        os.remove(r'./'+branch_code+'.csv')

                    
                    with open(r'./'+branch_code+'.csv', 'a+', newline="") as file:
                        all_the_entries = csv.writer(file)
                        all_the_entries.writerow(list_1)
                    map[branch_code] = 0
                map[branch_code] += 1
                
                with open(r'./'+branch_code+'.csv', 'a+', newline="") as file:
                    all_the_entries = csv.writer(file)
                    all_the_entries.writerow(row)
        
        with open(r'.\branch_strength.csv', 'w', newline="") as file:
            all_the_entries = csv.writer(file)
            all_the_entries.writerow(["BRANCH_CODE", "STRENGTH"])
        list_1_2 = []
        for branch_code in map.keys():
            list_1_2.append([branch_code, map[branch_code]])
        list_1_2 = sorted(list_1_2, key=lambda l: int(l[1]), reverse=True)

        for row in list_1_2:
            with open(r'.\branch_strength.csv', 'a+', newline="") as file:
                all_the_entries = csv.writer(file)
                all_the_entries.writerow(row)
                
    branch_number = len(list_1_2)

    list_1_3 = [[0 for i in range(branch_number+2)]
             for j in range(groups_no+1)]

    list_1_3[0][0] = "group"
    list_1_3[0][1] = "total"

    for i in range(2, branch_number+2):
        list_1_3[0][i] = list_1_2[i-2][0]

    temp_1 = len(str(groups_no))

    for i in range(1, groups_no+1):
        temp_2 = temp_1 - len(str(i))
        list_1_3[i][0] = "Group_G"+'0'*temp_2+str(i)+".csv"

    list_1_4 = []

    for i in range(len(list_1_2)):
        temp_3 = floor(list_1_2[i][1]/groups_no)

        for j in range(1, groups_no+1):
            list_1_3[j][i+2] = temp_3

        list_1_4.append(list_1_2[i][1]-groups_no*temp_3)

    length = 1
    for i in range(len(list_1_4)):
        while list_1_4[i] > 0:
            list_1_3[length][i+2] += 1
            list_1_4[i] -= 1
            if length == groups_no:
                length = 1
            else:
                length += 1

    for i in range(1, groups_no+1):
        for j in range(2, branch_number+2):
            list_1_3[i][1] += list_1_3[i][j]
    if os.path.isfile(r'./stats_grouping.csv'):
        os.remove(r'./stats_grouping.csv')
    
    with open(r'./stats_grouping.csv', 'w', newline="") as file:
        all_the_entries = csv.writer(file)
        all_the_entries.writerows(list_1_3)

    for i in range(1, groups_no+1):
        
        with open(r'./'+list_1_3[i][0], 'w', newline="") as file:
            all_the_entries = csv.writer(file)
            all_the_entries.writerow(["Roll", "Name", "Email"])
            
    for i in range(2, branch_number+2):
        temp_4 = pd.read_csv(r'./'+list_1_3[0][i]+'.csv')
        temp = 0

        for j in range(1, groups_no+1):
            flag = temp_4.iloc[temp:temp+list_1_3[j][i]]
            flag_to_list = flag.values.tolist()
            temp += list_1_3[j][i]
            
            with  open(r'./'+list_1_3[j][0], 'a+', newline="") as file:
                all_the_entries = csv.writer(file)
                all_the_entries.writerows(flag_to_list)
    return


filename = "Btech_2020_master_data.csv" #All the data derived from this file.12
#No. of groups to be provided by the user.
groups_no = int(input("Enter No. of Groups : ", ))
group_allocation(filename, groups_no)
