import os

os.chdir(r'C:\Users\Ahmad Walid Naimi\Desktop\Python Documents\py4e')

fname = 'mbox-short.txt'
handle = open(fname)

count = 0
sums = 0

for line in handle:
    if 'X-DSPAM-Confidence:' in line:
        spos = line.find(':')
        snum = line[spos+1:].strip()
        inum = float(snum)
        count = count + 1
        sums = sums + inum
    else:
        continue

aver = str(sums/count)

print('Average spam confidence:',aver)
