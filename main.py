import random
from Constraints import lecPerWeek, lecPerDay
from MasterSheetMaker import getSubDict
from MasterSheetMaker import t_pri, t_mid, t_sec
import copy
import os
from prettytable import PrettyTable

t_pri = sorted(t_pri)
t_mid = sorted(t_mid)
t_sec = sorted(t_sec)

subDict = getSubDict()
subCount = len(subDict)

wingClasses = {'00': 5, '01': 3, '02':2}
noOfSections = 6
noOfLec = 8
noOfDays = 5

class Teacher():
    def __init__(self, t_code):
        self.t_code = t_code
        self.sub = subDict[t_code[:2]]

def getListFromWing(wing):

    if wing == '00':
        wing_sub = pri_sub
        t_list = t_pri
    elif wing == '01':
        wing_sub = mid_sub
        t_list = t_mid
    elif wing == '02':
        wing_sub = sec_sub
        t_list = t_sec

    return t_list, wing_sub

def getSubList(t_list):
    sublist = []
    for i in t_list:
        sublist.append(int(i[:2]))
    
    return sublist

def perClassCounter(wing_sub):
    perCount = {}
    for i in subDict:
        if i in wing_sub:
            perCount[i] = 0
    return perCount

def perCounter(wing, wing_sub):
    perCount = []
    for i in range(wingClasses[wing]):
        perCount.append([])
        for j in range(noOfSections):
            perCount[i].append(perClassCounter(wing_sub))
    return perCount

def teacherCounter(t_list):
    t_counter = {}
    for i in t_list:
        t_counter[i] = 0
    
    return t_counter

def teachertimetable(t_list):
    t_lectures = {}
    for i in t_list:
        t_lectures[i] = []
        for j in range(noOfDays):
            t_lectures[i].append([])

    return t_lectures

def get_class(i, j):
    return str(9+i) + chr(65 + j)

def teacher_sub(t_list):
    a = 1
    d = {}
    l = []
    subCodes = []

    for i in t_list:
        subCodes.append(int(i[:2]))

    for a in range(1, subCount + 1):
        l = []
        if a in subCodes:
            for j in t_list:
                if int(j[:2]) == a:
                    l.append(j)
            d[a] = l
    return d

pri_sub = teacher_sub(t_pri)
mid_sub = teacher_sub(t_mid)
sec_sub = teacher_sub(t_sec)

def assignOne(wing_sub):
    c=[]

    for i in range(1, subCount + 1):
        l = []
        if i in wing_sub:
            l = wing_sub[i]
        else:
            continue
        c.append(random.choice(l))

    return c

def check(temp, d, wing_sub):
    for i in temp:
        x = int(i[:2])
        l = wing_sub[x]
        if d[i] >= noOfSections/len(l):
            temp.remove(i)
    return temp

def assign(wing):

    classes = []
    noOfClasses = wingClasses[wing]
    for i in range(noOfClasses):
        classes.append([])

    t_list, wing_sub = getListFromWing(wing)

    d = {}
    for i in t_list:
        d[i] = 0
    for i in range(noOfClasses):
        temp=list(t_list)
        d={}
        for j in t_list:
            d[j] = 0
        for j in range(noOfSections):
            c = assignOne(teacher_sub(temp))
            for k in t_list:
                d[k] = d[k] + c.count(k)
            temp = check(temp, d, wing_sub)
            classes[i].append(c)
    return classes

def assign_lec(classes, wing, wing_perWeek, wing_perDay, t_list, day, mathcount, t_timetable):
    
    t_counter = teacherCounter(t_list)
    temp = list(t_list)
    assigned_day = []
    wed_check = 0
    if day == 2:
        wed_check = 2
    for i in range(len(classes)):
        for j in range(noOfSections):
            temp2 = list(classes[i][j])
            counter_perWeek = wing_perWeek[i][j]
            counter_perDay = wing_perDay[i][j]
            temp2 = list(set(temp) & set(temp2))
            subjects = getSubList(temp2)
            assigned = []
            assigned.extend([1,9,10])
            subjects.remove(9)
            try:
                subjects.remove(10)
            except:
                print("An Unexpected Error has occured, Please restart the program")
                os.exit()
            if mathcount[i][j] == 1:
                subjects.remove(1)
            for k in subjects[::-1]:
                if counter_perWeek[k] >= lecPerWeek[k][int(wing)]:
                    subjects.remove(k)
                elif counter_perDay[k] >= lecPerDay[k][int(wing)]:
                    subjects.remove(k)
            # print(subjects)
            assigned.extend(random.sample(subjects, noOfLec - len(assigned) - wed_check))
            # print(assigned)
            assigned_teachers = []
            for a in temp2[::-1]:
                if int(a[:2]) in assigned:
                    t_counter[a] += 1
                    t_timetable[a][day].append(get_class(i, j))
                    for n in range(assigned.count(int(a[:2]))):
                        assigned_teachers.append(a)
                    if assigned.count(int(a[:2])) == 2:
                        mathcount[i][j] += 1
                    wing_perWeek[i][j][int(a[:2])] += assigned.count(int(a[:2]))
                    if t_counter[a] >= 6:
                        temp.remove(a)
            assigned_day.append(assigned_teachers)
    # print(assigned_day)
    loop_count = 0
    while True:
        try:
            final = []
            for i in range(len(classes*noOfSections)):
                final.append([])
                if day == 2:
                    final[i].extend(["Worksheet", "Worksheet"])
            new_assigned = copy.deepcopy(assigned_day)
            for i in range(noOfLec - wed_check):
                used = []
                for j in range(len(new_assigned)):
                    # print(final)
                    possible = list(new_assigned[j])
                    for k in possible[::-1]:
                        if k in used:
                            possible.remove(k)
                    x = random.choice(possible)
                    new_assigned[j].remove(x)
                    final[j].append(subDict[int(x[:2])])
                    used.append(x)
            break
        except:
            loop_count += 1
            if loop_count > 5000:
                raise ValueError("Restart")
    return final

def dailyTime(classes, wing, week, wing_perWeek, day, mathcount, t_timetable):
    t_list, wing_sub = getListFromWing(wing)
    wing_perDay = perCounter(wing, wing_sub)
    lec = assign_lec(classes, wing, wing_perWeek, wing_perDay, t_list, day, mathcount, t_timetable)
    week.append(lec)

def weektime(wing):
    week = []
    t_list, wing_sub = getListFromWing(wing)
    wing_perWeek = perCounter(wing, wing_sub)
    classes = assign(wing)
    print("Timetable is being generated")
    bla = 0
    while True:
        try:
            mathcount = []
            t_timetable = teachertimetable(t_list)
            for i in range(len(classes)):
                mathcount.append([])
                for j in range(noOfSections):
                    mathcount[i].append(0)
            for i in range(noOfDays):
                # print("DAY", i+1)
                dailyTime(classes, wing, week, wing_perWeek, i, mathcount, t_timetable)
            break
        except:
            wing_perWeek = perCounter(wing, wing_sub)
            week = []
            bla += 1
    print("Timetable has been generated")
    return week, t_timetable
table = {}
week, t_timetable = weektime('02')
days = ["Mon", "Tues", "Wed", "Thurs", "Fri"]
for i in range(12):
    class_sec = str(9 + i//6) + chr(65 + i - 6*(i//6))
    table[class_sec] = PrettyTable(["", "Lec 1", "Lec 2" , "Lec 3", "Lec 4", "Lec 5", "Lec 6", "Lec 7", "Lec 8"])
    for day in range(len(week)):
        day_table = [days[day]] + week[day][i]
        table[class_sec].add_row(day_table)

for i in table:
    print("                                          ", i)
    print(table[i])