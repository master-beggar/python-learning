import os
from tkinter import filedialog, Tk

# root = Tk()
# root.filename = filedialog.askopenfilename()

os.chdir(r'C:\Users\Ahmad Walid Naimi\Desktop\Python Documents\py4e')

fname = 'mbox-short.txt'
handle = open(fname)

counts = dict()

for line in handle:
    words = line.split()
    if line.startswith('From') and len(words)>2:
        day = words[-2][0:2]
        counts[day] = counts.get(day,0)+1

sortedlist = sorted([(k,v) for k,v in counts.items()])

for key, value in sortedlist:
    print(key, value)
