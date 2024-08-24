from openpyxl import Workbook, load_workbook
from MasterSheetMaker import Sub_dict

load_sheet = load_workbook("Data.xlsx", data_only=True)
Constraints_Input = load_sheet["Constraints_Input"]

def getlecPerWeek():
    i = 3
    lecPerWeek = {}
    while True:
        nameCell = 'A' + str(i)
        priCell = 'B' + str(i)
        midCell = 'C' + str(i)
        secCell = 'D' + str(i)
        subName = Constraints_Input[nameCell].value
        if subName == None:
            break
        else:
            lecPerWeek[int(Sub_dict[subName])] = [Constraints_Input[priCell].value, Constraints_Input[midCell].value, Constraints_Input[secCell].value]
            i += 1
    
    return lecPerWeek

def getlecPerDay():
    i = 3
    lecPerDay = {}
    while True:
        nameCell = 'A' + str(i)
        priCell = 'E' + str(i)
        midCell = 'F' + str(i)
        secCell = 'G' + str(i)
        subName = Constraints_Input[nameCell].value
        if subName == None:
            break
        else:
            lecPerDay[int(Sub_dict[subName])] = [Constraints_Input[priCell].value, Constraints_Input[midCell].value, Constraints_Input[secCell].value]
            i += 1

    return lecPerDay

lecPerWeek = getlecPerWeek()
lecPerDay = getlecPerDay()

load_sheet.close()

if __name__ == '__main__':
    print(lecPerDay)
    print(lecPerWeek)