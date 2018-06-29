from glob import glob
from os import chdir
import xlrd

all_projs = []
with open(r'C:\Users\Ahmad Walid Naimi\Desktop\projects.txt') as projs:
    for proj in projs:
        proj = proj.rstrip()
        all_projs.append(proj)

chdir(r'C:\Users\Ahmad Walid Naimi\Desktop\Forecasts')

scores = {}

for excel in glob('**\*.xlsx',recursive=True):
    words = excel.split('\\')
    proj_num = words[-1]
    proj_num = proj_num[:5]
    if proj_num in all_projs:
        xfile = xlrd.open_workbook(excel)
        sheet = xfile.sheet_by_index(0)
        score = sheet.cell_value(0,1)
        scores[proj_num] = score

vals = list(scores.values())

count = 0
sumt = 0
for i in vals:
    sumt += i
    count += 1

print(round(sumt/count,2))
print(scores)
