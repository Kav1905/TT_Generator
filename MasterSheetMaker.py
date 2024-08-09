from openpyxl import Workbook, load_workbook

load_sheet = load_workbook("Data.xlsx")
Teacher_Input = load_sheet["Teacher_Input"]
Subject_Input = load_sheet["Subject_Input"]
Master = load_sheet["Master"]

i = 2
Sub_dict = {}
prim_SubCount = {}
mid_SubCount = {}
sec_SubCount = {}
t_pri = []
t_mid = []
t_sec = []

while True:
    cell = 'A' + str(i)
    if i < 11:
        Sub_code = '0' + str(i-1)
    else:
        Sub_code = str(i-1)

    if Subject_Input[cell].value == None:
        break
    else:
        Sub_dict[Subject_Input[cell].value] = Sub_code
        prim_SubCount[Subject_Input[cell].value] = 1
        mid_SubCount[Subject_Input[cell].value] = 1
        sec_SubCount[Subject_Input[cell].value] = 1
        i+=1

Wing_dict = {'Primary':'00', 'Middle':'01', 'Secondary':'02'}

def create_MasterSheet():
    prim_count = 3
    mid_count = 3
    sec_count = 3
    i = 2
    while True:
        Wing_cell = 'C' + str(i)
        Sub_cell = 'B' + str(i)
        Name_cell = 'A' + str(i)
        teacher_Sub = Teacher_Input[Sub_cell].value
        teacher_Name = Teacher_Input[Name_cell].value
        teacher_Wing = Teacher_Input[Wing_cell].value

        if teacher_Sub == None:
            break
        else:
            if teacher_Wing == "Primary":
                for j in range(6):
                    active_cell = chr(65 + j) + str(prim_count)
                    if j == 0:
                        Master[active_cell] = teacher_Name
                    elif j == 1:
                        Master[active_cell] = teacher_Sub
                    elif j == 2:
                        Master[active_cell] = Sub_dict[teacher_Sub]
                    elif j == 3:
                        Master[active_cell] = teacher_Wing
                    elif j == 4:
                        Master[active_cell] = Wing_dict[teacher_Wing]
                    elif j == 5:
                        t_SubId = prim_SubCount[teacher_Sub]
                        if t_SubId < 10:
                            teacher_Code = Sub_dict[teacher_Sub] + Wing_dict[teacher_Wing] + '0' + str(t_SubId)
                        else:
                            teacher_Code = Sub_dict[teacher_Sub] + Wing_dict[teacher_Wing] + str(t_SubId)
                        prim_SubCount[teacher_Sub] += 1

                        t_pri.append(teacher_Code)
                        Master[active_cell] = teacher_Code

                prim_count += 1

            elif teacher_Wing == "Middle":
                for j in range(6):
                    active_cell = chr(71 + j) + str(mid_count)
                    if j == 0:
                        Master[active_cell] = teacher_Name
                    elif j == 1:
                        Master[active_cell] = teacher_Sub
                    elif j == 2:
                        Master[active_cell] = Sub_dict[teacher_Sub]
                    elif j == 3:
                        Master[active_cell] = teacher_Wing
                    elif j == 4:
                        Master[active_cell] = Wing_dict[teacher_Wing]
                    elif j == 5:
                        t_SubId = mid_SubCount[teacher_Sub]
                        if t_SubId < 10:
                            teacher_Code = Sub_dict[teacher_Sub] + Wing_dict[teacher_Wing] + '0' + str(t_SubId)
                        else:
                            teacher_Code = Sub_dict[teacher_Sub] + Wing_dict[teacher_Wing] + str(t_SubId)
                        mid_SubCount[teacher_Sub] += 1

                        t_mid.append(teacher_Code)
                        Master[active_cell] = teacher_Code

                mid_count += 1

            elif teacher_Wing == "Secondary":
                for j in range(6):
                    active_cell = chr(77 + j) + str(sec_count)
                    if j == 0:
                        Master[active_cell] = teacher_Name
                    elif j == 1:
                        Master[active_cell] = teacher_Sub
                    elif j == 2:
                        Master[active_cell] = Sub_dict[teacher_Sub]
                    elif j == 3:
                        Master[active_cell] = teacher_Wing
                    elif j == 4:
                        Master[active_cell] = Wing_dict[teacher_Wing]
                    elif j == 5:
                        t_SubId = sec_SubCount[teacher_Sub]
                        if t_SubId < 10:
                            teacher_Code = Sub_dict[teacher_Sub] + Wing_dict[teacher_Wing] + '0' + str(t_SubId)
                        else:
                            teacher_Code = Sub_dict[teacher_Sub] + Wing_dict[teacher_Wing] + str(t_SubId)
                        sec_SubCount[teacher_Sub] += 1

                        t_sec.append(teacher_Code)
                        Master[active_cell] = teacher_Code
                sec_count += 1
            
            i += 1
    load_sheet.save("Data.xlsx")

def get_pri_teacher_codes():
    return t_pri

def get_mid_teacher_codes():
    return t_mid

def get_sec_teacher_codes():
    return t_sec

def getSubDict():
    revSubDict = {}
    for key, value in Sub_dict.items():
        revSubDict[value] = key
    return revSubDict

def getWingDict():
    return Wing_dict

create_MasterSheet()