from openpyxl import Workbook, load_workbook
from MasterSheetMaker import getSubDict
from MasterSheetMaker import t_pri, t_mid, t_sec
from Constraints import lecPerWeek

load_data = load_workbook("Data.xlsx")
data = load_data["Master"]

subDict = getSubDict()
subCount = len(subDict)

class Teacher():
    def __init__(self, t_code):
        self.t_code = t_code

def teacher_list():
    print(subCount)
    print(t_pri, t_mid, t_sec, len(t_pri), len(t_mid), len(t_sec), sep = "\n")

def lecPerWeekCheck():
    pass

teacher_list()