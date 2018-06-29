import os

os.chdir(r'C:\Users\Ahmad Walid Naimi\Desktop\Python Documents\py4e')

fname = 'mbox-short.txt'
handle = open(fname)

counts = dict()

for line in handle:
    words = line.split()
    if line.startswith('From') and len(words)>2:
        date = words[2]
        counts[date] = counts.get(date,0)+1
print(counts)
