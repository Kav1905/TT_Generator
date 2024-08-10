import random
from openpyxl import Workbook, load_workbook
from MasterSheetMaker import getSubDict
from MasterSheetMaker import t_pri, t_mid, t_sec
from Constraints import lecPerWeek

t_pri = sorted(t_pri)
t_mid = sorted(t_mid)
t_sec = sorted(t_sec)

load_data = load_workbook("Data.xlsx")
data = load_data["Master"]

subDict = getSubDict()
subCount = len(subDict)

wingClasses = {'00': 5, '01': 3, '02':4}
noOfSections = 6

class Teacher():
    def __init__(self, t_code):
        self.t_code = t_code
        self.sub = subDict[t_code]

def lecPerWeekCheck():
    pass

def teacher_sub(t_list):
    a = 1
    d = {}
    l = []
    subCodes = []
    count = 0
    for i in t_list:
        subCodes.append(int(i[:2]))

    for a in range(subCount):
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

    if wing == '00':
        wing_sub = pri_sub
        t_list = t_pri
    elif wing == '01':
        wing_sub = mid_sub
        t_list = t_mid
    elif wing == '02':
        wing_sub = sec_sub
        t_list = t_sec

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

output = assign('02')

count = 9
for j in output:
    print(count)
    for k in range(len(j)):
        print(k)
        print(j[k])
    count += 1