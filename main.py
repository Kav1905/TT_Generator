import random
from Constraints import lecPerWeek, lecPerDay
from MasterSheetMaker import getSubDict
from MasterSheetMaker import t_pri, t_mid, t_sec
import copy

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

# def getWingCounters(wing):
    
#     if wing == '00':
#         wing_perDay = pri_perDay
#         wing_perWeek = pri_perWeek
#     elif wing == '01':
#         wing_perDay = mid_perDay
#         wing_perWeek = mid_perWeek
#     elif wing == '02':
#         wing_perDay = sec_perDay
#         wing_perWeek = sec_perWeek

#     return wing_perDay, wing_perWeek

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

def teacher_sub(t_list):
    a = 1
    d = {}
    l = []
    subCodes = []
    count = 0
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

# pri_perDay = perCounter(pri_sub)
# mid_perDay = perCounter(mid_sub)
# sec_perDay = perCounter(sec_sub)

# pri_perWeek = perCounter(pri_sub)
# mid_perWeek = perCounter(mid_sub)
# sec_perWeek = perCounter(sec_sub)

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

def active_lec(classes, wing, wing_perWeek):
    t_list, wing_sub = getListFromWing(wing)
    wing_perDay = perCounter(wing, wing_sub)
    subtemp2 = copy.deepcopy(wing_sub)
    temp = list(t_list)
    print(wing_perWeek)
    print("LECTURE")
    lec = []
    for i in range(len(classes)):
        lec.append([])
        for j in range(noOfSections):
            lec[i].append([])

    for i in range(len(classes)):
        for j in range(noOfSections):
            temp2 = list(classes[i][j])
            counter_perWeek = wing_perWeek[i][j]
            counter_perDay = wing_perDay[i][j]
            for k in temp2[::-1]:
                if k not in temp:
                    # print(temp2)
                    # print(k)
                    temp2.remove(k)
                
                elif counter_perWeek[int(k[:2])] >= lecPerWeek[int(k[:2])][int(wing)]:
                    # print(counter_perWeek)
                    # print(k)
                    temp2.remove(k)
                
                elif counter_perDay[int(k[:2])] >= lecPerDay[int(k[:2])][int(wing)]:
                    # print(counter_perDay)
                    # print(k)
                    temp2.remove(k)
            
            # print(subtemp2)
            # print(temp2)

            subtemp = list(teacher_sub(temp2).keys())
            x = random.choice(subtemp)

            for a in temp2:
                if int(a[:2]) == x:
                    y = a
                    break

            # print(subtemp2)
            # print(x,y, end = '\n')
            wing_perDay[i][j][x] += 1
            wing_perWeek[i][j][x] += 1
            subtemp2[x].remove(y)
            temp.remove(y)
            lec[i][j].append(x)
            lec[i][j].append(y)
            # print(lec)

    return lec

def dailyTime(classes, wing, day, wing_perWeek):
    for i in range(noOfLec):
        lec = active_lec(classes, wing, wing_perWeek)
        day.append(lec)

def weektime(wing):
    day = []
    week = []
    t_list, wing_sub = getListFromWing(wing)
    wing_perWeek = perCounter(wing, wing_sub)
    classes = assign(wing)
    for i in range(noOfDays):
        dailyTime(classes, wing, day, wing_perWeek)
        week.append(day)
    print(week)
    
# sec_classes = assign('02')
# count = 9
# for j in sec_classes:
#     print(count)
#     for k in range(len(j)):
#         print(k)
#         print(j[k])
#     count += 1

weektime('02')
