from openpyxl import Workbook, load_workbook
from MasterSheetMaker import *

load_data = load_workbook("Data.xlsx")
data = load_data["Master"]

class Teacher():
    def __init__(self, t_code):
        self.t_code = t_code

def teacher_list():
    subDict = getSubDict()
    print(Sub_dict)
    t_pri = get_pri_teacher_codes()
    t_mid = get_mid_teacher_codes()
    t_sec = get_sec_teacher_codes()
    print(t_pri, t_mid, t_sec, len(t_pri), len(t_mid), len(t_sec), sep = "\n")

teacher_list()