from openpyxl import Workbook, load_workbook

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
            lecPerWeek[subName] = [Constraints_Input[priCell].value, Constraints_Input[midCell].value, Constraints_Input[secCell].value]
            i += 1

    return lecPerWeek

lecPerWeek = getlecPerWeek()